from flask import Blueprint

bp = Blueprint('main',__name__,url_prefix='/')#초기 주소

@bp.route('/main')
def hello_pybo():
    return 'main pybo!!!!!!!!!!'

@bp.route('/')
def index():
    return 'pybo ind111ex'