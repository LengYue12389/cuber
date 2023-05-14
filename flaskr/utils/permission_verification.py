from functools import wraps
from flask import redirect, url_for

from flask_login import current_user
from .constants import UserRole


def permission_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.is_super == UserRole.SUPER_ADMIN.value or current_user.is_super == UserRole.ADMIN.value:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('users.login'))
    return wrapper
