# SGR-1

# SGR-1 Rover

<p align="center">
  <img src="https://img.shields.io/badge/Raspberry%20Pi-4B-C51A4A?logo=raspberry-pi" alt="Raspberry Pi 4B">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Status-In%20Development-yellow" alt="Status">
</p>

A Mars rover-inspired autonomous ground vehicle built with Raspberry Pi 4B, featuring advanced navigation, object detection, and obstacle avoidance capabilities.

## 🚀 Overview

SGR-1 (Smart Ground Rover - 1) is an autonomous rover platform designed with inspiration from Mars exploration rovers. It combines robust motor control, computer vision, GPS navigation, and inertial measurement capabilities to navigate complex terrains autonomously.

## ✨ Features

- **Autonomous Navigation**: GPS-based waypoint navigation with real-time position tracking
- **Object Detection**: Pi Camera-based computer vision for obstacle detection and avoidance
- **Robust Motor Control**: Dual 60A Sabertooth motor driver for powerful and precise movement
- **Orientation Tracking**: MPU6050 IMU for accurate heading and tilt measurements
- **Mars Rover Design**: Chassis inspired by proven Mars rover engineering principles
- **Real-time Decision Making**: Onboard processing for quick response to environmental changes

## 🔧 Hardware Components

### Core Components
- **Brain**: Raspberry Pi 4B (4GB/8GB recommended)
- **Motor Controller**: Sabertooth Dual 60A Motor Driver
- **Vision**:  Raspberry Pi Camera Module (v2 or HQ)
- **GPS**: NEO-6M GPS Module
- **IMU**: MPU6050 6-Axis Accelerometer & Gyroscope

### Power System
- Battery pack (recommend 12V LiPo or Li-Ion)
- Voltage regulator for 5V supply to Raspberry Pi
- Power distribution board

### Motors & Chassis
- DC motors compatible with Sabertooth driver
- Mars rover-inspired suspension system
- Rocker-bogie or similar suspension mechanism

## 📋 Prerequisites

### Software Requirements
```bash
Python 3.7+
OpenCV
TensorFlow/PyTorch (for object detection models)
GPS libraries (gpsd)
IMU libraries (smbus, mpu6050-raspberrypi)
```

### System Setup
```bash
# Update system
sudo apt-get update && sudo apt-get upgrade -y

# Install Python dependencies
sudo apt-get install python3-pip python3-opencv -y

# Install required Python packages
pip3 install numpy
pip3 install pyserial
pip3 install gps
pip3 install mpu6050-raspberrypi
```

## 🛠️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/shresthasameerman/SGR-1.git
cd SGR-1
```

2. **Install dependencies**
```bash
pip3 install -r requirements.txt
```

3. **Configure hardware connections**
   - Connect Sabertooth motor driver to Raspberry Pi GPIO
   - Set up Pi Camera module
   - Connect NEO-6M GPS via USB or UART
   - Connect MPU6050 via I2C

4. **Enable necessary interfaces**
```bash
sudo raspi-config
# Enable Camera, I2C, Serial
```

## 🔌 Hardware Connections

### Sabertooth Motor Driver
- S1 (Motor 1) → GPIO Pin (PWM)
- S2 (Motor 2) → GPIO Pin (PWM)
- GND → Raspberry Pi GND

### NEO-6M GPS Module
- VCC → 3.3V/5V
- GND → GND
- TX → RX (GPIO 15)
- RX → TX (GPIO 14)

### MPU6050 IMU
- VCC → 3.3V
- GND → GND
- SDA → GPIO 2 (SDA)
- SCL → GPIO 3 (SCL)

### Pi Camera
- Connect via CSI camera port

## 🚦 Usage

### Basic Operation
```bash
# Start the rover system
python3 main.py
```

### Navigation Mode
```bash
# Set target GPS coordinates
python3 navigate.py --lat 27.1234 --lon 85.5678
```

### Object Detection Mode
```bash
# Run object detection and obstacle avoidance
python3 vision.py
```

## 📂 Project Structure

```
SGR-1/
├── src/
│   ├── motor_control.py      # Motor driver interface
│   ├── gps_navigation.py     # GPS and navigation logic
│   ├── vision. py             # Object detection & avoidance
│   ├── imu_sensor.py         # MPU6050 interface
│   └── main.py               # Main control loop
├── config/
│   └── settings.yaml         # Configuration file
├── models/
│   └── object_detection/     # Trained models
├── tests/
│   └── hardware_tests.py     # Hardware testing scripts
├── docs/
│   └── wiring_diagram.png    # Circuit diagrams
├── requirements.txt
└── README.md
```

## 🎯 Roadmap

- [x] Basic motor control implementation
- [x] GPS module integration
- [x] IMU sensor integration
- [ ] Object detection model training
- [ ] Autonomous navigation algorithm
- [ ] Obstacle avoidance system
- [ ] Web-based control interface
- [ ] Telemetry dashboard
- [ ] Path planning optimization

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**shresthasameerman**
- GitHub: [@shresthasameerman](https://github.com/shresthasameerman)

## 🙏 Acknowledgments

- Mars rover designs by NASA/JPL for inspiration
- Raspberry Pi Foundation
- OpenCV and TensorFlow communities

## 📸 Gallery

_Coming soon:  Photos and videos of SGR-1 in action! _

## 📞 Support

For questions or issues, please open an issue in the GitHub repository.

---

**Happy Roving!  🤖🔴**
