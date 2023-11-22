from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from flask_login import login_required, current_user
from .controller.movies import add_new_movie, find_by_user_id, get_movie_by_id
from .controller.movies_geral import add_new_movie_geral, get_all_geral, get_movie_by_id_geral
from . import db
import json, os

views = Blueprint('views', __name__)

@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    lista_filmes = find_by_user_id(current_user.id)
    return render_template("home.html", user=current_user, filmes=lista_filmes)

@views.route('/movies_page', methods=['GET', 'POST'])
@login_required
def movies_page():
    lista_filmes = get_all_geral()
    return render_template("movies_list.html", user=current_user, filmes=lista_filmes)

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

            add_new_movie_geral(titulo, diretor, ano, minutos, genero, "img/poster_filmes/"+path_titulo+".jpg", sinopse)
            flash('Filme cadastrado com sucesso!', category='success')
            imagem.save(path_image)

    return render_template("add_filme.html", user=current_user)

@views.route('/add_movie_click/<int:filme_id>', methods=['GET', 'POST'])
@login_required
def add_movie_click(filme_id):
    filme = get_movie_by_id_geral(filme_id)
    titulo = filme.titulo
    diretor = filme.diretor
    ano = filme.ano
    minutos = filme.minutos
    genero = filme.genero
    user_ID = current_user.id
    image_path = filme.image_path
    sinopse = filme.sinopse
    movie_ID = filme_id

    add_new_movie(titulo, diretor, ano, minutos, genero, user_ID, image_path, sinopse, movie_ID)
    lista_filmes = get_all_geral()
    return render_template("movies_list.html", user=current_user, filmes=lista_filmes)

@views.route('/movie_page/<int:filme_id>', methods=['GET', 'POST'])
@login_required
def show_movie(filme_id):
    filme = get_movie_by_id_geral(filme_id)
    return render_template('movie_page.html', filme=filme)