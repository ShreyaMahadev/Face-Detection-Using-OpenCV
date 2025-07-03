# Face Detection using OpenCV

This project demonstrates real-time face detection using OpenCV and a webcam. It uses Haar Cascade classifiers to detect faces in video frames captured from your computer's default camera.

## Features
- Real-time face detection using your webcam
- Draws rectangles around detected faces
- Simple and easy-to-understand code

## Requirements
- Python 3.x
- OpenCV (`opencv-python`)

## Installation
1. Clone or download this repository.
2. Install the required Python package:
   ```bash
   pip install opencv-python
   ```

## Usage
1. Make sure your webcam is connected.
2. Run the script:
   ```bash
   python face_detection.py
   ```
3. A window will open showing the webcam feed with rectangles drawn around detected faces.
4. Press `q` to quit the application.

## How it works
- Loads the Haar Cascade classifier for face detection.
- Captures video from the default webcam.
- Converts each frame to grayscale and detects faces.
- Draws a green rectangle around each detected face.
- Displays the video feed in a window.

## Troubleshooting
- If you see "Error: Could not open webcam.", ensure your webcam is connected and not being used by another application.
- If you have issues with the Haar Cascade file, make sure OpenCV is installed correctly.

## License
This project is for educational purposes.
