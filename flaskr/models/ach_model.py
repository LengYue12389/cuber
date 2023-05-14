from flaskr.extensions import db


class Achievement(db.Model):
    __tablename__ = 'achievement_table'
    id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('competition_information.id'))
    address = db.Column(db.String(150), unique=False, nullable=False)
    match_name = db.Column(db.String(200), nullable=False)
    match_time = db.Column(db.Date, unique=False, nullable=False)



class AchievementCuber333(db.Model):
    __tablename__ = 'achievement_cuber_333'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('cuber_333', lazy='dynamic'))
    match_id = db.Column(db.Integer, db.ForeignKey('competition_information.id'))
    match = db.relationship('CompetitionInformation', backref=db.backref('match_cuber_333', lazy='dynamic'))
    t1 = db.Column(db.Float)
    t2 = db.Column(db.Float)
    t3 = db.Column(db.Float)
    t4 = db.Column(db.Float)
    t5 = db.Column(db.Float)
    best = db.Column(db.Float)
    ao5 = db.Column(db.Float)
    competition_options = db.Column(db.String(10))


class AchievementCuber222(db.Model):
    __tablename__ = 'achievement_cuber_222'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('cuber_222', lazy='dynamic'))
    match_id = db.Column(db.Integer, db.ForeignKey('competition_information.id'))
    match = db.relationship('CompetitionInformation', backref=db.backref('match_cuber_222', lazy='dynamic'))
    t1 = db.Column(db.Float)
    t2 = db.Column(db.Float)
    t3 = db.Column(db.Float)
    t4 = db.Column(db.Float)
    t5 = db.Column(db.Float)
    best = db.Column(db.Float)
    ao5 = db.Column(db.Float)
    competition_options = db.Column(db.String(10))


class AchievementCuberPy(db.Model):
    __tablename__ = 'achievement_cuber_py'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('cuber_py', lazy='dynamic'))
    match_id = db.Column(db.Integer, db.ForeignKey('competition_information.id'))
    match = db.relationship('CompetitionInformation', backref=db.backref('match_cuber_py', lazy='dynamic'))
    t1 = db.Column(db.Float)
    t2 = db.Column(db.Float)
    t3 = db.Column(db.Float)
    t4 = db.Column(db.Float)
    t5 = db.Column(db.Float)
    best = db.Column(db.Float)
    ao5 = db.Column(db.Float)
    competition_options = db.Column(db.String(10))


class AchievementCuberSk(db.Model):
    __tablename__ = 'achievement_cuber_sk'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('cuber_sk', lazy='dynamic'))
    match_id = db.Column(db.Integer, db.ForeignKey('competition_information.id'))
    match = db.relationship('CompetitionInformation', backref=db.backref('match_cuber_sk', lazy='dynamic'))
    t1 = db.Column(db.Float)
    t2 = db.Column(db.Float)
    t3 = db.Column(db.Float)
    t4 = db.Column(db.Float)
    t5 = db.Column(db.Float)
    best = db.Column(db.Float)
    ao5 = db.Column(db.Float)
    competition_options = db.Column(db.String(10))


class AchievementCuberOh(db.Model):
    __tablename__ = 'achievement_cuber_oh'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('cuber_oh', lazy='dynamic'))
    match_id = db.Column(db.Integer, db.ForeignKey('competition_information.id'))
    match = db.relationship('CompetitionInformation', backref=db.backref('match_cuber_oh', lazy='dynamic'))
    t1 = db.Column(db.Float)
    t2 = db.Column(db.Float)
    t3 = db.Column(db.Float)
    t4 = db.Column(db.Float)
    t5 = db.Column(db.Float)
    best = db.Column(db.Float)
    ao5 = db.Column(db.Float)
    competition_options = db.Column(db.String(10))
