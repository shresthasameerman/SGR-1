import cv2
import numpy as np
from picamera2 import Picamera2
import time
from flask import Flask, Response
import threading

# --- Flask app for streaming ---
app = Flask(__name__)
output_frame = None
lock = threading.Lock()

# --- Load COCO classes ---
classNames = []
with open("coco.names", "rt") as f:
    classNames = f.read().rstrip("\n").split("\n")

# --- Load DNN model ---
configPath = "ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
weightsPath = "frozen_inference_graph.pb"
net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

# --- Zone functions ---
def get_zone(box, img_width):
    x_center = box[0] + box[2] / 2
    if x_center < img_width / 3:
        return "LEFT"
    elif x_center < 2 * img_width / 3:
        return "CENTER"
    else:
        return "RIGHT"

def calculate_distance(box):
    area = box[2] * box[3]
    if area > 50000:
        return "VERY_CLOSE"
    elif area > 30000:
        return "CLOSE"
    elif area > 15000:
        return "MEDIUM"
    else:
        return "FAR"

def get_avoidance_action(objectInfo, img_width):
    if len(objectInfo) == 0:
        return "MOVE_FORWARD", "No obstacles detected"
    zones = {"LEFT": [], "CENTER": [], "RIGHT": []}
    for box, className in objectInfo:
        zone = get_zone(box, img_width)
        distance = calculate_distance(box)
        zones[zone].append((className, distance, box))
    if zones["CENTER"]:
        closest = min(zones["CENTER"], key=lambda x: ["FAR","MEDIUM","CLOSE","VERY_CLOSE"].index(x[1]))
        if closest[1] in ["VERY_CLOSE", "CLOSE"]:
            if len(zones["LEFT"]) < len(zones["RIGHT"]):
                return "TURN_LEFT", f"Avoiding {closest[0]} in center - turning left"
            else:
                return "TURN_RIGHT", f"Avoiding {closest[0]} in center - turning right"
        else:
            return "SLOW_DOWN", f"{closest[0]} detected ahead - slowing down"
    if zones["LEFT"] and any(d in ["VERY_CLOSE","CLOSE"] for _,d,_ in zones["LEFT"]):
        return "TURN_RIGHT", "Obstacle on left - turning right"
    if zones["RIGHT"] and any(d in ["VERY_CLOSE","CLOSE"] for _,d,_ in zones["RIGHT"]):
        return "TURN_LEFT", "Obstacle on right - turning left"
    return "MOVE_FORWARD", "Path clear"

# --- Object detection ---
def getObjects(img, thres=0.45, nms=0.2, draw=True, objects=[]):
    classIds, confs, bbox = net.detect(img, confThreshold=thres, nmsThreshold=nms)
    if len(objects) == 0:
        objects = classNames
    objectInfo = []

    if len(classIds) != 0:
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
            if classId < 1 or classId > len(classNames):
                continue
            className = classNames[classId - 1]
            if className in objects:
                objectInfo.append([box, className])
                if draw:
                    zone = get_zone(box, img.shape[1])
                    distance = calculate_distance(box)
                    color = {"VERY_CLOSE":(0,0,255),"CLOSE":(0,165,255),"MEDIUM":(0,255,255),"FAR":(0,255,0)}[distance]
                    cv2.rectangle(img, box, color=color, thickness=2)
                    cv2.putText(img, f"{className.upper()}", (box[0]+10, box[1]+30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
                    cv2.putText(img, f"{round(confidence*100,2)}%", (box[0]+10, box[1]+55),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
                    cv2.putText(img, f"{zone} - {distance}", (box[0]+10, box[1]+80),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
    return img, objectInfo

# --- Motor commands ---
def motor_control(action):
    commands = {
        "MOVE_FORWARD": "Motors: Left=100%, Right=100%",
        "TURN_LEFT": "Motors: Left=30%, Right=100%",
        "TURN_RIGHT": "Motors: Left=100%, Right=30%",
        "SLOW_DOWN": "Motors: Left=50%, Right=50%",
        "STOP": "Motors: Left=0%, Right=0%"
    }
    return commands.get(action, "Unknown command")

# --- Camera processing thread ---
def camera_thread():
    global output_frame
    picam2 = Picamera2()
    config = picam2.create_preview_configuration(main={"size": (640,480), "format":"RGB888"})
    picam2.configure(config)
    picam2.start()
    time.sleep(2)
    frame_count = 0

    while True:
        img = picam2.capture_array()
        frame_count += 1

        # Detect objects
        result, objectInfo = getObjects(img, 0.45, 0.2)

        # Get avoidance action
        action, message = get_avoidance_action(objectInfo, img.shape[1])
        motor_cmd = motor_control(action)
        print(f"[Frame {frame_count}] {len(objectInfo)} objects | {action} | {motor_cmd}")

        # Encode frame for streaming
        with lock:
            ret, jpeg = cv2.imencode(".jpg", img)
            output_frame = jpeg.tobytes()

# --- Flask route for video streaming ---
@app.route("/video_feed")
def video_feed():
    def generate():
        global output_frame
        while True:
            with lock:
                if output_frame is None:
                    continue
                frame = output_frame
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    return Response(generate(),
                    mimetype="multipart/x-mixed-replace; boundary=frame")

# --- Start camera thread and Flask server ---
if __name__ == "__main__":
    t = threading.Thread(target=camera_thread, daemon=True)
    t.start()
    print("Starting Flask server on http://0.0.0.0:5000/video_feed")
    app.run(host="0.0.0.0", port=5000, debug=False, threaded=True)
