from flask import Flask
from .config import Config
from .db import init_db
from .controllers import register_controllers


def create_app():
    """
    Flask application factory.
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize database
    init_db(app)

    # Register controllers (blueprints + hospital routes)
    register_controllers(app)

    return app
