from flask import render_template, flash, request, current_app
from flask_login import login_required, current_user
from flaskr.extensions import db
from flaskr.foms.match import CreateMatchForm, CreateHomeNoticeForm
from flaskr.utils.page import paging
from flaskr.utils.db_tools import get_match_details, get_notice_content
from flaskr.utils.permission_verification import permission_required
from . import match
from ..models.home_model import IndexArticle
from ..models.match_model import CompetitionInformation


@match.route('match_management')
@login_required
@permission_required
def match_management():
    match_lst = CompetitionInformation.query.filter_by(user_id=current_user.id)\
        .order_by(CompetitionInformation.match_time.desc()).all()
    context = paging(match_lst, current_app.config['PER_PAGE'])
    return render_template('match/match_management.html', **context)


@match.route('create_match', methods=['GET', 'POST'])
@login_required
@permission_required
def create_match():
    form = CreateMatchForm()
    if form.validate_on_submit():
        data = {
            'match_name': form.match_name.data,
            'match_time': form.match_time.data,
            'registration_end_time': form.registration_end_time.data,
            'address': form.address.data,
            'registration_fee': form.registration_fee.data,
            'item_registration_free': form.item_registration_free.data,
            'project_opening': form.project_opening.data,
            'number_of_applicants': form.number_of_applicants.data,
            'details': form.details.data,
            'user_id': current_user.id
        }
        match_obj = CompetitionInformation(**data)
        db.session.add(match_obj)
        db.session.commit()
        flash('提交成功', 'success')
    return render_template('match/create_match.html', form=form)


@match.route('edit_match/match_id=<int:match_id>', methods=['GET', 'POST'])
@login_required
@permission_required
def edit_match(match_id):
    match_obj = CompetitionInformation.query.get(match_id)
    form = CreateMatchForm()
    form.details.data = get_match_details(match_id)
    if form.validate_on_submit():
        data = {
            'match_name': form.match_name.data,
            'match_time': form.match_time.data,
            'registration_end_time': form.registration_end_time.data,
            'address': form.address.data,
            'registration_fee': form.registration_fee.data,
            'item_registration_free': form.item_registration_free.data,
            'project_opening': form.project_opening.data,
            'number_of_applicants': form.number_of_applicants.data,
            'details': request.form.get('details'),
        }
        CompetitionInformation.query.filter_by(id=match_id).update(data)
        db.session.commit()
        flash('提交成功', 'success')
    return render_template('match/edit_match.html',
                           match_obj=match_obj,
                           form=form,
                           time=match_obj.match_time,
                           time2=match_obj.registration_end_time)


@match.route('create_home_notice', methods=['GET', 'POST'])
@login_required
@permission_required
def create_home_notice():
    form = CreateHomeNoticeForm()
    if form.validate_on_submit():
        data = {
            'title': form.title.data,
            'release_time': form.release_time.data,
            'content': form.content.data,
            'user_id': current_user.id
        }
        match_obj = IndexArticle(**data)
        db.session.add(match_obj)
        db.session.commit()
        flash('提交成功', 'success')
    return render_template('match/create_home_notice.html', form=form)


@match.route('home_notice_management')
@login_required
@permission_required
def home_notice_management():
    match_lst = IndexArticle.query.filter_by(user_id=current_user.id)\
        .order_by(IndexArticle.release_time.desc()).all()
    context = paging(match_lst, current_app.config['PER_PAGE'])
    return render_template('match/home_notice_management.html', **context)


@match.route('edit_notice/notice_id=<int:notice_id>', methods=['GET', 'POST'])
@login_required
@permission_required
def edit_notice(notice_id):
    notice_obj = IndexArticle.query.get(notice_id)
    form = CreateHomeNoticeForm()
    form.content.data = get_notice_content(notice_id)
    if form.validate_on_submit():
        data = {
            'title': form.title.data,
            'release_time': form.release_time.data,
            'content':  request.form.get('content'),
        }
        IndexArticle.query.filter_by(id=notice_id).update(data)
        db.session.commit()
        flash('提交成功', 'success')
    return render_template('match/edit_notice.html', notice_obj=notice_obj, form=form, time=notice_obj.release_time)