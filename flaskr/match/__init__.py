from flask import Blueprint

match = Blueprint('match', __name__, template_folder='./templates/match', url_prefix='/',
                  static_folder='../static')

from . import views_match, match_edit
