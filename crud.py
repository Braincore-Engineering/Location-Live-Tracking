from flask import Blueprint, render_template
from rate_limiter import limiter
from cache import cache
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Tracker  # Assuming you have a Tracker model defined in models.py

bp = Blueprint("crud", __name__, url_prefix="/crud")

DATABASE_URL = "sqlite:///data.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def read_data_file():
    session = Session()
    data = session.query(Tracker).all()
    session.close()
    return [{"tracker_id": tracker.tracker_id, "lat": tracker.lat, "long": tracker.long} for tracker in data]

@bp.route("/")
@cache.cached(timeout=15)
def location_live_tracking():
    data = read_data_file()
    trackers = set(d['tracker_id'] for d in data)
    return render_template("pages/location_live_tracking/crud.html", trackers=trackers)

