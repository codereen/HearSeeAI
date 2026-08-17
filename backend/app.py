from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.get("/")
def home():
    return {
        "message": "HearSee Backend Running"
    }


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)