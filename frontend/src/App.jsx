import "./App.css";

function App() {

  return (

    <div className="container">

      <div className="camera">

        <h2>Camera Feed</h2>

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