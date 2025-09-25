from flask import Flask
from .config import Config
from .db import init_db
from .controllers import register_blueprints

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    init_db(app)
    register_blueprints(app)
    return app
