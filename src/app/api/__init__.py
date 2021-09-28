from flask import Blueprint


def create_blueprint() -> Blueprint:
    bp = Blueprint('api', __name__)

    @bp.route('/foo')
    def test_route():
        return 'bar'

    return bp

blueprint = create_blueprint()
