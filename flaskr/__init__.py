import warnings
from flask import Flask
from config import Config
from flaskr.extensions import init_extensions
from flaskr.utils.constants import UserRole, MatchEnter
from flaskr.utils.filters import set_dnf_time, two_decimal

warnings.filterwarnings("ignore")


def create_app():
    app = Flask(__name__)
    init_extensions(app)
    app.config.from_object(Config)
    app.add_template_global(UserRole)
    app.add_template_global(MatchEnter)
    app.add_template_filter(set_dnf_time, 'set_dnf_time')
    app.add_template_filter(two_decimal), 'two_decimal'

    from flaskr.users import users
    app.register_blueprint(users)
    from flaskr.match import match
    app.register_blueprint(match)
    from flaskr.api import api
    app.register_blueprint(api)

    return app
