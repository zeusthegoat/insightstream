from flask import Flask
from flask_cors import CORS
from .routes import api
from .db import init_db

def create_app():
    app = Flask(__name__)
    CORS(app)
    init_db(app)
    app.register_blueprint(api, url_prefix="/api")
    return app