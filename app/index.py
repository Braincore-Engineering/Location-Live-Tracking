import sqlite3
from flask import Blueprint, render_template, request, jsonify
from datetime import datetime
from app.db import get_db

bp = Blueprint("index", __name__, url_prefix="/v1")


@bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        tracker_id = request.form["trackerId"]
        lat = request.form["lat"]
        lon = request.form["long"]
        cur_time = datetime.now()

        if not tracker_id or not lat or not lon:
            return (
                jsonify(
                    {"status": 400, "message": "Your provided data is not complete"}
                ),
                400,
            )

        try:
            db = get_db()
            db.execute(
                "INSERT INTO location (tracker_id, latitude, longitude, timestamp) VALUES (?, ?, ?, ?)",
                (tracker_id, lat, lon, cur_time),
            )
            db.commit()

            return jsonify(
                {
                    "status": 200,
                    "message": "Success",
                    "data": {"lat": lat, "lon": lon, "timestamp": cur_time},
                }
            )
        except sqlite3.Error as e:
            return (
                jsonify(
                    {
                        "status": 500,
                        "message": "Failed to insert data into the database",
                        "error": str(e),
                    }
                ),
                500,
            )
    elif request.method == "GET":
        try:
            db = get_db()
            cursor = db.execute("SELECT * FROM location")
            locations = cursor.fetchall()
            return render_template("index.html", locations=locations)
        except sqlite3.Error as e:
            return (
                jsonify(
                    {
                        "status": 500,
                        "message": "Failed to fetch data from the database",
                        "error": str(e),
                    }
                ),
                500,
            )
        finally:
            db.close()
