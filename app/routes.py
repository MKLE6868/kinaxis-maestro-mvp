from flask import Blueprint, request, jsonify
from .services.planner import generate_recommendations
from .services.anomaly import detect_anomalies
from .services.workflow import trigger_workflow

bp = Blueprint("main", __name__)

@bp.route("/recommend", methods=["POST"])
def recommend():
    data = request.json
    recommendations = generate_recommendations(data)
    return jsonify(recommendations)

@bp.route("/detect-anomaly", methods=["POST"])
def anomaly():
    data = request.json
    result = detect_anomalies(data)
    return jsonify(result)

@bp.route("/trigger-workflow", methods=["POST"])
def workflow():
    data = request.json
    result = trigger_workflow(data)
    return jsonify(result)
