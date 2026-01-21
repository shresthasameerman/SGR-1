import cv2
import numpy as np

# Import the Open-CV extra functionalities
classNames = []
classFile = "/Users/rakshyatamang/Downloads/Object_Detection_Files/Object_Detection_Files/coco.names"
with open(classFile,"rt") as f:
    classNames = f.read().rstrip("\n").split("\n")

# Pull the information about what each object should look like
configPath = "/Users/rakshyatamang/Downloads/Object_Detection_Files/Object_Detection_Files/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
weightsPath = "/Users/rakshyatamang/Downloads/Object_Detection_Files/Object_Detection_Files/frozen_inference_graph.pb"

# Set up values to get good results
net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

# Define zones for avoidance (divide screen into left, center, right)
def get_zone(box, img_width):
    """Determine which zone the object is in"""
    x_center = box[0] + box[2] / 2
    
    if x_center < img_width / 3:
        return "LEFT"
    elif x_center < 2 * img_width / 3:
        return "CENTER"
    else:
        return "RIGHT"

def calculate_distance(box):
    """Estimate distance based on bounding box size (larger = closer)"""
    area = box[2] * box[3]  # width * height
    
    if area > 50000:
        return "VERY_CLOSE"
    elif area > 30000:
        return "CLOSE"
    elif area > 15000:
        return "MEDIUM"
    else:
        return "FAR"

def get_avoidance_action(objectInfo, img_width):
    """Determine what action to take based on detected objects"""
    if len(objectInfo) == 0:
        return "MOVE_FORWARD", "No obstacles detected"
    
    # Analyze all detected objects
    zones = {"LEFT": [], "CENTER": [], "RIGHT": []}
    
    for box, className in objectInfo:
        zone = get_zone(box, img_width)
        distance = calculate_distance(box)
        zones[zone].append((className, distance, box))
    
    # Priority: avoid center obstacles first
    if zones["CENTER"]:
        closest = min(zones["CENTER"], key=lambda x: x[1])
        if closest[1] in ["VERY_CLOSE", "CLOSE"]:
            # Check which side is clearer
            if len(zones["LEFT"]) < len(zones["RIGHT"]):
                return "TURN_LEFT", f"Avoiding {closest[0]} in center - turning left"
            else:
                return "TURN_RIGHT", f"Avoiding {closest[0]} in center - turning right"
        else:
            return "SLOW_DOWN", f"{closest[0]} detected ahead - slowing down"
    
    # Check side obstacles
    if zones["LEFT"] and any(d in ["VERY_CLOSE", "CLOSE"] for _, d, _ in zones["LEFT"]):
        return "TURN_RIGHT", "Obstacle on left - turning right"
    
    if zones["RIGHT"] and any(d in ["VERY_CLOSE", "CLOSE"] for _, d, _ in zones["RIGHT"]):
        return "TURN_LEFT", "Obstacle on right - turning left"
    
    return "MOVE_FORWARD", "Path clear"

def getObjects(img, thres, nms, draw=True, objects=[]):
    classIds, confs, bbox = net.detect(img, confThreshold=thres, nmsThreshold=nms)
    
    if len(objects) == 0: 
        objects = classNames
    
    objectInfo = []
    
    if len(classIds) != 0:
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
            className = classNames[classId - 1]
            if className in objects: 
                objectInfo.append([box, className])
                
                if draw:
                    # Get zone and distance info
                    zone = get_zone(box, img.shape[1])
                    distance = calculate_distance(box)
                    
                    # Color code based on distance
                    if distance == "VERY_CLOSE":
                        color = (0, 0, 255)  # Red
                    elif distance == "CLOSE":
                        color = (0, 165, 255)  # Orange
                    elif distance == "MEDIUM":
                        color = (0, 255, 255)  # Yellow
                    else:
                        color = (0, 255, 0)  # Green
                    
                    # Draw rectangle
                    cv2.rectangle(img, box, color=color, thickness=2)
                    
                    # Draw labels
                    label = f"{className.upper()}"
                    cv2.putText(img, label, (box[0] + 10, box[1] + 30),
                               cv2.FONT_HERSHEY_COMPLEX, 0.6, color, 2)
                    
                    conf_label = f"{round(confidence*100, 2)}%"
                    cv2.putText(img, conf_label, (box[0] + 10, box[1] + 55),
                               cv2.FONT_HERSHEY_COMPLEX, 0.6, color, 2)
                    
                    # Add zone and distance info
                    info_label = f"{zone} - {distance}"
                    cv2.putText(img, info_label, (box[0] + 10, box[1] + 80),
                               cv2.FONT_HERSHEY_COMPLEX, 0.5, color, 1)
    
    return img, objectInfo

def draw_zones(img):
    """Draw visual zones on the image"""
    height, width = img.shape[:2]
    
    # Draw vertical lines to show zones
    cv2.line(img, (width//3, 0), (width//3, height), (255, 255, 255), 1)
    cv2.line(img, (2*width//3, 0), (2*width//3, height), (255, 255, 255), 1)
    
    # Label zones
    cv2.putText(img, "LEFT", (width//6 - 30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(img, "CENTER", (width//2 - 50, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(img, "RIGHT", (5*width//6 - 30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    
    return img

def motor_control(action):
    """
    Placeholder function for motor control
    Connect this to your robot's motor controller
    """
    # Example GPIO/motor control code would go here
    # For example, using RPi.GPIO or similar library
    
    commands = {
        "MOVE_FORWARD": "Motors: Left=100%, Right=100%",
        "TURN_LEFT": "Motors: Left=30%, Right=100%",
        "TURN_RIGHT": "Motors: Left=100%, Right=30%",
        "SLOW_DOWN": "Motors: Left=50%, Right=50%",
        "STOP": "Motors: Left=0%, Right=0%"
    }
    
    return commands.get(action, "Unknown command")

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    
    # Object tracking variables
    frame_count = 0
    detection_log = []
    
    print("Object Detection and Avoidance System Started")
    print("Press 'q' to quit")
    print("Press 's' to toggle zone display")
    print("Press 'p' to pause/resume")
    
    show_zones = True
    paused = False
    
    while True:
        if not paused:
            success, img = cap.read()
            if not success:
                break
            
            frame_count += 1
            
            # Detect objects
            result, objectInfo = getObjects(img, 0.45, 0.2)
            
            # Draw zones if enabled
            if show_zones:
                img = draw_zones(img)
            
            # Get avoidance action
            action, message = get_avoidance_action(objectInfo, img.shape[1])
            
            # Display action on screen
            cv2.rectangle(img, (0, img.shape[0] - 60), (img.shape[1], img.shape[0]), (0, 0, 0), -1)
            cv2.putText(img, f"Action: {action}", (10, img.shape[0] - 35),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(img, message, (10, img.shape[0] - 10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            
            # Log detected objects (every 30 frames)
            if frame_count % 30 == 0 and objectInfo:
                motor_cmd = motor_control(action)
                print(f"Frame {frame_count}: {len(objectInfo)} objects | {action} | {motor_cmd}")
                for box, className in objectInfo:
                    zone = get_zone(box, img.shape[1])
                    distance = calculate_distance(box)
                    print(f"  - {className}: {zone} zone, {distance}")
            
            cv2.imshow("Object Detection & Avoidance", img)
        
        # Handle keyboard input
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord('q'):
            break
        elif key == ord('s'):
            show_zones = not show_zones
        elif key == ord('p'):
            paused = not paused
            print("PAUSED" if paused else "RESUMED")
    
    cap.release()
    cv2.destroyAllWindows()
    print("System stopped")
