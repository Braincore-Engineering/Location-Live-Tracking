from flask import Blueprint, render_template

bp = Blueprint("location_live_tracking", __name__,
               url_prefix="/location_live_tracking")

# Define the path to your data.txt file
DATA_FILE_PATH = "data.txt"


def read_data_file():
    data = []
    with open(DATA_FILE_PATH, "r") as file:
        next(file)  # Skip the header row
        for line in file:
            tracker_id, lat, long = line.strip().split()
            data.append({"tracker_id": int(tracker_id),
                        "lat": float(lat), "long": float(long)})
    return data


@bp.route("/")
def location_live_tracking():
    # Read the data from the file
    data = read_data_file()
    # Extract unique tracker IDs from the data
    trackers = set(d['tracker_id'] for d in data)
    return render_template("pages/location_live_tracking/index.html", trackers=trackers)


@bp.route("/<int:tracker_id>")
def location_live_tracking_tracker(tracker_id):
    # Read the data from the file
    data = read_data_file()

    # Filter locations for the specified tracker ID
    locations = [
        location for location in data if location["tracker_id"] == tracker_id]

    # Extract active trackers
    active_trackers = set(location["tracker_id"] for location in data)

    # Pass the data to the template
    return render_template("pages/location_live_tracking/trackers.html",
                           tracker_id=tracker_id, locations=locations, active_trackers=active_trackers)
