from flask import flash
from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, RadioField, FloatField, IntegerField, StringField, DateField, SelectField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditorField
from flaskr.extensions import db
from flaskr.models.ach_model import AchievementCuber333, AchievementCuber222, AchievementCuberOh, AchievementCuberSk, \
    AchievementCuberPy
from flaskr.models.match_model import Info
from flaskr.models.user_model import User
from sqlalchemy import and_


class InfoForm(FlaskForm):
    """报名相关"""
    cuber_222 = BooleanField(label='二阶')
    cuber_333 = BooleanField(label='三阶')
    cuber_oh = BooleanField(label='单手')
    cuber_sk = BooleanField(label='斜转')
    cuber_py = BooleanField(label='金字塔')
    submit = SubmitField(label='提交')


class EnterAchievementForm(FlaskForm):
    cuber_option_enter = RadioField('项目', choices=[
        ('三阶', '三阶'),
        ('二阶', '二阶'),
        ('单手', '单手'),
        ('金字塔', '金字塔'),
        ('斜转', '斜转')], validators=[DataRequired()])
    competition_options_enter = RadioField('比赛选项', choices=[
        ('初赛', '初赛'),
        ('复赛', '复赛'),
        ('决赛', '决赛'), ], validators=[DataRequired()])
    user_id_enter = IntegerField(label='选手ID', validators=[DataRequired()])
    time_1 = FloatField(label='T1', default=None)
    time_2 = FloatField(label='T2', default=None)
    time_3 = FloatField(label='T3', default=None)
    time_4 = FloatField(label='T4', default=None)
    time_5 = FloatField(label='T5', default=None)
    submit_enter = SubmitField(label='录入')

    def validate(self, extra_validators=None):
        user = User.query.get(self.data['user_id_enter'])
        if user:
            result = True
        else:
            self.user_id_enter.errors = ['暂无该用户']
            result = False
        return result

    def cuber_item(self):
        if self.data['cuber_option_enter'] == '二阶':
            return AchievementCuber222
        elif self.data['cuber_option_enter'] == '三阶':
            return AchievementCuber333
        elif self.data['cuber_option_enter'] == '单手':
            return AchievementCuberOh
        elif self.data['cuber_option_enter'] == '斜转':
            return AchievementCuberSk
        elif self.data['cuber_option_enter'] == '金字塔':
            return AchievementCuberPy

    def do_enter(self, match_id):
        user = User.query.get(self.data['user_id_enter'])
        if db.session.query(Info).filter(and_(Info.user_id == user.id, match_id == Info.match_id)).first():
            info_obj = Info.query.filter_by(user_id=user.id).first()
            registration_items = info_obj.registration_items.split('，')
            if self.data['cuber_option_enter'] in registration_items:
                result = self.__process_ach_data()

                cuber_options = self.cuber_item()
                cuber = cuber_options.query.filter(
                    and_(
                        cuber_options.match_id == match_id,
                        cuber_options.competition_options == self.competition_options_enter.data,
                        cuber_options.user_id == user.id
                    )
                ).first()
                if cuber is None:
                    try:
                        if result[0] == "best_2" or result[0] == 'best_3':
                            self.__enter_ach(match_id, best=result[1])
                        elif result[0] == 'best':
                            self.__enter_ach(match_id, best=result[1], ao5=result[2])
                        flash(
                            f'{user.name} {self.cuber_option_enter.data} {self.competition_options_enter.data}，成绩录入成功',
                            'success')
                    except Exception as e:
                        flash('至少输入两次成绩', 'danger')
                else:
                    flash(f'【无法重复录入】{user.name}，已存在成绩 项目：{self.data["cuber_option_enter"]}，'
                          f'类型：{cuber.competition_options}；'
                          f'成绩为：T1：{cuber.t1}，T2：{cuber.t2}，T3：{cuber.t3}，T4：{cuber.t4}，T5：{cuber.t5}', 'danger')
            else:
                flash(f'{user.name}，没有报名该项目', 'danger')
        else:
            flash(f'{user.name}，没有报名本场比赛', 'danger')

    @staticmethod
    def __avg(lst: list) -> float:
        lst.remove(min(lst))
        lst.remove(max(lst))
        sum_lst = 0
        lens = len(lst)
        for i in lst:
            sum_lst = sum_lst + i
        avg_time = round(sum_lst / lens, 2)
        return avg_time

    @staticmethod
    def __process_grades(time_list):
        ach_lst = []
        for eun, time in enumerate(time_list):
            if time:
                ach_lst.append(time)
        return ach_lst

    def __process_ach_data(self):
        time_list = (self.time_1.data, self.time_2.data, self.time_3.data, self.time_4.data, self.time_5.data)
        result_data = self.__process_grades(time_list)
        if len(result_data) == 2:
            best_2 = min(result_data)
            return 'best_2', best_2
        elif len(result_data) == 3:
            best_3 = min(result_data)
            return 'best_3', best_3
        elif len(result_data) == 5:
            best = min(result_data)
            ao5 = self.__avg(result_data)
            if ao5 > 9999:
                ao5 = 99999
            return 'best', best, ao5

    def __enter_ach(self, match_id, best=None, ao5=None):
        ach_obj = dict(user_id=self.data['user_id_enter'],
                       match_id=match_id,
                       best=best,
                       ao5=ao5,
                       t1=self.data['time_1'],
                       t2=self.data['time_2'],
                       t3=self.data['time_3'],
                       t4=self.data['time_4'],
                       t5=self.data['time_5'],
                       competition_options=self.data['competition_options_enter'])

        if self.data['cuber_option_enter'] == '三阶':
            ach_obj = AchievementCuber333(**ach_obj)
        elif self.data['cuber_option_enter'] == '二阶':
            ach_obj = AchievementCuber222(**ach_obj)
        elif self.data['cuber_option_enter'] == '单手':
            ach_obj = AchievementCuberOh(**ach_obj)
        elif self.data['cuber_option_enter'] == '斜转':
            ach_obj = AchievementCuberSk(**ach_obj)
        elif self.data['cuber_option_enter'] == '金字塔':
            ach_obj = AchievementCuberPy(**ach_obj)
        db.session.add(ach_obj)
        db.session.commit()


class DeleteAchievementForm(FlaskForm):
    cuber_option_delete = RadioField('项目', choices=[
        ('三阶', '三阶'),
        ('二阶', '二阶'),
        ('单手', '单手'),
        ('金字塔', '金字塔'),
        ('斜转', '斜转')], validators=[DataRequired()])
    competition_options_delete = RadioField('比赛选项', choices=[
        ('初赛', '初赛'),
        ('复赛', '复赛'),
        ('决赛', '决赛')], validators=[DataRequired()])
    user_id_delete = IntegerField(label='选手ID', validators=[DataRequired()])
    submit_delete = SubmitField(label='删除')

    def validate(self, extra_validators=None):
        user = User.query.get(self.data['user_id_delete'])
        if user:
            result = True
        else:
            self.user_id_delete.errors = ['暂无该用户']
            result = False
        return result

    def cuber_item(self):
        if self.data['cuber_option_delete'] == '二阶':
            return AchievementCuber222
        elif self.data['cuber_option_delete'] == '三阶':
            return AchievementCuber333
        elif self.data['cuber_option_delete'] == '单手':
            return AchievementCuberOh
        elif self.data['cuber_option_delete'] == '斜转':
            return AchievementCuberSk
        elif self.data['cuber_option_delete'] == '金字塔':
            return AchievementCuberPy

    def do_delete(self, match_id):
        user = User.query.get(self.data['user_id_delete'])
        if db.session.query(Info).filter(and_(Info.user_id == user.id, match_id == Info.match_id)).first():
            info_obj = Info.query.filter_by(user_id=user.id).first()
            registration_items = info_obj.registration_items.split('，')
            cuber_options = self.cuber_item()
            cuber = cuber_options.query.filter(
                and_(
                    cuber_options.match_id == match_id,
                    cuber_options.competition_options == self.competition_options_delete.data,
                    cuber_options.user_id == user.id
                )
            ).first()
            if cuber is not None:
                if self.data['cuber_option_delete'] in registration_items:
                    self.__delete_ach(match_id)
                    flash(
                        f'{user.name} {self.cuber_option_delete.data} {self.competition_options_delete.data}，成绩删除成功',
                        'success')
                else:
                    flash(f'{user.name}，没有报名该项目', 'danger')
            else:
                flash(f'删除失败，暂无 {user.name} '
                      f'{self.cuber_option_delete.data}'
                      f'{self.competition_options_delete.data}的成绩', 'danger')
        else:
            flash(f'{user.name}，没有报名本场比赛', 'danger')

    def __delete_ach(self, match_id):
        user_id = self.data['user_id_delete']

        if self.data['cuber_option_delete'] == '三阶':
            AchievementCuber333.query.filter(
                AchievementCuber333.user_id == user_id,
                AchievementCuber333.match_id == match_id,
                AchievementCuber333.competition_options == self.data['competition_options_delete']
            ).delete()
        elif self.data['cuber_option_delete'] == '二阶':
            AchievementCuber222.query.filter(
                AchievementCuber222.user_id == user_id,
                AchievementCuber222.match_id == match_id,
                AchievementCuber222.competition_options == self.data['competition_options_delete']
            ).delete()
        elif self.data['cuber_option_delete'] == '单手':
            AchievementCuberOh.query.filter(
                AchievementCuberOh.user_id == user_id,
                AchievementCuberOh.match_id == match_id,
                AchievementCuberOh.competition_options == self.data['competition_options_delete']
            ).delete()
        elif self.data['cuber_option_delete'] == '斜转':
            AchievementCuberSk.query.filter(
                AchievementCuberSk.user_id == user_id,
                AchievementCuberSk.match_id == match_id,
                AchievementCuberSk.competition_options == self.data['competition_options_delete']
            ).delete()
        elif self.data['cuber_option_delete'] == '金字塔':
            AchievementCuberPy.query.filter(
                AchievementCuberPy.user_id == user_id,
                AchievementCuberPy.match_id == match_id,
                AchievementCuberPy.competition_options == self.data['competition_options_delete']
            ).delete()
        db.session.commit()


class CreateMatchForm(FlaskForm):
    """发布比赛"""
    match_name = StringField(label='比赛名称', validators=[DataRequired()])
    address = StringField(label='地址', validators=[DataRequired()])
    project_opening = StringField(label='开设项目', validators=[DataRequired()])
    match_time = DateField(label='比赛时间', validators=[DataRequired()])
    number_of_applicants = StringField(label='报名人数上限', validators=[DataRequired()])
    registration_end_time = DateField(label='报名截止时间', validators=[DataRequired()])
    registration_fee = StringField(label='基础报名费', default=0)
    item_registration_free = StringField(label='项目报名费', default=0)
    details = CKEditorField(label='详情')
    submit = SubmitField(label='提交')


class CreateHomeNoticeForm(FlaskForm):
    """首页通知"""
    title = StringField(label='标题', validators=[DataRequired()])
    release_time = DateField(label='时间', validators=[DataRequired()])
    content = CKEditorField(label='详情')
    submit = SubmitField(label='提交')


class RankingForm(FlaskForm):
    cuber = SelectField(label='项目',
                        choices=['三阶', '二阶', '单手', '斜转', '金字塔'],
                        default='三阶',
                        validators=[DataRequired()])
    sex = SelectField(label='姓别',
                      choices=['所有', '男', '女'],
                      default='所有',
                      validators=[DataRequired()])
    submit = SubmitField()
