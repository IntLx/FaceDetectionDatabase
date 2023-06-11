# FaceDetectionDatabase
Dont forget to make a folder  called "database" inside the "base" folder
go to cmd and type pip install opencv-python after installing enjooy
It utilizes the Haar cascade classifier, which is a machine learning-based approach for object detection. Specifically, it uses a pre-trained model called "haarcascade_frontalface_default.xml" to detect faces in a video stream.

Here's how the script works:

It imports the necessary libraries, including OpenCV (cv2) for computer vision tasks.

A cascade classifier object (face_cascade) is created using the "haarcascade_frontalface_default.xml" file. This classifier is trained to detect frontal faces in images.

A VideoCapture object (video_capture) is created to capture frames from the default camera (index 0).

The script prompts the user to enter their name and ID. These inputs are used to save the face data associated with each person.

The script enters a while loop to continuously read frames from the video stream until interrupted.

Within the loop, it reads a frame from the video stream using the VideoCapture object.

The frame is converted to grayscale, which simplifies the face detection process.

The detectMultiScale function is used to detect faces in the grayscale frame. It returns an array of rectangles representing the coordinates of the detected faces.

The script iterates over each detected face, draws a rectangle around it, and saves the face data as an image file. The face data is extracted from the grayscale frame using the coordinates of the face rectangle.

The resulting frame, with the detected faces and rectangles, is displayed on the screen.

The script checks for a key press, specifically the 'q' key, to exit the while loop.

After exiting the loop, the VideoCapture object is released and all windows created by OpenCV are closed.

To summarize, the script captures frames from the video stream, detects faces using the Haar cascade classifier, draws rectangles around the detected faces, and saves the face data as images. This process continues until the user interrupts the script.
