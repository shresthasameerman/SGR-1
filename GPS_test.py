#!/usr/bin/env python3
import socket
import json
import time
import math
from datetime import datetime

def calculate_bearing(lat1, lon1, lat2, lon2):
    """Calculate bearing from point 1 to point 2 in degrees (0-360)"""
    lat1_rad = math.radians(lat1)
    lat2_rad = math.radians(lat2)
    lon_diff = math.radians(lon2 - lon1)
    
    x = math.sin(lon_diff) * math.cos(lat2_rad)
    y = math.cos(lat1_rad) * math.sin(lat2_rad) - math.sin(lat1_rad) * math.cos(lat2_rad) * math.cos(lon_diff)
    
    bearing_rad = math.atan2(x, y)
    bearing_deg = math.degrees(bearing_rad)
    bearing_deg = (bearing_deg + 360) % 360
    
    return bearing_deg

def calculate_distance(lat1, lon1, lat2, lon2):
    """Calculate distance between two points in meters"""
    R = 6371000
    lat1_rad = math.radians(lat1)
    lat2_rad = math.radians(lat2)
    delta_lat = math.radians(lat2 - lat1)
    delta_lon = math.radians(lon2 - lon1)
    
    a = math.sin(delta_lat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    
    return R * c

def get_direction_name(bearing):
    """Convert bearing to compass direction"""
    directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
                  "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    index = round(bearing / 22.5) % 16
    return directions[index]

def get_turn_instruction(current_heading, target_bearing):
    """Calculate turn angle and direction"""
    diff = target_bearing - current_heading
    
    if diff > 180:
        diff -= 360
    elif diff < -180:
        diff += 360
    
    if diff >= 0:
        return abs(diff), "RIGHT"
    else:
        return abs(diff), "LEFT"

# Get user inputs
print("=" * 60)
print("GPS NAVIGATION SYSTEM - STATIC HEADING MODE")
print("=" * 60)

# Get static heading (device orientation)
print("\n--- DEVICE HEADING SETUP ---")
print("Enter the direction your device is facing (0-360 degrees)")
print("Examples: 0=North, 90=East, 180=South, 270=West")

while True:
    try:
        static_heading = float(input("\nDevice Heading (degrees): "))
        if 0 <= static_heading < 360:
            break
        else:
            print("Please enter a value between 0 and 360")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

print(f"Device heading set to: {static_heading:.1f}° ({get_direction_name(static_heading)})")

# Get target coordinates
print("\n--- TARGET COORDINATES ---")
while True:
    try:
        target_lat = float(input("Target Latitude: "))
        target_lon = float(input("Target Longitude: "))
        break
    except ValueError:
        print("Invalid input! Please enter valid numbers.")

print(f"\nTarget set to: {target_lat:.6f}, {target_lon:.6f}")
print("Connecting to GPSD...\n")

# Variables to track satellite information
satellites_used = 0
satellites_visible = 0

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)
    sock.connect(('127.0.0.1', 2947))
    print("Connected to GPSD successfully!\n")
    
    sock.send(b'?WATCH={"enable":true,"json":true}\n')
    
    buffer = ""
    
    while True:
        data = sock.recv(4096).decode('utf-8')
        buffer += data
        
        while '\n' in buffer:
            line, buffer = buffer.split('\n', 1)
            line = line.strip()
            
            if not line:
                continue
                
            try:
                obj = json.loads(line)
                
                # Handle SKY class messages for satellite data
                if obj.get('class') == 'SKY':
                    satellites_visible = len(obj.get('satellites', []))
                    satellites_used = obj.get('uSat', 0)
                
                if obj.get('class') == 'TPV' and 'lat' in obj and 'lon' in obj:
                    latitude = obj['lat']
                    longitude = obj['lon']
                    altitude = obj.get('alt', 'N/A')
                    speed = obj.get('speed', 'N/A')
                    
                    # Calculate navigation using STATIC heading
                    bearing = calculate_bearing(latitude, longitude, target_lat, target_lon)
                    distance = calculate_distance(latitude, longitude, target_lat, target_lon)
                    direction = get_direction_name(bearing)
                    
                    # Calculate turn based on STATIC heading
                    turn_angle, turn_dir = get_turn_instruction(static_heading, bearing)
                    
                    # Display
                    print("\033[2J\033[H")
                    print("=" * 60)
                    print("GPS NAVIGATION - STATIC HEADING MODE")
                    print("=" * 60)
                    
                    print("\n--- SATELLITE INFO ---")
                    print(f"Satellites Used:    {satellites_used}")
                    print(f"Satellites Visible: {satellites_visible}")
                    
                    print("\n--- DEVICE ORIENTATION ---")
                    print(f"Device Facing: {static_heading:.1f}° ({get_direction_name(static_heading)})")
                    print("(This is your fixed reference direction)")
                    
                    print("\n--- CURRENT POSITION ---")
                    print(f"Time:      {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                    print(f"Latitude:  {latitude:.6f}°")
                    print(f"Longitude: {longitude:.6f}°")
                    
                    if altitude != 'N/A':
                        print(f"Altitude:  {altitude:.2f} m")
                    
                    if speed != 'N/A':
                        print(f"Speed:     {speed:.2f} m/s ({speed*3.6:.2f} km/h)")
                    
                    print("\n--- TARGET POSITION ---")
                    print(f"Target:    {target_lat:.6f}, {target_lon:.6f}")
                    
                    print("\n--- NAVIGATION ---")
                    print(f"Distance to target:  {distance:.2f} m ({distance/1000:.3f} km)")
                    print(f"Bearing to target:   {bearing:.1f}° ({direction})")
                    
                    if distance > 5:
                        print(f"\n*** TURN INSTRUCTION ***")
                        if turn_angle < 5:
                            print("  >> GO STRAIGHT AHEAD <<")
                        else:
                            print(f"  >> TURN {turn_dir} {turn_angle:.1f}° <<")
                            
                        # Additional visual indicator
                        print(f"\nRelative Direction: ", end="")
                        if turn_angle < 5:
                            print("STRAIGHT ↑")
                        elif turn_dir == "RIGHT":
                            if turn_angle < 45:
                                print("SLIGHT RIGHT ↗")
                            elif turn_angle < 135:
                                print("RIGHT →")
                            else:
                                print("SHARP RIGHT ↘")
                        else:  # LEFT
                            if turn_angle < 45:
                                print("SLIGHT LEFT ↖")
                            elif turn_angle < 135:
                                print("LEFT ←")
                            else:
                                print("SHARP LEFT ↙")
                    else:
                        print("\n*** 🎯 TARGET REACHED! ***")
                    
                    print("\n" + "=" * 60)
                    print("Press Ctrl+C to stop | 'h' to change heading")
                    print("=" * 60)
                    
            except json.JSONDecodeError:
                pass
            except Exception as e:
                print(f"Error processing data: {e}")
        
except KeyboardInterrupt:
    print("\n\nGPS Navigation Stopped")
except Exception as e:
    print(f"\nError: {e}")
    import traceback
    traceback.print_exc()
finally:
    try:
        sock.close()
    except:
        pass
