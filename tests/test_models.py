from flaskr.models.user_model import User
from flaskr.extensions import db


def test_create_user():
    username = '13200000007'
    name = '小明'
    password = 'ASDFAD@#23232'
    sex = '男'
    birthday = '2022-01-01'
    user = User(username=username, name=name, password=password, birthday=birthday, sex=sex)
    db.session.add(user)
    db.session.commit()
    assert user.id is not None



