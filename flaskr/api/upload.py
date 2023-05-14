from flask import url_for, request, send_from_directory, flash, redirect
from flask_ckeditor import upload_fail, upload_success
from flask_login import login_required
from werkzeug.utils import secure_filename
import uuid

from config import Config
from . import api
from ..utils.permission_verification import permission_required


@api.route('/files/<path:filename>')
def uploaded_files(filename):
    path = Config.UPLOADED_PATH + 'img/'
    return send_from_directory(path, filename)


@api.route('/upload', methods=['POST'])
@login_required
@permission_required
def upload():
    f = request.files.get('upload')  # 获取上传图片文件对象
    # Add more validations here
    extension = f.filename.split('.')[1].lower()
    if extension not in ['jpg', 'gif', 'png', 'jpeg']:  # 验证文件类型示例
        return upload_fail(message='请上传图片!')  # 返回upload_fail调用
    f.save(Config.UPLOADED_PATH + 'img/' + f.filename)
    url = url_for('api.uploaded_files', filename=f.filename)
    return upload_success(url=url)  # 返回upload_success调用


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in Config.ALLOWED_EXTENSIONS


@api.route('/up_avatar', methods=['GET', 'POST'])
@login_required
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('请选择文件', 'danger')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('请选择文件', 'danger')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            ext = filename.rsplit('.')[1]
            new_filename = str(uuid.uuid4()) + '.' + ext
            path = Config.UPLOADED_PATH + "photo/"
            file.save(path + new_filename)
            return redirect(url_for('users.my_information', filename=new_filename))
        else:
            flash('图片格式不符', 'danger')
    return redirect(url_for('users.my_information'))
