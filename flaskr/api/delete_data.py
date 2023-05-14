from flask import jsonify
from flask_login import login_required

from flaskr.extensions import db
from . import api
from ..models.home_model import IndexArticle
from ..models.match_model import Info, CompetitionInformation
from ..utils.permission_verification import permission_required
from flaskr.utils.db_tools import delete_ach


@api.route('delete_ach_data/<int:match_id>', methods=['DELETE'])
@login_required
@permission_required
def delete_ach_data(match_id):
    delete_ach(match_id)
    db.session.commit()
    return jsonify({'result': '已删除match_id为{match_id}的所有成绩数据'.format(match_id=match_id)})


@api.route('delete_match/<int:match_id>', methods=['DELETE'])
@login_required
@permission_required
def delete_match_all(match_id):
    delete_ach(match_id)
    Info.query.filter_by(match_id=match_id).delete()
    CompetitionInformation.query.filter_by(id=match_id).delete()
    db.session.commit()
    return jsonify({'result': '已删除match_id为{match_id}的所有比赛数据和成绩数据'.format(match_id=match_id)})


@api.route('delete_notice/<int:notice_id>', methods=['DELETE'])
@login_required
@permission_required
def delete_notice(notice_id):
    IndexArticle.query.filter_by(id=notice_id).delete()
    db.session.commit()
    return jsonify({'result': '已删除notice_id为{notice_id}的通知'.format(notice_id=notice_id)})
