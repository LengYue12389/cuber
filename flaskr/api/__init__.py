from flask import Blueprint

api = Blueprint('api', __name__, url_prefix="")

from . import upload, delete_data
