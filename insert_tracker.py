from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from database.model.tracker import Tracker
from database.mysql import db, format_database_error
from form.form_insert import InsertTrackerForm

bp = Blueprint("mysql", __name__, url_prefix="/tracker")


@bp.route("/insert/", methods=["POST", "GET"])
def insert_data():
    form = InsertTrackerForm()

    if form.validate_on_submit():
        name = form.name.data
        desc = form.name.description

        tracker = Tracker(name=name, description=desc)
        db.session.add(tracker)
        db.session.commit()

        return redirect(url_for("location_live_tracking.location_live_tracking"))
    return render_template(
        "pages/location_live_tracking/insert_tracker.html", form=form
    )


@bp.route("/api/insert/", methods=["POST"])
def insert_data_api():
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