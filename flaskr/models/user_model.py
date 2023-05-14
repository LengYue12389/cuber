from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from flaskr.extensions import db
from flaskr.utils import constants
from .ach_model import AchievementCuber333, AchievementCuber222, AchievementCuberOh, AchievementCuberSk, \
    AchievementCuberPy
from .match_model import CompetitionInformation, Info


class User(db.Model, UserMixin):
    """用户信息表"""
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    hash_password = db.Column(db.String(512), unique=False, nullable=False)
    name = db.Column(db.String(20), unique=False, nullable=False)
    birthday = db.Column(db.Date)
    sex = db.Column(db.String(16))
    # 是否有效，无效用户将不能登录系统
    status = db.Column(db.Integer, default=constants.UserStatus.USER_ACTIVE.value)
    # 是否是超级管理员，管理员可以对所有内容进行管理
    is_super = db.Column(db.Integer, default=constants.UserRole.COMMON.value)
    # 创建时间
    created_at = db.Column(db.DateTime, default=datetime.now)
    user_profile = db.relationship('UserProfile', backref='profile', uselist=False)

    @property
    def password(self):
        raise AttributeError('password cannot be read')

    @password.setter
    def password(self, password):
        self.hash_password = generate_password_hash(password)

    def confirm_password(self, password):
        return check_password_hash(self.hash_password, password)

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return f'<{self.id}, {self.name}, {self.sex}, {self.birthday}>'

    # 最后修改的时间

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        """ 有效的用户才能登录系统 """
        return self.status == constants.UserStatus.USER_ACTIVE.value

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return '{}'.format(self.id)

    @property
    def cuber_333_best(self):
        return self.cuber_333.filter(AchievementCuber333.best.isnot(None)).order_by(AchievementCuber333.best).first()

    @property
    def cuber_333_ao5(self):
        return self.cuber_333.filter(AchievementCuber333.ao5.isnot(None)).order_by(AchievementCuber333.ao5).first()

    @property
    def cuber_222_best(self):
        return self.cuber_222.filter(AchievementCuber222.best.isnot(None)).order_by(AchievementCuber222.best).first()

    @property
    def cuber_222_ao5(self):
        return self.cuber_222.filter(AchievementCuber222.best.isnot(None)).order_by(AchievementCuber222.best).first()

    @property
    def cuber_oh_best(self):
        return self.cuber_oh.filter(AchievementCuberOh.best.isnot(None)).order_by(AchievementCuberOh.best).first()

    @property
    def cuber_oh_ao5(self):
        return self.cuber_oh.filter(AchievementCuberOh.best.isnot(None)).order_by(AchievementCuberOh.best).first()

    @property
    def cuber_py_best(self):
        return self.cuber_py.filter(AchievementCuberPy.best.isnot(None)).order_by(AchievementCuberPy.best).first()

    @property
    def cuber_py_ao5(self):
        return self.cuber_py.filter(AchievementCuberPy.best.isnot(None)).order_by(AchievementCuberPy.best).first()

    @property
    def cuber_sk_best(self):
        return self.cuber_sk.filter(AchievementCuberSk.best.isnot(None)).order_by(AchievementCuberSk.best).first()

    @property
    def cuber_sk_ao5(self):
        return self.cuber_sk.filter(AchievementCuberSk.best.isnot(None)).order_by(AchievementCuberSk.best).first()

    @property
    def get_user_avatar(self):
        return self.user_profile

    @property
    def get_user_confidentiality(self):
        return self.user_confidentiality.first()

    @property
    def cuber_333_all(self):
        results = db.session.query(CompetitionInformation.match_name,
                                   CompetitionInformation.id,
                                   AchievementCuber333).join(Info).join(AchievementCuber333).filter(
            self.id == AchievementCuber333.user_id).order_by(CompetitionInformation.match_time.desc()).all()
        return results

    @property
    def cuber_222_all(self):
        results = db.session.query(CompetitionInformation.match_name,
                                   CompetitionInformation.id,
                                   AchievementCuber222).join(Info).join(AchievementCuber222).filter(
            self.id == AchievementCuber222.user_id).order_by(CompetitionInformation.match_time.desc()).all()
        return results

    @property
    def cuber_oh_all(self):
        results = db.session.query(CompetitionInformation.match_name,
                                   CompetitionInformation.id,
                                   AchievementCuberOh).join(Info).join(AchievementCuberOh).filter(
            self.id == AchievementCuberOh.user_id).order_by(CompetitionInformation.match_time.desc()).all()
        return results

    @property
    def cuber_py_all(self):
        results = db.session.query(CompetitionInformation.match_name,
                                   CompetitionInformation.id,
                                   AchievementCuberPy).join(Info).join(AchievementCuberPy).filter(
            self.id == AchievementCuberPy.user_id).order_by(CompetitionInformation.match_time.desc()).all()
        return results

    @property
    def cuber_sk_all(self):
        results = db.session.query(CompetitionInformation.match_name,
                                   CompetitionInformation.id,
                                   AchievementCuberSk).join(Info).join(AchievementCuberSk).filter(
            self.id == AchievementCuberSk.user_id).order_by(CompetitionInformation.match_time.desc()).all()
        return results

    # @property
    # def get_competition_all(self):
    #     results = db.session.query(CompetitionInformation.match_name, CompetitionInformation.id).join(Info)\
    #
    #     return result


class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    avatar = db.Column(db.String(256))


class UserLoginHistory(db.Model):
    __tablename__ = 'user_login_history'
    id = db.Column(db.Integer, primary_key=True)  # 主键
    # 用户名，用于登录
    username = db.Column(db.String(64), nullable=False)
    # IP地址
    ip = db.Column(db.String(32))
    # user-agent
    ua = db.Column(db.String(512))
    # 创建时间
    created_at = db.Column(db.DateTime, default=datetime.now)
    # 关联用户
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # 建立与用户的一对多属性,user.history_list
    user = db.relationship('User', backref=db.backref('history_list', lazy='dynamic'))


class UserConfidentiality(db.Model):
    __tablename__ = 'user_confidentiality'
    id = db.Column(db.Integer, primary_key=True)
    confidentiality_question = db.Column(db.Text)
    confidentiality_answer = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('user_confidentiality', lazy='dynamic'))


class OderInfo(db.Model):
    """用户报名缴费订单表"""
    __tablename__ = 'oder_info'
    id = db.Column(db.Integer, primary_key=True)
    # 订单号
    oder_id = db.Column(db.Integer)
    add_time = db.Column(db.DateTime, unique=True)
    # 金额
    amount = db.Column(db.String(10))
    match_id = db.Column(db.Integer, db.ForeignKey('competition_information.id'))
    user = db.relationship('User', backref=db.backref('user_oder_info', lazy='dynamic'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
