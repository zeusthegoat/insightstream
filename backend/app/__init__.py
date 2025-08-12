# backend/app/__init__.py
from flask import Flask
from .config import Config
from .db import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions first
    db.init_app(app)

    # Import models and create tables (safe to call; alembic recommended later)
    with app.app_context():
        # Import models so SQLAlchemy knows about them
        from . import models  # noqa: F401
        db.create_all()

    # Import and register blueprints AFTER db.init_app() and models are known
    from .routes import api
    app.register_blueprint(api, url_prefix="/api")

    return app