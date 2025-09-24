from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)

# Load models
models_path = os.path.join(os.getcwd(), "models")

cpu_model = joblib.load(os.path.join(models_path, "cpu_isoforest.pkl"))
network_model = joblib.load(os.path.join(models_path, "network_model.pkl"))
login_model = joblib.load(os.path.join(models_path, "login_model.pkl"))
storage_model = joblib.load(os.path.join(models_path, "storage_model.pkl"))

# Content model is a tuple (vectorizer, classifier)
content_vec, content_clf = joblib.load(os.path.join(models_path, "content_model.pkl"))

@app.route("/")
def home():
    return "Helios EC2 Agent Alive"
# CPU anomaly detection
@app.route("/predict/cpu", methods=["POST"])
def predict_cpu():
    data = request.json.get("value", 0)
    prediction = cpu_model.predict([[data]])[0]
    return jsonify({"cpu_value": data, "anomaly": int(prediction == -1)})

# Network anomaly detection
@app.route("/predict/network", methods=["POST"])
def predict_network():
    data = request.json.get("value", 0)
    prediction = network_model.predict([[data]])[0]
    return jsonify({"network_value": data, "anomaly": int(prediction == -1)})

# Login anomaly detection
@app.route("/predict/login", methods=["POST"])
def predict_login():
    data = request.json.get("value", [0, 0])  # [failed_attempts, time_of_day]
    prediction = login_model.predict([data])[0]
    return jsonify({"login_attempts": data, "anomaly": int(prediction == 1)})

# Content injection detection
@app.route("/predict/content", methods=["POST"])
def predict_content():
    text = request.json.get("text", "")
    X = content_vec.transform([text])
    prediction = content_clf.predict(X)[0]
    return jsonify({"text": text, "blocked": int(prediction == 1)})

# Storage anomaly detection
@app.route("/predict/storage", methods=["POST"])
def predict_storage():
    data = request.json.get("value", 0)
    prediction = storage_model.predict([[data]])[0]
    return jsonify({"storage_value": data, "anomaly": int(prediction == -1)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
