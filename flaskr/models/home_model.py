from datetime import datetime
from flaskr.extensions import db


class IndexArticle(db.Model):
    __tablename__ = 'index_article'
    id = db.Column(db.Integer, primary_key=True)
    release_time = db.Column(db.Date, nullable=False)
    title = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('article'))
    content = db.Column(db.Text, nullable=False)


class Banner(db.Model):
    """轮播图"""
    __tablename__ = 'home_banner'
    id = db.Column(db.Integer, primary_key=True)
    image_route = db.Column(db.Text)
    add_time = db.Column(db.Date, default=datetime.now)
    index = db.Column(db.Integer)
    match_id = db.Column(db.ForeignKey('competition_information.id'))