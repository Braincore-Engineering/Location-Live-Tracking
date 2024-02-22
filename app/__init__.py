import os

from flask import Flask
import app.index as index, app.db as db


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "app.sqlite"),
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    # Registering the blueprints
    app.register_blueprint(index.bp)

    return app
