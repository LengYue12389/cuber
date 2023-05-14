from flask import render_template, current_app
from flask_login import login_required, current_user
from sqlalchemy import func

from flaskr.extensions import db
from flaskr.foms.match import EnterAchievementForm, DeleteAchievementForm
from flaskr.utils.constants import MatchEnter
from flaskr.utils.page import paging
from flaskr.utils.permission_verification import permission_required
from . import match
from ..models.ach_model import Achievement
from ..models.match_model import CompetitionInformation, Info
from ..models.user_model import User


@match.route('/enter_list')
@login_required
@permission_required
def enter_list():
    content = CompetitionInformation.query \
        .filter_by(user_id=current_user.id).order_by(CompetitionInformation.match_time.desc()).all()
    context = paging(content, current_app.config['PER_PAGE'])
    return render_template('match/enter/enter_list.html', **context)


@match.route('/enter_achievement/match_id=<int:match_id>', methods=('GET', 'POST'))
@login_required
@permission_required
def enter_achievement(match_id):
    match_ach = CompetitionInformation.query.get(match_id)
    result = Achievement.query.filter(Achievement.match_id == match_ach.id).first()
    if result is None:
        ach_list_obj = Achievement(
            match_id=match_id,
            address=match_ach.address,
            match_time=match_ach.match_time,
            match_name=match_ach.match_name
        )
        competition_obj = db.session.query(CompetitionInformation).filter_by(id=match_ach.id).update(
            {'enter_status': MatchEnter.ENTERED.value}
        )
        db.session.add(ach_list_obj, competition_obj)
        db.session.commit()
    match_data = {
        'name': match_ach.match_name,
        'address': match_ach.address,
        'match_time': match_ach.match_time,
        'match_enter': match_ach.enter_status
    }
    enter_form = EnterAchievementForm()
    if enter_form.submit_enter.data and enter_form.validate():
        enter_form.do_enter(match_id=match_id)

    delete_form = DeleteAchievementForm()
    if delete_form.submit_delete.data and delete_form.validate():
        delete_form.do_delete(match_id=match_id)
    return render_template('match/enter/enter_achievement.html',
                           match_ach=match_ach,
                           enter_form=enter_form,
                           delete_form=delete_form,
                           match_data=match_data)


@match.route('get_entries/match_id=<int:match_id>')
@login_required
def get_entries(match_id):
    entries = db.session.query(User, Info).join(Info).filter(Info.match_id == match_id).all()
    count = db.session.query(func.count(Info.id), CompetitionInformation.number_of_applicants).join(Info).filter(
        Info.match_id == match_id
    ).first()
    num = CompetitionInformation.query.get(match_id)
    return render_template('match/get_entries.html', entries=entries, count=count, num=num)
