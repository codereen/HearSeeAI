from flask import Flask, Response, request, jsonify
from flask_cors import CORS
import cv2

from face_recognition import (
    register_face,
    recognize,
    load_model
)

from speech_recognition import (
    start_recording,
    stop_recording
)


app = Flask(__name__)
CORS(app)

load_model()


@app.get("/")
def home():

    return {
        "message": "Backend Running"
    }


def generate_frames():

    camera = cv2.VideoCapture(0)

    while True:

        success, frame = camera.read()

        if not success:
            break

        frame = recognize(frame)

        success, buffer = cv2.imencode(
            ".jpg",
            frame
        )

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

    name = data.get(
        "name",
        ""
    ).strip()

    if not name:

        return jsonify({
            "message": "Please enter a name."
        }), 400

    print(
        f"Registering {name}..."
    )

    register_face(name)

    load_model()

    return jsonify({
        "message":
            f"{name} registered successfully!"
    })


@app.post("/start_recording")
def start_recording_route():

    start_recording()

    return jsonify({
        "status": "recording"
    })


@app.post("/stop_recording")
def stop_recording_route():

    text = stop_recording()

    return jsonify({
        "transcript": text
    })


if __name__ == "__main__":

    print(
        "Starting backend..."
    )

    app.run(
        debug=False,
        use_reloader=False
    )