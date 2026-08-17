import "./App.css";

function App() {

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
        />

        <div className="buttons">

          <button>
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