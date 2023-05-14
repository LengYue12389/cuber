import os


class Config(object):
    """ 配置信息，文件上传的根路径以及数据库连接的uri """
    # 数据用户配置
    DB_USERNAME = 'root'
    DB_PASSWORD = ''
    DB_HOST = 'localhost'
    # 数据库配置
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:3306/registration_system'

    # 使用sqlit 数据库
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///./database.db'
    SECRET_KEY = ''
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = False
    FLASK_ADMIN_SWATCH = 'cerulean'
    # 配置admin中文界面
    BABEL_DEFAULT_LOCALE = 'zh_CN'
    CKEDITOR_FILE_UPLOADER = 'upload'
    UPLOADED_PATH = os.path.join(BASEDIR, 'flaskr/static/media/')
    # 分页配置项
    PER_PAGE = 30
    INDEX_PAGE = 10
    # cookie 设置 过期时间为1天
    REMEMBER_COOKIE_DURATION = 1
    # DNF的时间
    DNF_TIME = 99999
    # 头像上传配置
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'svg'}
