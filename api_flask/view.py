from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from flask_login import login_required, current_user
from .controller.movies import add_new_movie, find_by_user_id
from . import db
import json, os

views = Blueprint('views', __name__)

@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    print(current_user.id)
    lista_filmes = find_by_user_id(current_user.id)
    return render_template("home.html", user=current_user, filmes=lista_filmes)

@views.route('/add_movie', methods=['GET', 'POST'])
@login_required
def add_movie():
    if request.method == 'POST':
        titulo = request.form['film-name']
        diretor = request.form['director']
        ano = request.form['year']
        minutos = request.form['time-minutes']
        genero = request.form['genero']
        imagem = request.files['image']
        sinopse = request.form['sinopse']

        if not titulo:
            flash('Há informações do filme faltando', category='error')
        elif not diretor:
            flash('Há informações do filme faltando', category='error')
        elif not ano:
            flash('Há informações do filme faltando', category='error')
        elif not minutos:
            flash('Há informações do filme faltando', category='error')
        elif not genero:
            flash('Há informações do filme faltando', category='error')
        elif not imagem:
            flash('Há informações do filme faltando', category='error')
        elif not sinopse:
            flash('Há informações do filme faltando', category='error')
        else:
            path_titulo = titulo.replace(' ', '_')

            path = "C:/Users/gusta/OneDrive/Documentos/Códigos/Python/my_movie_lib/api_flask/static/img/poster_filmes/"
            path_image = os.path.join(path, path_titulo + '.jpg')

            add_new_movie(titulo, diretor, ano, minutos, genero, current_user.id, "img/poster_filmes/"+path_titulo+".jpg", sinopse)
            flash('Filme cadastrado com sucesso!', category='success')
            imagem.save(path_image)

    return render_template("add_filme.html", user=current_user)

"""def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            #new_note = Note(data=note, user_id=current_user.id)
            #db.session.add(new_note)
            #db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)"""