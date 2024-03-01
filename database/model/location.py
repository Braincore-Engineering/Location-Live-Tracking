from database.mysql import db
from database.model.tracker import Tracker


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tracker_id = db.Column(db.Integer, db.ForeignKey("tracker.id"), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lon = db.Column(db.Float, nullable=False)

    tracker = db.relationship("Tracker", backref="locations")

    def __init__(self, tracker_id, lat, lon):
        self.tracker_id = tracker_id
        self.lat = lat
        self.lon = lon

    def to_dict(self):
        return {
            "id": self.id,
            "tracker_id": self.tracker_id,
            "lat": self.lat,
            "lon": self.lon,
        }
