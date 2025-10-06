import cv2
from yolov5 import load  # Import the correct function

# Load your trained YOLOv5 model
model = load("/Users/kevindinh/Desktop/ASL/runs/detect/train10/weights/best.pt")

# Open a video capture object
cap = cv2.VideoCapture(1)  # Use 0 for default camera, or 1 for another connected camera

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture image.")
        break

    # Make predictions
    results = model(frame)

    # Render predictions on the frame
    frame_with_results = results.render()[0]  # Get the frame with bounding boxes and labels

    # Display the frame with the predictions
    cv2.imshow("Webcam YOLOv5 Inference", frame_with_results)

    # Press 'q' to quit the webcam preview
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()