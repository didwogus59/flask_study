from flask import Flask, render_template, request, Blueprint

from werkzeug.utils import secure_filename

bp = Blueprint('main',__name__,url_prefix='/')#초기 주소

@bp.route('/hello')
def hello():
    return "hello"

@bp.route('/upload')
def upload_file():
    return render_template('upload.html')

@bp.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'