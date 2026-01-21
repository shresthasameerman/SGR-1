import serial
import time
import sys
import termios
import tty
import os
import threading

class ContinuousRobotControl:
    def __init__(self):
        # Auto-detect serial port
        possible_ports = ['/dev/serial0', '/dev/ttyAMA0', '/dev/ttyS0']
        port = None
        for p in possible_ports:
            if os.path.exists(p):
                port = p
                break
        
        if not port:
            raise Exception("No serial port found!")
        
        self.serial = serial.Serial(port, 9600)
        time.sleep(0.1)
        print(f"Connected to {port}\n")
        
        self.address = 128
        self.current_command = None
        self.running = True
        
        # Start continuous command thread
        self.command_thread = threading.Thread(target=self._continuous_send, daemon=True)
        self.command_thread.start()
    
    def _send_command(self, motor1_cmd, motor1_data, motor2_cmd, motor2_data):
        """Send commands to both motors"""
        # Motor 1
        data1 = max(0, min(127, motor1_data))
        checksum1 = (self.address + motor1_cmd + data1) & 0x7F
        packet1 = bytes([self.address, motor1_cmd, data1, checksum1])
        
        # Motor 2
        data2 = max(0, min(127, motor2_data))
        checksum2 = (self.address + motor2_cmd + data2) & 0x7F
        packet2 = bytes([self.address, motor2_cmd, data2, checksum2])
        
        self.serial.write(packet1)
        self.serial.write(packet2)
    
    def _continuous_send(self):
        """Continuously send current command at 20Hz"""
        while self.running:
            if self.current_command == 'FORWARD':
                # Both motors forward at 67
                self._send_command(0, 67, 4, 67)  # M1 forward, M2 forward
            elif self.current_command == 'BACKWARD':
                # Both motors reverse at 67
                self._send_command(1, 67, 5, 67)  # M1 reverse, M2 reverse
            elif self.current_command == 'LEFT':
                # Left motor reverse, right motor forward (tank turn)
                self._send_command(1, 67, 4, 67)  # M1 reverse, M2 forward
            elif self.current_command == 'RIGHT':
                # Left motor forward, right motor reverse (tank turn)
                self._send_command(0, 67, 5, 67)  # M1 forward, M2 reverse
            else:
                # STOP - both motors at 0
                self._send_command(0, 0, 4, 0)
            
            time.sleep(0.05)  # Send commands at 20Hz
    
    def set_command(self, command):
        """Set the current movement command"""
        self.current_command = command
    
    def stop(self):
        """Stop all motors"""
        self.current_command = None
    
    def get_key(self):
        """Get single keypress without blocking"""
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
            return ch
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
    
    def print_status(self):
        """Print current status"""
        os.system('clear')
        print("=" * 60)
        print("CONTINUOUS ROBOT CONTROL - WASD")
        print("=" * 60)
        print("\nControls:")
        print("  W : Forward")
        print("  S : Backward")
        print("  A : Turn Left")
        print("  D : Turn Right")
        print("  Q : Quit")
        print()
        print("Hold key to move, release to stop")
        print("-" * 60)
        
        if self.current_command == 'FORWARD':
            print("Status: ▲ MOVING FORWARD")
        elif self.current_command == 'BACKWARD':
            print("Status: ▼ MOVING BACKWARD")
        elif self.current_command == 'LEFT':
            print("Status: ◄ TURNING LEFT")
        elif self.current_command == 'RIGHT':
            print("Status: ► TURNING RIGHT")
        else:
            print("Status: ■ STOPPED")
        
        print("=" * 60)
    
    def run(self):
        """Main control loop"""
        try:
            self.print_status()
            
            while self.running:
                key = self.get_key()
                
                if key.lower() == 'q':
                    print("\nQuitting...")
                    self.running = False
                    break
                    
                elif key.lower() == 'd':
                    self.set_command('FORWARD')
                    self.print_status()
                    
                elif key.lower() == 'a':
                    self.set_command('BACKWARD')
                    self.print_status()
                    
                elif key.lower() == 'w':
                    self.set_command('LEFT')
                    self.print_status()
                    
                elif key.lower() == 's':
                    self.set_command('RIGHT')
                    self.print_status()
                
                else:
                    # Any other key stops the robot
                    self.stop()
                    self.print_status()
                
        except KeyboardInterrupt:
            print("\n\nInterrupted!")
            
        finally:
            self.running = False
            self.stop()
            time.sleep(0.2)
            self.serial.close()
            print("Motors stopped and cleaned up.")


if __name__ == "__main__":
    print("=" * 60)
    print("INITIALIZING CONTINUOUS ROBOT CONTROL")
    print("=" * 60)
    print("\nSetup checklist:")
    print("✓ DIP switch 1: DOWN (serial mode)")
    print("✓ DIP switch 2: DOWN (9600 baud)")
    print("✓ Pi TX (GPIO 14) → Sabertooth S1")
    print("✓ Pi GND → Sabertooth 0V")
    print("✓ Both motors connected (M1 = left, M2 = right)")
    print()
    
    input("Press Enter to start...")
    
    try:
        robot = ContinuousRobotControl()
        robot.run()
    except Exception as e:
        print(f"\nError: {e}")
        print("\nTroubleshooting:")
        print("1. Enable UART: sudo raspi-config → Interface Options → Serial")
        print("2. Check connections")
