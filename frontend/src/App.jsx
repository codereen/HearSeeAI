import "./App.css";
import { useState } from "react";

function App() {

  const [name, setName] = useState("");

  const registerFace = async () => {

    if (!name) {
      alert("Enter your name first.");
      return;
    }

    const response = await fetch(
      "http://127.0.0.1:5000/register",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name,
        }),
      }
    );

    const data = await response.json();

    alert(data.message);

  };

  return (

    <div className="container">

      <div className="camera">

        <img
          src="http://127.0.0.1:5000/video_feed"
          alt="Camera"
        />

      </div>

      <div className="controls">

        <input
          placeholder="Enter your name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />

        <div className="buttons">

          <button onClick={registerFace}>
            Register Face
          </button>

          <button>
            Start Recording
          </button>

        </div>

        <div className="transcript">
          Transcript will appear here.
        </div>

      </div>

    </div>

  );

}

export default App;