from flask_login import logout_user, login_user, current_user
from flask import render_template, redirect, url_for, flash, request

from application import app
from application.forms import LoginForm
from application.models import User


@app.route('/login/')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    form = LoginForm()
    return render_template('auth.html', form=form)


@app.route('/login/', methods=['POST'])
def post_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user or not user.check_password(form.password.data):
            flash('Неверный логин или пароль', 'danger')
            return redirect(url_for('login'))
        login_user(user)
        next = request.args.get('next')
        flash('Успешный вход', 'success')
        return redirect(next or url_for('main'))
    return render_template('auth.html', form=form)


@app.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for("login"))
