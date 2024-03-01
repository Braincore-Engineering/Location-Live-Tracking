from flask import Flask
from config import CONFIG

from index import bp as index_bp
from crud import bp as crud_bp

from errors import bp as error_bp
from location_live_tracking import bp as llt_bp
from receive_data import bp as rd_bp

from cache import init_cache_app
from compress import init_compress_app
from rate_limiter import init_rate_limiter


def create_app():
    app = Flask(__name__)
    app.config.update(CONFIG)

    app.register_blueprint(index_bp)
    app.register_blueprint(crud_bp)

    app.register_blueprint(error_bp)
    app.register_blueprint(llt_bp)
    app.register_blueprint(rd_bp)

    init_cache_app(app)
    init_compress_app(app)
    init_rate_limiter(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
