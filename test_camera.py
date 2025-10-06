import cv2

# Initialize webcam (use 0 for the default camera, 1 for the second camera)
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Error: Could not access the camera.")
else:
    print("Camera is working!")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Display the frame
    cv2.imshow("Camera Preview", frame)

    # Exit if the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()