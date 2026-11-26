# HearSee

A multimodal web app that combines **face recognition** and **speech-to-text** in one interface. Built for my Applications of Artificial Intelligence unit (AAI202) at Torrens University Australia.


## What it does

- Streams a live webcam feed and detects faces
- Registers a new person by capturing 20 face images and training a model
- Recognises registered people by name and labels everyone else "Unknown"
- Records speech in the browser and transcribes it to text
- Shows a loading state while the transcript is processed

## How it works

**Face recognition**
1. Enter a name and the webcam captures 20 images of your face.
2. Faces are detected with an OpenCV Haar Cascade.
3. An LBPH (Local Binary Patterns Histograms) recogniser is trained on the images and saved locally.
4. During live video, each detected face is matched against the trained model. A low-confidence match is labelled "Unknown".

**Speech recognition**
1. Start Recording captures microphone audio; Stop Recording ends it.
2. The audio is uploaded to the AssemblyAI API.
3. The transcript is returned and shown in the UI.

## Tech stack

| Area | Tools |
|---|---|
| Frontend | React, Vite, JavaScript, CSS |
| Backend | Python, Flask, Flask-CORS |
| Computer vision | OpenCV (Haar Cascade, LBPH) |
| Speech | AssemblyAI API |
| Other | NumPy, SciPy, SoundDevice |

## Getting started

Prerequisites: Python 3.[x], Node.js [x], a webcam, a microphone, and a free [AssemblyAI](https://www.assemblyai.com/) API key.

```bash
# backend
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # then add your AssemblyAI key
python app.py

# frontend (new terminal)
cd frontend
npm install
npm run dev
```

Open the URL Vite prints (usually http://localhost:5173).

## Project structure

```text
HearSee/
├── backend/    Flask API, face recognition, speech recognition
└── frontend/   React app (Vite)
```

## Limitations

- LBPH is a classical method. It works best with good lighting, a front-facing face and a small number of registered people. It is not a deep-learning recogniser.
- Currently runs locally only. 
- Face images and recordings stay on your machine and are excluded from the repo.

## What I learned

- Connecting a React frontend to a Flask API (CORS, file upload, async state)
- Training and saving a face recognition model with OpenCV
- Calling a third-party speech-to-text API and handling its asynchronous results
- Running involved quite a few steps, would try to simplify

## Next steps

- Use the browser's MediaRecorder so audio capture works when deployed
- Swap LBPH for an embedding-based recogniser
- Add tests and deploy the app

## Author

Afreen Fatima Syeda: [LinkedIn](https://linkedin.com/in/afreenfsyeda)
