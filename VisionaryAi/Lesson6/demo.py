import cv2

# Load the pre-trained Haar Cascade Classifier for face detection

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start video capture from the default webcam (0)

cap = cv2.VideoCapture(0)

while True:

# Read a frame from the webcam
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture image")
        break

# Convert the frame to grayscale for face detection

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Detect faces in the grayscale frame

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Draw rectangles around detected faces

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the frame with detected faces

        cv2.imshow('Face Detection', frame)

# Break the loop if 'q' is pressed

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the video capture object and close all OpenCV windows

cap.release()

cv2.destroyAllWindows()