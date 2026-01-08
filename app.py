from flask import Flask, request, jsonify, render_template
import time

app = Flask(__name__)

# Store latest sensor values
latest_data = {
    "ax": 0.0,
    "ay": 0.0,
    "az": 0.0,
    "time": time.time()
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/update", methods=["POST"])
def update():
    global latest_data
    data = request.json

    latest_data["ax"] = data.get("ax", 0.0)
    latest_data["ay"] = data.get("ay", 0.0)
    latest_data["az"] = data.get("az", 0.0)
    latest_data["time"] = time.time()

    return jsonify({"status": "ok"})

@app.route("/data")
def data():
    return jsonify(latest_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
