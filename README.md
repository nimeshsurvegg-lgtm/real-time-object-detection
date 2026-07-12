# Real-Time Object Detection Assistant 👁️🔊

An intelligent, real-time object detection system designed to assist visually impaired individuals and enhance security systems. This application uses a webcam to identify multiple objects in its field of view, displays them with bounding boxes, and communicates the detections through voice feedback.

## 🚀 Features

* **Real-Time Detection:** Utilizes the YOLOv8 deep learning model for fast and accurate object recognition.
* **Audio Feedback:** Integrated Text-to-Speech (TTS) reads out detected objects.
* **Smart Cooldown System:** Prevents audio overlap and repetition overload by implementing a cooldown timer for spoken labels.
* **Visual Tracking:** Draws bounding boxes and labels directly on the video feed.
* **User-Friendly GUI:** Built with Tkinter, featuring a simple interface to start and stop the camera feed easily.
* **Asynchronous Processing:** Voice feedback runs on a separate thread to ensure the video feed remains smooth and lag-free.

## 🎯 Problem Statement

The goal of this project is to develop an assistive and interactive application that enhances accessibility and situational awareness using computer vision and speech technology. The system must accurately detect objects, provide visual cues, output non-intrusive voice feedback, and operate via a smooth, accessible user interface.

## 🛠️ Tech Stack

* **Language:** Python
* **Computer Vision:** OpenCV (`cv2`)
* **Deep Learning Model:** YOLOv8 (`ultralytics`)
* **GUI:** Tkinter & Pillow (`PIL`)
* **Text-to-Speech:** `pyttsx3`

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git](https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git)
   cd YOUR-REPOSITORY-NAME
