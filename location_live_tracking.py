from flask import Blueprint, render_template
from cache import cache
from database.model.tracker import Tracker
from database.model.location import Location

bp = Blueprint("location_live_tracking", __name__,
               url_prefix="/location_live_tracking")


@bp.route("/")
@cache.cached(timeout=15)
def location_live_tracking():
    trackers = Tracker.query.all()
    return render_template("pages/location_live_tracking/index.html", trackers=trackers)


@bp.route("/<int:tracker_id>")
@cache.cached(timeout=15)
def location_live_tracking_tracker(tracker_id):
    # trackers = Tracker.query.all()
    tracker = Tracker.query.filter_by(id=tracker_id).first()

    data = Location.query.filter(Location.tracker_id == tracker_id).all()
    locations = [location.to_dict() for location in data]
    return render_template(
        "pages/location_live_tracking/trackers.html",
        locations=locations,
        tracker=tracker,
    )
