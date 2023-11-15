from flask import Blueprint, Flask, render_template, request, flash, redirect, url_for
from .controller.users import add_user, get_user_by_email
from .models.users import Users
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        user = get_user_by_email(email)
        password = request.form.get('password')
        if user:
            if password == user.senha:
                flash('Logado com sucesso!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Senha incorreta!', category='error')
        else:
            flash('Este email não existe!', category='error')

    return render_template("index.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':

        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = Users.query.filter_by(email=email).first()

        if user:
            flash('Este email já foi cadastrado', category='error')
        if len(email) < 4:
            flash('Email muito curto', category='error')
        elif len(first_name) < 2:
            flash('Primeiro nome tem que ter mais de 1 caractere', category='error')
        elif password1 != password2:
            flash('As senhas não são iguais', category='error')
        elif len(password1) < 7:
            flash('Senha menor que 7 caracteres', category='error')
        else:
            add_user(first_name, email, password1)
            login_user(user, remember=True)
            flash('Conta criada!', category='success')
            return redirect(url_for('auth.index'))
        
    return render_template('sign_up.html', user=current_user)