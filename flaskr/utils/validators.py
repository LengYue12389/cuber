import re
from wtforms import ValidationError


def phone_required(form, field):
    """ 验证方法，强制用户填入的必须是手机号码，
    否则无法通过表单验证 """
    username = field.data
    pattern = r'^1[0-9]{10}$'
    if not re.search(pattern, username):
        raise ValidationError('请输入手机号')
    return field

