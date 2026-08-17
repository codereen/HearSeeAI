from flask import Flask, Response, request, jsonify
from flask_cors import CORS
import cv2

from face_recognition import (
    register_face,
    recognize,
    load_model
)

app = Flask(__name__)
CORS(app)

# Load existing face model if one exists
load_model()


@app.get("/")
def home():
    return {
        "message": "HearSee Backend Running"
    }


def generate_frames():

    camera = cv2.VideoCapture(0)

    while True:

        success, frame = camera.read()

        if not success:
            break

        frame = recognize(frame)

        success, buffer = cv2.imencode(".jpg", frame)

        if not success:
            continue

        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n"
            + buffer.tobytes()
            + b"\r\n"
        )

    camera.release()


@app.get("/video_feed")
def video_feed():

    return Response(
        generate_frames(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )


@app.post("/register")
def register():

    data = request.get_json()

    name = data.get("name", "").strip()

    if not name:

        return jsonify({
            "message": "Please enter a name."
        }), 400

    print(f"Registering {name}...")

    register_face(name)

    load_model()

    return jsonify({
        "message": f"{name} registered successfully!"
    })


if __name__ == "__main__":

    print("Starting HearSee backend...")

    app.run(
        debug=False,
        use_reloader=False
    )