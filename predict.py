import subprocess

# Define your YOLOv5 command
yolo_command = [
    "yolo", 
    "task=detect", 
    "mode=predict", 
    f"model=/Users/kevindinh/Desktop/ASL/runs/detect/train10/weights/best.pt", 
    "source=1",  # Use 1 for webcam input
    "conf=0.25", 
    "save=True"
]

# Run the YOLOv5 command
subprocess.run(yolo_command)