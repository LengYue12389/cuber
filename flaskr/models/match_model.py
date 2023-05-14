from datetime import datetime
from flaskr.extensions import db
from flaskr.utils import constants


class Info(db.Model):
    """
    参赛选手信息信息
    """
    __tablename__ = 'player_information'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(5), unique=False, nullable=False)
    mobile = db.Column(db.String(11), unique=False, nullable=False)
    birthday = db.Column(db.Date, unique=False, nullable=False)
    registration_items = db.Column(db.String(50), unique=False, nullable=False)
    # 外键关联比赛表
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    match_id = db.Column(db.Integer, db.ForeignKey('competition_information.id'))
    match = db.relationship('CompetitionInformation', backref=db.backref('competition'))
    user = db.relationship('User', backref=db.backref('user_player_info', lazy='dynamic'))
    add_time = db.Column(db.DateTime, default=datetime.now)


class CompetitionInformation(db.Model):
    """
    比赛信息详情表
    """
    __tablename__ = 'competition_information'
    id = db.Column(db.Integer, primary_key=True)
    # 比赛时间
    match_time = db.Column(db.Date, unique=False, nullable=False)
    # 比赛地址
    address = db.Column(db.String(150), unique=False, nullable=False)
    # 报名人数上限
    number_of_applicants = db.Column(db.String(4), nullable=False)
    # 开设项目
    project_opening = db.Column(db.String(500), nullable=False)
    # 比赛的名字
    match_name = db.Column(db.String(200), nullable=False)
    # 基础报名费
    registration_fee = db.Column(db.String(4), nullable=True)
    # 项目报名费
    item_registration_free = db.Column(db.String(4), nullable=True)
    # 报名截止时间
    registration_end_time = db.Column(db.Date, nullable=False)
    # 比赛详情
    details = db.Column(db.Text)
    enter_status = db.Column(db.Integer, default=constants.MatchEnter.FUTURE_ENTER.value)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('match'))

    def __unicode__(self):
        return self.match_name

    def __repr__(self):
        return f'<{self.id}, {self.match_name}, {self.match_time}>'
