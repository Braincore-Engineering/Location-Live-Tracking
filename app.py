import os
from flask import Flask
from mqtt_client import init_mqtt
from socket_io import socketio
from config import CONFIG

from index import bp as index_bp
from errors import bp as error_bp
from location_live_tracking import bp as llt_bp
from receive_data import bp as rd_bp
from insert_tracker import bp as db_bp

from cache import init_cache_app
from compress import init_compress_app
from rate_limiter import init_rate_limiter
from database.mysql import init_db, init_db_command, drop_db_command


def create_app():
    app = Flask(__name__)
    app.config.update(CONFIG)

    # Register Blueprint
    app.register_blueprint(index_bp)
    app.register_blueprint(error_bp)
    app.register_blueprint(llt_bp)
    app.register_blueprint(rd_bp)
    app.register_blueprint(db_bp)

    # Initializing
    init_cache_app(app)
    init_compress_app(app)
    # init_rate_limiter(app)
    init_db(app)

    socketio.init_app(app, cors_allowed_origins="*")

    init_mqtt(app)
    # CLI Command
    app.cli.add_command(init_db_command)
    app.cli.add_command(drop_db_command)

    return app


if __name__ == "__main__":
    app = create_app()
    socketio.run(
        app, debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 10600))
    )
