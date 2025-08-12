# backend/app/routes.py
import json
from flask import Blueprint, request, jsonify, current_app
from app.db import db
from app.models import Insight

api = Blueprint("api", __name__)

def error_response(msg, code=400):
    return jsonify({"error": msg}), code

@api.route("/status", methods=["GET"])
def status():
    return jsonify({"status": "ok", "message": "InsightStream API running"}), 200

@api.route("/insights", methods=["GET"])
def list_insights():
    q = request.args.get("q", "").strip()
    query = Insight.query
    if q:
        query = query.filter(Insight.name.ilike(f"%{q}%"))
    items = query.order_by(Insight.created_at.desc()).all()
    return jsonify([i.to_dict() for i in items]), 200

@api.route("/insights/<int:insight_id>", methods=["GET"])
def get_insight(insight_id):
    i = Insight.query.get(insight_id)
    if not i:
        return error_response("Insight not found", 404)
    return jsonify(i.to_dict()), 200

@api.route("/insights", methods=["POST"])
def create_insight():
    data = request.get_json() or {}
    name = data.get("name")
    if not name:
        return error_response("`name` is required", 400)
    description = data.get("description")
    config = data.get("config")
    if config and not isinstance(config, dict):
        try:
            config = json.loads(config)
        except Exception:
            return error_response("`config` must be a JSON object", 400)
    ins = Insight(name=name, description=description, config=config)
    db.session.add(ins)
    db.session.commit()
    return jsonify(ins.to_dict()), 201

@api.route("/insights/<int:insight_id>", methods=["PUT", "PATCH"])
def update_insight(insight_id):
    ins = Insight.query.get(insight_id)
    if not ins:
        return error_response("Insight not found", 404)
    data = request.get_json() or {}
    name = data.get("name")
    description = data.get("description")
    config = data.get("config")
    if name is not None:
        ins.name = name
    if description is not None:
        ins.description = description
    if config is not None:
        if config and not isinstance(config, dict):
            try:
                config = json.loads(config)
            except Exception:
                return error_response("`config` must be a JSON object", 400)
        ins.config = config
    db.session.commit()
    return jsonify(ins.to_dict()), 200

@api.route("/insights/<int:insight_id>", methods=["DELETE"])
def delete_insight(insight_id):
    ins = Insight.query.get(insight_id)
    if not ins:
        return error_response("Insight not found", 404)
    db.session.delete(ins)
    db.session.commit()
    return jsonify({"deleted": insight_id}), 200