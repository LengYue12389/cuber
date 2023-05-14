from flask import Blueprint

users = Blueprint('users', __name__, template_folder='./templates', url_prefix='/',
                  static_folder='../static')

from .views_user import *
from .edit_info import *
