import streamlit as st
import cv2
import numpy as np
import os
import shutil
import zipfile
from PIL import Image
import tempfile

# Create directory to store faces
FACES_DIR = "detected_faces"
if os.path.exists(FACES_DIR):
    shutil.rmtree(FACES_DIR)
os.makedirs(FACES_DIR, exist_ok=True)

# Load Haar cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

st.set_page_config(page_title="Face Detection App", layout="centered")
st.title("👁️‍🗨️ Face Detection App")
st.markdown("Choose between **Webcam** or **Image Upload**, detect faces, and **download cropped face images.**")

# Option selection
option = st.radio("Select Input Source", ("Upload Images", "Use Webcam"))

face_counter = 0

# ──────────────────────────────────────────────
# 📂 UPLOAD MULTIPLE IMAGES
# ──────────────────────────────────────────────
if option == "Upload Images":
    uploaded_files = st.file_uploader("Upload image(s)", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

    if uploaded_files:
        for idx, uploaded_file in enumerate(uploaded_files):
            st.markdown(f"### 🖼️ {uploaded_file.name}")

            image = Image.open(uploaded_file).convert('RGB')
            img_array = np.array(image)
            gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)

            faces = face_cascade.detectMultiScale(gray, 1.1, 5)

            for i, (x, y, w, h) in enumerate(faces):
                face_counter += 1
                cv2.rectangle(img_array, (x, y), (x + w, y + h), (0, 255, 0), 2)

                face_img = img_array[y:y + h, x:x + w]
                face_path = os.path.join(FACES_DIR, f"{uploaded_file.name.replace('.', '_')}_face_{i + 1}.jpg")
                cv2.imwrite(face_path, cv2.cvtColor(face_img, cv2.COLOR_RGB2BGR))

            st.image(img_array, caption=f"{len(faces)} face(s) detected", use_column_width=True)

# ──────────────────────────────────────────────
# 📸 LIVE WEBCAM DETECTION
# ──────────────────────────────────────────────
elif option == "Use Webcam":
    run_webcam = st.checkbox("Turn ON Webcam")

    if run_webcam:
        FRAME_WINDOW = st.image([])
        cap = cv2.VideoCapture(0)

        while run_webcam:
            ret, frame = cap.read()
            if not ret:
                st.warning("⚠️ Could not access the webcam.")
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 5)

            for i, (x, y, w, h) in enumerate(faces):
                face_counter += 1
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                face_img = frame[y:y + h, x:x + w]
                face_path = os.path.join(FACES_DIR, f"webcam_face_{face_counter}.jpg")
                cv2.imwrite(face_path, face_img)

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            FRAME_WINDOW.image(frame)

        cap.release()

# ──────────────────────────────────────────────
# 📦 DOWNLOAD CROPPED FACE IMAGES (if any)
# ──────────────────────────────────────────────
if face_counter > 0:
    zip_filename = "cropped_faces.zip"
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for file in os.listdir(FACES_DIR):
            zipf.write(os.path.join(FACES_DIR, file), arcname=file)

    st.success(f"✅ Total Faces Detected: {face_counter}")
    with open(zip_filename, "rb") as f:
        st.download_button("📥 Download All Cropped Faces", f, file_name=zip_filename, mime="application/zip")
else:
    st.info("👆 Upload images or turn on webcam to begin detecting faces.")
