from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

# Dummy inference: calculates severity score based on input numbers
@app.route('/api/reliefx/infer', methods=['POST'])
def infer():
    payload = request.json
    incident_id = payload.get("incident_id", "UNKNOWN")
    data = payload.get("data", [])

    if not data:
        return jsonify({"error": "No data provided"}), 400

    # Dummy "model" – severity is average of values normalized between 0 and 1
    arr = np.array(data, dtype=float)
    severity = float(np.mean(arr) / 100.0)  # assume values are 0–100

    # Pick top-3 "priority zones"
    priority_zones = [{"zone": i, "score": float(val / 100.0)} for i, val in enumerate(arr[:3])]

    return jsonify({
        "incident_id": incident_id,
        "severity": severity,
        "priority_zones": priority_zones,
        "message": f"Inference complete for {incident_id}"
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
