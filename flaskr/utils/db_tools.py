from flaskr.extensions import db
from flaskr.models.ach_model import AchievementCuber333, AchievementCuber222, AchievementCuberOh, AchievementCuberPy, \
    AchievementCuberSk, Achievement
from flaskr.models.home_model import IndexArticle
from flaskr.models.match_model import CompetitionInformation

from flaskr.utils.constants import MatchEnter


def get_match_details(match_id):
    match_detail = CompetitionInformation.query.filter_by(id=match_id).first()
    return match_detail.details


def get_notice_content(notice_id):
    match_detail = IndexArticle.query.filter_by(id=notice_id).first()
    return match_detail.content


def delete_ach(match_id):
    db.session.query(AchievementCuber333).filter_by(match_id=match_id).delete()
    db.session.query(AchievementCuber222).filter_by(match_id=match_id).delete()
    db.session.query(AchievementCuberOh).filter_by(match_id=match_id).delete()
    db.session.query(AchievementCuberPy).filter_by(match_id=match_id).delete()
    db.session.query(AchievementCuberSk).filter_by(match_id=match_id).delete()
    Achievement.query.filter_by(match_id=match_id).delete()
    db.session.query(CompetitionInformation).filter_by(id=match_id).update(
        {'enter_status': MatchEnter.FUTURE_ENTER.value}
    )
