from flask import Blueprint, request, jsonify
from datetime import datetime
from auth import auth
from rate_limiter import limiter

bp = Blueprint("receive_data", __name__)


@bp.route("/receive_data", methods=["GET", "POST"])
@limiter.limit("5 per minute")
@auth.login_required()
def receive_data_from_esp32():
    if request.method == "POST":
        input_data = request.get_json()
        tracker_id = input_data["tracker_id"]
        lat = input_data["lat"]
        long = input_data["long"]
        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        with open("data.txt", "a") as file:
            file.write(f"{tracker_id} {lat} {long}\n")

        return jsonify({
            "status": {
                "code": 200,
                "message": "Data received and saved successfully"
            },
            "data": {
                "tracker_id": tracker_id,
                "lat": lat,
                "long": long,
                "timestamp": timestamp
            }
        }), 200

    else:
        return jsonify({
            "status": {
                "code": 200,
                "message": "Method not allowed"
            },
            "data": None
        }), 405
