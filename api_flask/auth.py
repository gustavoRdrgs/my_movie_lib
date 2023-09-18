from flask import Blueprint, Flask, render_template, request, flash, redirect, url_for
from .controller.users import get_users, add_user
from .models.users import Users

auth = Blueprint('auth', __name__)

@auth.route('/', methods=['GET', 'POST'])
def index():
    email = request.form.get('email')
    #print(get_users())
    return render_template("index.html")

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
            flash('Conta criada!', category='success')
            return redirect(url_for('auth.index'))
        
    return render_template('sign_up.html')