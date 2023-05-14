from flask import flash, render_template, redirect, url_for, request
from flask_login import login_required, current_user

from flaskr.models.user_model import User, UserConfidentiality
from flaskr.users import users
from flaskr.foms.user import UserEditForm, ForgetPasswordFrom, ResetPassword, QuestionAnswering
from flaskr.extensions import db


@users.route('forget_password', methods=['GET', 'POST'])
def forget_password():
    form = ForgetPasswordFrom()
    if form.validate_on_submit():
        username = form.data['username']
        user = User.query.filter_by(username=username).first()
        question = db.session.query(UserConfidentiality).join(User).filter(
            user.id == UserConfidentiality.user_id
        ).first()
        return redirect(url_for(
            'users.question_answering',
            question=question.confidentiality_question,
            user_id=user.id)
        )
    return render_template('users/forget_password.html', form=form)


@users.route('question_answering', methods=['GET', 'POST'])
def question_answering():
    user_id = request.args.get('user_id')
    form = QuestionAnswering(user_id)
    question = request.args.get('question')
    if form.validate_on_submit():
        return redirect(url_for('users.reset_password', user_id=user_id))
    return render_template(
        'users/question_answering.html',
        question=question,
        form=form
    )


@users.route('reset_password', methods=['GET', 'POST'])
def reset_password():
    user_id = request.args.get('user_id')
    form = ResetPassword(user_id=user_id)
    if form.validate_on_submit():
        user = db.session.query(User).filter_by(id=user_id).first()
        user.password = form.confirm_password.data
        db.session.commit()

        flash('密码修改成功', 'success')
        return redirect(url_for('users.login'))
    return render_template('users/reset_password.html', form=form)


@users.route('user_edit', methods=['GET', 'POST'])
@login_required
def user_edit():
    form = UserEditForm()
    if form.validate_on_submit():
        db.session.query(User).filter_by(id=current_user.id).update(
            {
                'name': form.name.data,
                'sex': form.sex.data,
                'birthday': form.birthday.data,
            }
        )
        db.session.query(UserConfidentiality).filter_by(user_id=current_user.id).update(
            {
                'confidentiality_question': form.confidentiality_question.data,
                'confidentiality_answer': form.confidentiality_answer.data
            }
        )
        db.session.commit()
        flash('提交成功', 'success')
    return render_template('users/user_edit.html', form=form, time=current_user.birthday)



