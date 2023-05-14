from datetime import datetime

from flask import render_template, flash, redirect, url_for, jsonify, request, current_app
from flask_login import login_required, current_user
from pypinyin import pinyin, Style
from sqlalchemy import and_, func

from flaskr.extensions import db
from flaskr.foms.match import InfoForm, EnterAchievementForm, DeleteAchievementForm, RankingForm

from flaskr.utils.constants import MatchEnter
from flaskr.utils.constants import UserRole
from flaskr.utils.page import paging
from flaskr.utils.permission_verification import permission_required
from . import match
from ..models.ach_model import AchievementCuber333, AchievementCuber222, AchievementCuberOh, AchievementCuberSk, \
    AchievementCuberPy, Achievement
from ..models.home_model import Banner, IndexArticle
from ..models.match_model import CompetitionInformation, Info
from ..models.user_model import User


@match.route('/')
def index():
    banner = Banner.query.all()
    articles = IndexArticle.query.order_by(IndexArticle.release_time.desc()).all()
    context = paging(articles, current_app.config['INDEX_PAGE'])
    return render_template('match/index.html', banner=banner, role=UserRole, **context)


@match.route('/article_detail/article_id=<int:article_id>')
def article_detail(article_id):
    article = IndexArticle.query.get(article_id)
    return render_template('match/index_article_detail.html', article=article)


@match.route('/sign_up/match_id=<int:match_id>', methods=('GET', 'POST'))
@login_required
def sign_up(match_id):
    #  信息收集
    form = InfoForm()
    competition = CompetitionInformation.query.get(match_id)
    opens_item = competition.project_opening
    # 报名项目显示和隐藏
    items = [form.cuber_oh, form.cuber_222, form.cuber_py, form.cuber_333, form.cuber_sk]
    display = []
    opens_list = opens_item.split('，')
    opens_list.sort(key=lambda keys: [pinyin(q, style=Style.TONE3) for q in keys])
    for i in opens_list:
        for j in items:
            if i == j.label.text:
                display.append(j)

    if form.validate_on_submit():
        registration_items = []
        for i in items:
            if i.data:
                registration_items.append(i.label.text)
        info_obj = Info(name=current_user.name,
                        birthday=current_user.birthday,
                        mobile=current_user.username,
                        registration_items='，'.join(registration_items),
                        match_id=match_id, user_id=current_user.id)
        # 查一查数据库是不是重复报名
        if Info.query.filter(and_(Info.mobile.startswith(current_user.username),
                                  Info.match_id == match_id)).first():
            flash('已报名，请勿重复提交', 'danger')
        elif Info.query.filter(Info.match_id == match_id).count() >= int(competition.number_of_applicants):
            flash('报名人数已满', 'warning')
        elif len(registration_items) == 0:
            flash('必须报一项', 'danger')
        else:
            try:
                db.session.add(info_obj)
                db.session.commit()
            except Exception as e:
                pass
            flash('提交成功', 'success')
            return redirect(url_for('match.sign_up', match_id=match_id))
    return render_template('match/sign_up.html', form=form, display=display)


@match.route('/list')
def get_match():
    current_time = datetime.now().strftime('%Y%m%d')
    if request.args.get('search'):
        keyword = request.args['search']
        news_content = CompetitionInformation.query. \
            filter(CompetitionInformation.match_name.like("%" + keyword + "%")) \
            .order_by(CompetitionInformation.match_time.desc()).all()
        news_context = paging(news_content, current_app.config['PER_PAGE'])
        return render_template('match/list_page.html', **news_context, current_time=current_time)

    content = CompetitionInformation.query.order_by(CompetitionInformation.match_time.desc()).all()
    context = paging(content, current_app.config['PER_PAGE'])
    return render_template('match/list_page.html', **context, current_time=current_time)


@match.route('/match_detail/match_id=<int:match_id>')
def match_details(match_id):
    competition = CompetitionInformation.query.get(match_id)
    current_time = datetime.now().strftime('%Y%m%d')
    return render_template('match/match_detail.html',
                           match_id=match_id,
                           competition=competition,
                           current_time=current_time)


@match.route('/achievement_detail/match_id=<int:match_id>')
@login_required
def achievement_detail(match_id):
    match_obj = CompetitionInformation.query.get(match_id)
    # project_opening = match_obj.project_opening.split('，')
    return render_template('match/achievement_detail.html', match_obj=match_obj)


@match.route('achievement_data/match_id=<int:match_id>')
@login_required
def achievement_data(match_id):
    # 成绩数据接口
    ach_cuber_333 = db.session.query(User, AchievementCuber333, AchievementCuber333.competition_options). \
        join(AchievementCuber333).filter(AchievementCuber333.match_id == match_id). \
        order_by(AchievementCuber333.ao5, AchievementCuber333.best).all()
    ach_cuber_222 = db.session.query(User, AchievementCuber222, AchievementCuber222.competition_options). \
        join(AchievementCuber222).filter(AchievementCuber222.match_id == match_id). \
        order_by(AchievementCuber222.ao5, AchievementCuber222.best).all()
    ach_cuber_oh = db.session.query(User, AchievementCuberOh, AchievementCuberOh.competition_options). \
        join(AchievementCuberOh).filter(AchievementCuberOh.match_id == match_id). \
        order_by(AchievementCuberOh.ao5, AchievementCuberOh.best).all()
    ach_cuber_sk = db.session.query(User, AchievementCuberSk, AchievementCuberSk.competition_options). \
        join(AchievementCuberSk).filter(AchievementCuberSk.match_id == match_id). \
        order_by(AchievementCuberSk.ao5, AchievementCuberSk.best).all()
    ach_cuber_py = db.session.query(User, AchievementCuberPy, AchievementCuberPy.competition_options). \
        join(AchievementCuberPy).filter(AchievementCuberPy.match_id == match_id). \
        order_by(AchievementCuberPy.ao5, AchievementCuberPy.best).all()
    match_obj = CompetitionInformation.query.get(match_id)
    project_opening = match_obj.project_opening.split('，')

    data = render_template('match/achievement_data.html', data={
        'ach_cuber_333': ach_cuber_333,
        'ach_cuber_222': ach_cuber_222,
        'ach_cuber_oh': ach_cuber_oh,
        'ach_cuber_sk': ach_cuber_sk,
        'ach_cuber_py': ach_cuber_py,
    }, project_opening=project_opening, match_obj=match_obj)
    return jsonify({'data': data})


@match.route('/achievement_person')
@login_required
def achievement_person():
    if request.args.get('search'):
        keyword = request.args['search']
        news_user = User.query.filter(User.name.like("%" + keyword + "%")).all()
        news_context = paging(news_user, current_app.config['PER_PAGE'])
        return render_template('match/achievement_person.html', **news_context)

    user = db.session.query(User).all()
    context = paging(user, current_app.config['PER_PAGE'])
    return render_template('match/achievement_person.html', **context)


@match.route('/achievement_list')
@login_required
def achievement_list():
    if request.args.get('search'):
        keyword = request.args['search']
        news_ach_list = Achievement.query. \
            filter(Achievement.match_name.like("%" + keyword + "%")) \
            .order_by(Achievement.match_time.desc()).all()
        news_context = paging(news_ach_list, current_app.config['PER_PAGE'])
        return render_template('match/achievement_list.html', **news_context)

    ach_list = Achievement.query.order_by(Achievement.match_time.desc()).all()
    context = paging(ach_list, current_app.config['PER_PAGE'])
    return render_template('match/achievement_list.html', **context)


@match.route('/about')
def about():
    return render_template('match/about.html')


@match.route('/enter_list')
@login_required
@permission_required
def enter_list():
    content = CompetitionInformation.query\
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


# @match.get('ranking')
# @login_required
# def ranking():
#     form = RankingForm()
#     if request.args.get('cuber') == '三阶':
#         cuber_333_ach = db.session.query(func.min(AchievementCuber333.best), User, Info).join(AchievementCuber333) \
#             .join(Info).group_by(AchievementCuber333.best).filter(User.sex == request.args['sex'])\
#             .order_by(AchievementCuber333.best).all()
#     if request.args.get('submit') == '平均':
#         return render_template('match/ranking.html', form=form, request=request, temp=False)
#     return render_template('match/ranking.html', form=form, request=request, temp=True)
