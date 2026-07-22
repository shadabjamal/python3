# '/app/v1/details'
# '/app/v1/healthz'
from flask import Flask, jsonify
from datetime import datetime, timezone
import socket

app = Flask(__name__)

@app.route("/app/v1/details")
def details():
    return jsonify({"time": datetime.now(timezone.utc).isoformat(), "hostname": socket.gethostname(), "message": "Application details Hello.!!"}), 200

@app.route("/app/v1/healthz")
def healthz():
    return jsonify({"message": "Application is healthy"}),200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)