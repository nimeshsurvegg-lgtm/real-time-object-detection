<div align="center">
  <h1>👁️ Object Detection Assistant</h1>
  <h3><em>Real-time object detection with YOLOv8 and Voice Feedback</em></h3>
</div>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Model-YOLOv8-orange.svg" alt="YOLOv8">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT">
</p>

> **Overview:** The Object Detection Assistant is a desktop application that uses your computer's webcam to perform real-time object detection using the YOLOv8 machine learning model. It features a clean Tkinter GUI and integrates Text-to-Speech (TTS) to audibly announce objects as they appear on screen.

---

## 📖 Table of Contents
- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage](#-usage)
- [Technical Stack](#-technical-stack)
- [The Team](#-the-team)
- [License](#-license)

---

## 🚀 Features

* **Real-Time Detection:** Utilizes Ultralytics YOLOv8 for fast and accurate object bounding box generation.
* **Audio Feedback:** Uses `pyttsx3` to announce detected objects out loud.
* **Smart Cooldown System:** Prevents audio spam by implementing a cooldown timer, ensuring an object isn't repeatedly announced every single frame.
* **Graphical Interface:** Built with Tkinter, featuring a live video feed and simple Start/Stop/Quit controls.
* **Asynchronous Audio:** Audio plays on a separate daemon thread so the video feed never stutters or freezes while the system is speaking.

---

## ⚙️ Prerequisites

* Python 3.8 or higher
* A working webcam attached to your computer

---

## 💻 Installation

1. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/nimeshsurvegg-lgtm/object-detection-assistant.git](https://github.com/nimeshsurvegg-lgtm/object-detection-assistant.git)
   cd object-detection-assistant

2. (Optional but recommended) Create a virtual environment:
 ```bash
   git clone [https://github.com/nimeshsurvegg-lgtm/object-detection-assistant.git](https://github.com/nimeshsurvegg-lgtm/object-detection-assistant.git)
   cd object-detection-assistant
 ```

3.Install the required dependencies:
 ```bash
pip install -r requirements.txt
 ```
## 🎮 Usage
Run the main Python script to launch the application:

 ```bash
python objdetect.py
 ```
1. Click Start Camera to begin the video feed and object detection. (Note: The YOLOv8 model weights yolov8n.pt will automatically download on the first run).

2. Listen for audio announcements as objects enter the frame.

3. Click Stop Camera to pause the feed, or Quit to close the application cleanly.

## 🧠 Technical Stack
Computer Vision: opencv-python (cv2)

Machine Learning: ultralytics (YOLOv8 Nano)

Text-to-Speech: pyttsx3

GUI: tkinter, Pillow (PIL)

## 🤝 The Team
The Object Detection Assistant was built collaboratively by a dedicated team of four developers:
Nimesh Surve
Sahil Pal
Harsh Parab
Vedant Parab

## 📜 License
Distributed under the MIT License. See LICENSE for more information.
