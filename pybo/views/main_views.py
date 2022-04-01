from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/1234')  # 초기 주소


@bp.route('/main')
def hello_pybo():
    return 'main pybo!!!!!!!!!!'


@bp.route('/1234')
def index():
    return 'pybo ind111ex'
