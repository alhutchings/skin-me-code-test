from flask import Flask, Blueprint


def create_app() -> Flask:
    app = Flask(__name__)

    bp = Blueprint('api', __name__)

    @bp.route('/test')
    def test_route():
        return "test"

    app.register_blueprint(bp)

    return app

app = create_app()
