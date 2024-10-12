import json
from paho.mqtt.client import Client

from database.model.location import Location
from database.mysql import db
from socket_io import socketio

mqtt_client = Client()


def validate_message(payload):
    """Validate the incoming MQTT message."""
    required_fields = ["tracker_id", "lat", "lon", "timestamp"]

    # Check if all required fields are present
    for field in required_fields:
        if field not in payload:
            print(f"Missing field: {field}")
            return False

    # Additional type checks
    if not isinstance(payload["tracker_id"], (float, int)):
        print("Invalid type for tracker_id. Expected a string.")
        return False
    if not isinstance(payload["lat"], (float, int)):
        print("Invalid type for lat. Expected a float or int.")
        return False
    if not isinstance(payload["lon"], (float, int)):
        print("Invalid type for lon. Expected a float or int.")
        return False
    if not isinstance(
        payload["timestamp"], str
    ):  # Assuming timestamp is a string (ISO format)
        print("Invalid type for timestamp. Expected a string.")
        return False

    return True


def init_mqtt(app):
    def on_message(client, userdata, message):
        try:
            # Parse the JSON payload
            payload = json.loads(message.payload.decode())
            print(payload)

            # Validate the message
            if not validate_message(payload):
                print("Message validation failed.")
                return

            tracker_data = {
                "tracker_id": payload["tracker_id"],
                "lat": payload["lat"],
                "lon": payload["lon"],
                "timestamp": payload["timestamp"],
            }

            with app.app_context():  # Create application context here
                tracker_data_db = Location(**tracker_data)
                db.session.add(tracker_data_db)
                db.session.commit()

                print(f"Received and emitted data: {tracker_data}")

                # Load all locations and emit to web socket so the UI will be updated
                all_locations = (
                    Location.query.filter_by(tracker_id=tracker_data["tracker_id"])
                    .order_by(Location.timestamp.asc())
                    .all()
                )

                locations_data = [
                    {
                        "lat": loc.lat,
                        "lon": loc.lon,
                        "timestamp": loc.timestamp.isoformat(),
                    }
                    for loc in all_locations
                ]
                socketio.emit("new_broadcast", locations_data)

        except Exception as e:
            print(f"Error processing message: {e}")

    mqtt_client.on_message = on_message
    mqtt_client.connect("broker.emqx.io", 1883)
    mqtt_client.subscribe("braincore/live-location")
    mqtt_client.loop_start()
