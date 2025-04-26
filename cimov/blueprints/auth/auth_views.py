from flask import Blueprint, render_template, url_for, redirect, request, flash
from cimov.extensions.forms import LoginForm, RegistroForm
from cimov.extensions.db import db, User
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
        flash('Email ou senha inválido(s)')
    return render_template('auth/login.html', form=form)

@auth.route('/registro', methods=['GET', 'POST'])
def registro():
    form = RegistroForm()
    if form.validate_on_submit():
        user = User(
            email=form.email.data,
            nome_completo=form.nome.data,
            cpf=form.cpf.data,
            telefone=form.telefone.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        flash('Você poderá fazer login agora.')
        return redirect(url_for('auth.login'))
    return render_template('auth/registro.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você saiu do sistema.')
    return redirect(url_for('main.index'))