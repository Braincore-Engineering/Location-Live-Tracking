from flask import Blueprint, jsonify, request
from database.model.tracker import Tracker
from database.mysql import db
from database.model.tracker import Location
from auth import auth
from rate_limiter import limiter

bp = Blueprint("mysql", __name__, url_prefix="/tracker")


@bp.route("/insert/", methods=["POST"])
def insert_data():
    name = request.form.get("name")
    desc = request.form.get("description")

    if not name:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        tracker = Tracker(name=name, description=desc)
        db.session.add(tracker)
        db.session.commit()
        return jsonify({"message": "tracker created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
