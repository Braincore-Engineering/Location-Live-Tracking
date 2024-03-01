from flask import Blueprint, jsonify, request
from database.model.tracker import Tracker
from database.mysql import db, format_database_error
from auth import auth
from rate_limiter import limiter

bp = Blueprint("mysql", __name__, url_prefix="/tracker")


@bp.route("/insert/", methods=["POST"])
@limiter.limit("5 per minute")
@auth.login_required()
def insert_data():
    name = request.form.get("name")
    desc = request.form.get("description")

    if not name:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        tracker = Tracker(name=name, description=desc)
        db.session.add(tracker)
        db.session.commit()
        return (
            jsonify(
                {
                    "status": {
                        "code": 201,
                        "message": "tracker created successfully",
                    },
                    "tracker": {"id": tracker.id, "name": name, "description": desc},
                }
            ),
            201,
        )
    except Exception as e:
        db.session.rollback()
        error_msg = format_database_error(e)
        return (
            jsonify(
                {
                    "status": {"code": 500, "message": error_msg},
                    "data": None,
                }
            ),
            500,
        )
