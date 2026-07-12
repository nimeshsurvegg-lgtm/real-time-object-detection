import cv2
import pyttsx3
import threading
import time
import tkinter as tk
from PIL import Image, ImageTk
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")

# Text-to-Speech setup
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Cooldown control
last_spoken = {}
cooldown = 3

# Camera variable
cap = None
running = False

# Speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

def speak_async(text):
    thread = threading.Thread(target=speak, args=(text,))
    thread.daemon = True
    thread.start()

# Start Camera
def start_camera():
    global cap, running

    if running:
        return

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        status_label.config(text="Camera Error")
        return

    running = True
    status_label.config(text="Camera Started")

    update_frame()

# Stop Camera
def stop_camera():
    global running, cap

    running = False

    if cap:
        cap.release()

    video_label.config(image="")
    status_label.config(text="Camera Stopped")

# Frame Update Loop
def update_frame():
    global cap, running

    if not running:
        return

    ret, frame = cap.read()

    if ret:
        results = model(frame)
        detected_objects = set()

        for r in results:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                label = model.names[cls_id]

                detected_objects.add(label)

                # Draw box
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (0,255,0),
                    2
                )

                cv2.putText(
                    frame,
                    label,
                    (x1, y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0,255,0),
                    2
                )

        # Speak detected objects
        current_time = time.time()

        for obj in detected_objects:
            if obj not in last_spoken or \
               current_time - last_spoken[obj] > cooldown:

                speak_async(obj)
                last_spoken[obj] = current_time

        # Convert frame to Tkinter format
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        img = Image.fromarray(frame_rgb)
        img = img.resize((640, 480))

        imgtk = ImageTk.PhotoImage(image=img)

        video_label.imgtk = imgtk
        video_label.configure(image=imgtk)

    # Call again
    video_label.after(10, update_frame)

# GUI Window
root = tk.Tk()
root.title("Object Detection Assistant")
root.geometry("750x600")

# Title
title_label = tk.Label(
    root,
    text="Object Detection Assistant",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=10)

# Video Display
video_label = tk.Label(root)
video_label.pack()

# Buttons Frame
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

start_btn = tk.Button(
    btn_frame,
    text="Start Camera",
    font=("Arial", 12),
    width=15,
    command=start_camera
)
start_btn.grid(row=0, column=0, padx=10)

stop_btn = tk.Button(
    btn_frame,
    text="Stop Camera",
    font=("Arial", 12),
    width=15,
    command=stop_camera
)
stop_btn.grid(row=0, column=1, padx=10)

quit_btn = tk.Button(
    btn_frame,
    text="Quit",
    font=("Arial", 12),
    width=15,
    command=root.destroy
)
quit_btn.grid(row=0, column=2, padx=10)

# Status Label
status_label = tk.Label(
    root,
    text="Camera Stopped",
    font=("Arial", 12)
)
status_label.pack(pady=5)

# Run GUI
root.mainloop()

# Cleanup
if cap:
    cap.release()

cv2.destroyAllWindows()