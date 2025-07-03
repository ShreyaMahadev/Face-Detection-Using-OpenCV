# Face Detection App using OpenCV & Streamlit

A simple web app for detecting faces in images or webcam feed, built with Streamlit and OpenCV. Upload images or use your webcam, detect faces, and download all cropped face images as a ZIP file.

## Features
- Upload one or more images and detect faces in each
- Use your webcam for live face detection
- Cropped faces are saved and can be downloaded as a ZIP
- Easy-to-use web interface

## Requirements
- Python 3.x
- streamlit
- opencv-python
- numpy
- pillow

## Installation
1. Clone or download this repository.
2. Install the required packages:
   ```bash
   pip install streamlit opencv-python numpy pillow
   ```

## Usage
1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Open the provided local URL in your browser.
3. Choose between **Upload Images** or **Use Webcam**.
4. For uploads, select one or more images (JPG, JPEG, PNG).
5. For webcam, turn on the webcam and allow access.
6. Detected faces will be highlighted and cropped.
7. Download all cropped faces as a ZIP file if faces are detected.

## How it works
- Uses OpenCV's Haar Cascade for face detection
- Draws rectangles around detected faces
- Crops and saves each detected face
- Provides a download button for all cropped faces

## License
This project is for educational purposes.
