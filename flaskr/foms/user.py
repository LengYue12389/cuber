from flask import request
from flask_login import login_user
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FileField
from wtforms.validators import DataRequired
from flaskr.extensions import db
from flaskr.models.user_model import UserLoginHistory, User, UserConfidentiality
from flaskr.utils import constants
from flaskr.utils.validators import phone_required


class LoginForms(FlaskForm):
    """登录注册相关"""
    username = StringField(label='手机号', validators=[DataRequired()])
    password = StringField(label='密码', validators=[DataRequired()])

    def validate(self, extra_validators=None):
        result = super().validate()
        try:
            username = self.username.data
            if result:
                # 查询数据库，用户是否存在
                user = User.query.filter_by(username=username).first()
                if user is None:
                    result = False
                    self.username.errors = ['手机号或密码有误']
                elif user.status == constants.UserStatus.USER_IN_ACTIVE.value:
                    result = False
                    self.username.errors = ['用户已被禁用']
        except Exception as e:
            pass
        return result

    def do_login(self):
        """ 执行登录的逻辑代码 """
        username = self.username.data
        password = self.password.data
        try:
            user = User.query.filter_by(username=username).first()
            if user.confirm_password(password):
                # 2登录用户
                login_user(user)
                # 3记录日志
                ip = request.headers.get('x-forwarded-for')
                ua = request.headers.get('User-Agent', None)
                obj = UserLoginHistory(username=username, user=user, ip=ip, ua=ua)
                db.session.add(obj)
                db.session.commit()
                return user
            else:
                self.password.errors = ['手机号或密码有误']
        except Exception as e:
            pass
        return None


class RegisterForm(FlaskForm):
    name = StringField(label='姓名', validators=[DataRequired()])
    sex = SelectField(label='性别', choices=['男', '女'], default='男', validators=[DataRequired()])
    birthday = StringField(label='生日', validators=[DataRequired()])
    username = StringField(label='手机号', validators=[DataRequired(), phone_required])
    password = StringField(label='密码', validators=[DataRequired()])
    confirm_password = StringField(label='确认密码', validators=[DataRequired()])
    # 设置密保
    confidentiality_question = StringField(label='密保问题', validators=[DataRequired()],
                                           render_kw={"placeholder": "如：我最喜欢的城市？"})
    confidentiality_answer = StringField(label='密保答案', validators=[DataRequired()],
                                         render_kw={"placeholder": "如：湖南株洲"})

    def validate(self, extra_validators=None):
        result = super().validate()
        username = self.username.data
        password = self.password.data
        confirm_password = self.confirm_password.data
        if result:
            user = User.query.filter_by(username=username).first()
            if user is not None:
                self.username.errors = ['该用户已被注册']
                result = False
            elif len(password) < 6:
                self.password.errors = ['密码长度不能小于5位']
                result = False
            elif len(password) > 18:
                self.password.errors = ['密码长度不能超过17位']
                result = False
            elif password != confirm_password:
                self.confirm_password.errors = ['两次密码输入不一致']
                result = False
        return result

    def do_register(self):
        name = self.name.data
        birthday = self.birthday.data
        sex = self.sex.data
        username = self.username.data
        password = self.password.data
        confidentiality_question = self.confidentiality_question.data
        confidentiality_answer = self.confidentiality_answer.data
        obj = User(name=name,
                   sex=sex,
                   birthday=birthday,
                   username=username,
                   password=password)
        db.session.add(obj)
        db.session.commit()
        user = User.query.filter_by(username=username).first()
        confidentiality_obj = UserConfidentiality(user=user,
                                                  confidentiality_answer=confidentiality_answer,
                                                  confidentiality_question=confidentiality_question)
        db.session.add(confidentiality_obj)
        db.session.commit()


class UserAvatar(FlaskForm):
    user_avatar = FileField(label='用户头像', )


class UserEditForm(FlaskForm):
    name = StringField(label='姓名', validators=[DataRequired()])
    sex = SelectField(label='性别', choices=['男', '女'], validators=[DataRequired()])
    birthday = StringField(label='生日', validators=[DataRequired()])
    confidentiality_question = StringField(label='密保问题', validators=[DataRequired()])
    confidentiality_answer = StringField(label='密保答案', validators=[DataRequired()])


class ForgetPasswordFrom(FlaskForm):
    username = StringField(label='手机号', validators=[DataRequired(), phone_required],
                           render_kw={"placeholder": "请输入您的手机号"})

    def validate(self, extra_validators=None):
        user = User.query.filter_by(username=self.username.data).first()
        if user:
            return True
        else:
            self.username.errors = ['用户不存在']
            return False


class QuestionAnswering(FlaskForm):
    confidentiality_answer = StringField(label='密保答案', validators=[DataRequired()],
                                         render_kw={"placeholder": "请输入密保答案"})

    def __init__(self, user_id):
        self.user_id = user_id
        super().__init__()

    def validate(self, extra_validators=None):
        user = User.query.filter_by(id=self.user_id).first()
        confidentiality_answer = user.get_user_confidentiality.confidentiality_answer
        if self.confidentiality_answer.data != confidentiality_answer:
            self.confidentiality_answer.errors = ['密保答案有误']
            return False
        else:
            return True
        

class ResetPassword(FlaskForm):
    password = StringField(label='新密码', validators=[DataRequired()])
    confirm_password = StringField(label='确认密码', validators=[DataRequired()])

    def __init__(self, user_id):
        self.user_id = user_id
        super().__init__()

    def validate(self, extra_validators=None):
        user = User.query.filter_by(id=self.user_id).first()
        if user:
            result = super().validate()
            password = self.password.data
            confirm_password = self.confirm_password.data
            if result:
                if len(password) < 6:
                    self.password.errors = ['密码长度不能小于5位']
                    result = False
                elif len(password) > 18:
                    self.password.errors = ['密码长度不能超过17位']
                    result = False
                elif password != confirm_password:
                    self.confirm_password.errors = ['两次密码输入不一致']
                    result = False
                return result
