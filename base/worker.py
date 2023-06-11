import cv2
import os

# Create a cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Create a VideoCapture object to capture video from the default camera
video_capture = cv2.VideoCapture(0)

# Create a directory to save the face data
data_dir = "C:/Users/Ifzen/Desktop/base/database"
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Input name and ID
name = input("Enter your name: ")
id = input("Enter your ID: ")

# Capture and process frames from the video stream
while True:
    # Read the frame from the video stream
    ret, frame = video_capture.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Iterate over each detected face
    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Save the face data to a file
        face_data = gray[y:y+h, x:x+w]
        file_name = os.path.join(data_dir, f"{name}_{id}.jpg")
        cv2.imwrite(file_name, face_data)

    # Display the resulting frame
    cv2.imshow("Face Detection", frame)

    # Check for key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close all windows
video_capture.release()
cv2.destroyAllWindows()
