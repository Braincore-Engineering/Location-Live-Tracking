from flask import Blueprint, render_template
from cache import cache


bp = Blueprint("location_live_tracking", __name__,
               url_prefix="/location_live_tracking")


DATA_FILE_PATH = "data.txt"


def read_data_file():
    data = []
    with open(DATA_FILE_PATH, "r") as file:
        next(file)
        for line in file:
            tracker_id, lat, long = line.strip().split()
            data.append({"tracker_id": int(tracker_id),
                        "lat": float(lat), "long": float(long)})
    return data


@bp.route("/")
@cache.cached(timeout=15)
def location_live_tracking():
    data = read_data_file()
    trackers = set(d['tracker_id'] for d in data)
    return render_template("pages/location_live_tracking/index.html", trackers=trackers)


@bp.route("/<int:tracker_id>")
@cache.cached(timeout=15)
def location_live_tracking_tracker(tracker_id):
    data = read_data_file()

    locations = [
        location for location in data if location["tracker_id"] == tracker_id]

    active_trackers = set(location["tracker_id"] for location in data)

    return render_template("pages/location_live_tracking/trackers.html",
                           tracker_id=tracker_id,
                           locations=locations,
                           active_trackers=active_trackers)
