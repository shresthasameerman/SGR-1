import smbus
import time

# MPU6050 Registers
PWR_MGMT_1 = 0x6B
ACCEL_XOUT_H = 0x3B
GYRO_XOUT_H = 0x43

bus = smbus.SMBus(1)  # I2C bus 1
address = 0x68        # MPU6050 default address

# Wake up the MPU6050
bus.write_byte_data(address, PWR_MGMT_1, 0)

def read_raw_data(addr):
    high = bus.read_byte_data(address, addr)
    low = bus.read_byte_data(address, addr + 1)
    value = (high << 8) | low
    if value > 32768:
        value = value - 65536
    return value

while True:
    # Read accelerometer data
    acc_x = read_raw_data(ACCEL_XOUT_H)
    acc_y = read_raw_data(ACCEL_XOUT_H + 2)
    acc_z = read_raw_data(ACCEL_XOUT_H + 4)
    
    # Read gyroscope data
    gyro_x = read_raw_data(GYRO_XOUT_H)
    gyro_y = read_raw_data(GYRO_XOUT_H + 2)
    gyro_z = read_raw_data(GYRO_XOUT_H + 4)
    
    print(f"Accel: X={acc_x} Y={acc_y} Z={acc_z}")
    print(f"Gyro:  X={gyro_x} Y={gyro_y} Z={gyro_z}\n")
    
    time.sleep(1)

