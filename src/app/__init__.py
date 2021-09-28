from flask import Flask

from .api import create_blueprint as create_api_blueprint


def create_app() -> Flask:
    app = Flask(__name__)

    app.register_blueprint(create_api_blueprint())

    return app

app = create_app()
