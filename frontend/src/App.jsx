import { useState } from "react";
import "./App.css";

function App() {

  const [name, setName] = useState("");
  const [recording, setRecording] = useState(false);
  const [loading, setLoading] = useState(false);
  const [transcript, setTranscript] = useState("");

  const registerFace = async () => {

    if (!name.trim()) {
      alert("Enter your name first.");
      return;
    }

    const response = await fetch(
      "http://127.0.0.1:5000/register",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          name: name
        })
      }
    );

    const data = await response.json();

    alert(data.message);
  };


  const startRecording = async () => {

    setTranscript("");

    await fetch(
      "http://127.0.0.1:5000/start_recording",
      {
        method: "POST"
      }
    );

    setRecording(true);
  };


  const stopRecording = async () => {

    setRecording(false);
    setLoading(true);

    const response = await fetch(
      "http://127.0.0.1:5000/stop_recording",
      {
        method: "POST"
      }
    );

    const data = await response.json();

    setTranscript(
      data.transcript || "No speech detected."
    );

    setLoading(false);
  };


  return (

    <div className="container">

      <div className="camera">

        <img
          src="http://127.0.0.1:5000/video_feed"
          alt="Live webcam"
        />

      </div>


      <div className="controls">

        <div className="registration">

          <input
            type="text"
            placeholder="Enter your name"
            value={name}
            onChange={(event) =>
              setName(event.target.value)
            }
          />

          <button onClick={registerFace}>
            Register Face
          </button>

        </div>


        {!recording ? (

          <button
            className="record-button"
            onClick={startRecording}
            disabled={loading}
          >
            Start Recording
          </button>

        ) : (

          <button
            className="record-button recording"
            onClick={stopRecording}
          >
            Stop Recording
          </button>

        )}


        <div className="transcript">

          {loading ? (
            <span>Loading...</span>
          ) : transcript ? (
            transcript
          ) : (
            <span className="placeholder">
              Your transcript will appear here.
            </span>
          )}

        </div>

      </div>

    </div>
  );
}

export default App;