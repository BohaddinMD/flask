from flask import Flask, request

app = Flask(__name__)

latest_frame = None

@app.route("/")
def home():
    return "Flask server running"

@app.route("/live")
def live():
    return "Waiting for video"

@app.route("/upload", methods=["POST"])
def upload():
    global latest_frame
    latest_frame = request.data
    return "Frame received"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
