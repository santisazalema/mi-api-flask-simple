import os
from flask import Flask
from dotenv import load_dotenv
from app.models import db

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///tasks.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from app.routes import api
    app.register_blueprint(api)

    with app.app_context():
        db.create_all()

    return app