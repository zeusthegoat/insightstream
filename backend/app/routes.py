from flask import Blueprint, jsonify
from .models import Event

api = Blueprint("api", __name__)

@api.route("/status", methods=["GET"])
def status():
    return jsonify({"status": "ok", "message": "InsightStream API running"})