from flask_admin import Admin
from flask_babelex import Babel
from flask_ckeditor import CKEditor
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flaskr.admin import admin_views
from config import Config

db = SQLAlchemy()
ckeditor = CKEditor()
babel = Babel()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message = '请登录'
login_manager.login_message_category = 'danger'
admin = Admin(name='后台管理', index_view=admin_views.MyAdminIndexView(name='主界面'), template_mode='bootstrap3')


@login_manager.user_loader
def load_user(user_id):
    from flaskr.models.user_model import User
    return User.query.get(user_id)


def init_extensions(app):
    login_manager.init_app(app)
    admin.init_app(app)
    db.init_app(app)
    ckeditor.init_app(app)
    babel.init_app(app)

    with app.app_context():
        from flaskr.models.match_model import Info
        from flaskr.models.match_model import CompetitionInformation
        from flaskr.models.home_model import Banner
        from flaskr.models.home_model import IndexArticle
        from flaskr.models.ach_model import AchievementCuber333
        from flaskr.models.ach_model import AchievementCuber222
        from flaskr.models.ach_model import AchievementCuberOh
        from flaskr.models.ach_model import AchievementCuberSk
        from flaskr.models.ach_model import AchievementCuberPy
        from flaskr.models.user_model import User
        from flaskr.models.user_model import UserLoginHistory
        from flaskr.models.user_model import UserProfile
        from flaskr.models.user_model import OderInfo
        admin.add_view(admin_views.InfoAdmin(Info, db.session, name='报名信息'))
        admin.add_view(admin_views.CompetitionInformationAdmin(CompetitionInformation, db.session, name='赛事信息'))
        admin.add_view(admin_views.BannerAdmin(Banner, db.session, name='轮播图', category='首页信息'))
        admin.add_view(admin_views.IndexArticleAdmin(IndexArticle, db.session, name='首页文章', category='首页信息'))
        admin.add_view(admin_views.AchievementCuber333Admin(AchievementCuber333, db.session, name='三阶', category='成绩'))
        admin.add_view(admin_views.AchievementCuber222Admin(AchievementCuber222, db.session, name='二阶', category='成绩'))
        admin.add_view(admin_views.AchievementCuberOhAdmin(AchievementCuberOh, db.session, name='单手', category='成绩'))
        admin.add_view(admin_views.AchievementCuberSkAdmin(AchievementCuberSk, db.session, name='斜转', category='成绩'))
        admin.add_view(admin_views.AchievementCuberPyAdmin(AchievementCuberPy, db.session, name='金字塔', category='成绩'))
        admin.add_view(admin_views.UserAdmin(User, db.session, name='用户信息', category='用户管理'))
        admin.add_view(admin_views.UserLoginHistoryAdmin(UserLoginHistory, db.session, name='登录信息', category='用户管理'))
        admin.add_view(admin_views.UserProfileAdmin(UserProfile, db.session, name='用户头像', category='用户管理'))
        admin.add_view(admin_views.OderInfoAdmin(OderInfo, db.session, name='订单信息', category='用户管理'))
        admin.add_view(admin_views.MyFileAdmin(Config.UPLOADED_PATH, '/static/', name='文件管理', ))
        admin.add_view(admin_views.MyView(name='退出'))
