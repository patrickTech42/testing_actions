from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello from GitHub Actions demo app!"})

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return jsonify({"result": a + b})

if __name__ == "__main__":
    # For local testing only; in production use a proper WSGI server
    app.run(host="0.0.0.0", port=5000, debug=True)
