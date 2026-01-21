import serial
import time

class Sabertooth2x60Serial:
    def __init__(self, port='/dev/serial0', baudrate=9600, address=128):
        """
        Initialize Sabertooth serial control
        
        port: '/dev/serial0' or '/dev/ttyAMA0' or '/dev/ttyS0'
        """
        self.address = address
        
        # Try to find available port
        import os
        possible_ports = [port, '/dev/serial0', '/dev/ttyAMA0', '/dev/ttyS0']
        
        actual_port = None
        for p in possible_ports:
            if os.path.exists(p):
                actual_port = p
                break
        
        if actual_port is None:
            raise Exception("No serial port found! Enable UART with raspi-config")
        
        print(f"Using serial port: {actual_port}")
        
        self.serial = serial.Serial(
            port=actual_port,
            baudrate=baudrate,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            timeout=1
        )
        time.sleep(0.1)
        print(f"Sabertooth initialized at {baudrate} baud, address {address}\n")
    
    def _send_command(self, command, data):
        """Send packetized serial command"""
        data = max(0, min(127, data))
        checksum = (self.address + command + data) & 0x7F
        packet = bytes([self.address, command, data, checksum])
        self.serial.write(packet)
        return packet
    
    def motor1_forward(self, speed):
        speed = max(0, min(127, speed))
        packet = self._send_command(0, speed)
        print(f"M1 Forward: {speed}/127 | Packet: {[hex(b) for b in packet]}")
    
    def motor1_reverse(self, speed):
        speed = max(0, min(127, speed))
        packet = self._send_command(1, speed)
        print(f"M1 Reverse: {speed}/127 | Packet: {[hex(b) for b in packet]}")
    
    def motor2_forward(self, speed):
        speed = max(0, min(127, speed))
        packet = self._send_command(4, speed)
        print(f"M2 Forward: {speed}/127 | Packet: {[hex(b) for b in packet]}")
    
    def motor2_reverse(self, speed):
        speed = max(0, min(127, speed))
        packet = self._send_command(5, speed)
        print(f"M2 Reverse: {speed}/127 | Packet: {[hex(b) for b in packet]}")
    
    def set_motor1(self, speed):
        """speed: -127 to +127"""
        if speed >= 0:
            self.motor1_forward(speed)
        else:
            self.motor1_reverse(abs(speed))
    
    def set_motor2(self, speed):
        """speed: -127 to +127"""
        if speed >= 0:
            self.motor2_forward(speed)
        else:
            self.motor2_reverse(abs(speed))
    
    def stop_all(self):
        print("Stopping all motors")
        self.motor1_forward(0)
        self.motor2_forward(0)
    
    def cleanup(self):
        self.stop_all()
        time.sleep(0.1)
        self.serial.close()
        print("Serial connection closed")


if __name__ == "__main__":
    print("=" * 70)
    print("SABERTOOTH SERIAL CONTROL")
    print("=" * 70)
    
    # Try to create connection (will auto-detect port)
    try:
        motor = Sabertooth2x60Serial()
    except Exception as e:
        print(f"\nError: {e}")
        print("\nPlease enable UART:")
        print("1. Run: sudo raspi-config")
        print("2. Interface Options → Serial Port")
        print("3. Login shell over serial: NO")
        print("4. Serial hardware enabled: YES")
        print("5. Reboot")
        exit(1)
    
    try:
        print("\n--- Testing Motor 1 ---")
        
        motor.set_motor1(0)
        motor.set_motor2(0)
        time.sleep(5)
        
        motor.set_motor1(64)
        motor.set_motor2(-64)
        time.sleep(5)


        motor.set_motor1(0)
        motor.set_motor2(0)
        time.sleep(5)

        motor.set_motor1(-64)
        motor.set_motor2(64)
        time.sleep(5)
        
        motor.set_motor1(0)
        motor.set_motor2(0)
        time.sleep(5)
        
        motor.set_motor1(64)
        motor.set_motor2(64)
        time.sleep(5)

        motor.set_motor1(64)
        motor.set_motor2(-64)
        time.sleep(5)
        
        motor.set_motor1(0)
        motor.set_motor2(0)


        motor.set_motor1(-64)
        motor.set_motor2(-64)
        time.sleep(5)


        motor.set_motor1(-64)
        motor.set_motor2(64)
        time.sleep(5)


        motor.set_motor1(0)
        motor.set_motor2(0)
        time.sleep(5)
        print("\nTest complete!")
        
    except KeyboardInterrupt:
        print("\nInterrupted")
    finally:
        motor.cleanup()
