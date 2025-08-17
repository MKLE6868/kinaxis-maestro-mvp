def detect_anomalies(data):
    # Placeholder for anomaly detection logic
    # Replace with ML-based detection in production
    anomalies = []
    if data.get("value", 0) > 1000:
        anomalies.append("Unusually high value detected")
    return {"anomalies": anomalies}