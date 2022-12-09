from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .api import create_blueprint as create_api_blueprint
from .dev import create_blueprint as create_dev_blueprint
from .general import create_blueprint as create_general_blueprint
from .db import db


def create_app() -> Flask:
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

    SQLAlchemy.init_app(db, app)

    app.register_blueprint(create_general_blueprint())
    app.register_blueprint(create_api_blueprint())
    app.register_blueprint(create_dev_blueprint())

    return app

app = create_app()
