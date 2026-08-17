# HearSee

A simple multimodal AI application that combines **face recognition** and **speech recognition** in one web-based interface.

HearSee uses a webcam to detect and recognise registered faces while allowing the user to record speech and convert it into text.

---

## Features

- 🎥 Live webcam feed
- 👤 Face detection using OpenCV
- 🧠 Face registration and training
- 🔍 Recognition of previously registered users
- ❓ Detection of unknown faces
- 🎙️ Start and stop voice recording
- 📝 Automatic speech-to-text transcription
- ⏳ Loading state while transcription is processed
- 🌐 React frontend with Flask backend

---

## How It Works

HearSee combines two different AI capabilities:

### Face Recognition

1. The user enters their name.
2. The webcam captures 20 images of their face.
3. The images are saved locally as training data.
4. An LBPH face recognition model is trained using the captured images.
5. The trained model is saved locally.
6. When the webcam is running, registered faces are recognised and their names are displayed.
7. Faces that are not recognised are labelled **Unknown**.

### Speech Recognition

1. The user selects **Start Recording**.
2. The microphone records the user's speech.
3. The user selects **Stop Recording**.
4. The recorded audio is uploaded to AssemblyAI.
5. AssemblyAI converts the speech into text.
6. The transcript is displayed in the application.

---

## Technologies Used

### Frontend

- React
- Vite
- JavaScript
- CSS

### Backend

- Python
- Flask
- Flask-CORS

### AI / Machine Learning

- OpenCV
- Haar Cascade face detection
- LBPH face recognition
- AssemblyAI speech recognition

### Other

- NumPy
- SciPy
- SoundDevice
- Git / GitHub

---

## Project Structure

```text
HearSee/
│
├── backend/
│   ├── app.py
│   ├── face_recognition.py
│   ├── speech_recognition.py
│   ├── haarcascade_frontalface_default.xml
│   ├── dataset/
│   ├── trainer/
│   └── recordings/
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── index.css
│   ├── package.json
│   └── ...
│
├── .gitignore
└── README.md
