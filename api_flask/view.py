from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from flask_login import login_required, current_user
from collections import Counter
from .controller.users import get_user_by_id, update_minutos, update_descricao, update_profile_pic
from .controller.movies import add_new_movie, find_by_user_id, get_genero_most_repeat, get_movies_watched
from .controller.movies_geral import add_new_movie_geral, get_all_geral, get_movie_by_id_geral
from .utils.Functions import calcular_tempo
from . import db
import json, os

views = Blueprint('views', __name__)

@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    lista_filmes = find_by_user_id(current_user.id)
    movies_counts = Counter([filme.movie_ID for filme in lista_filmes])
    return render_template("home.html", user=current_user, filmes=lista_filmes, movies_counts=movies_counts)

@views.route('/perfil', methods=['GET', 'POST'])
@login_required
def perfil():
    
    genero = None
    dias = 0
    horas = 0
    minutos = 0
    qntd_filmes = 0

    valor_mais_comum = get_genero_most_repeat(current_user.id)
    if valor_mais_comum:
        genero = valor_mais_comum[0]
        dias, horas, minutos = calcular_tempo(current_user.tempo_assistido)
        qntd_filmes = get_movies_watched(current_user.id)

    return render_template("perfil.html", user=current_user, dias=dias, horas=horas, minutos=minutos, genero=genero, qntd_filmes=qntd_filmes)

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

@views.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'POST':
        imagem = request.files['image']
        descricao = request.form['descricao']

        if imagem:
            path_nome = (current_user.primeiro_nome.replace(' ', '_') + str(current_user.id))
            path = "C:/Users/gusta/OneDrive/Documentos/Códigos/Python/my_movie_lib/api_flask/static/img/profile_pictures/"
            path_image = os.path.join(path, path_nome + '.jpg')
            imagem.save(path_image)
            update_profile_pic(current_user.id, "img/profile_pictures/"+path_nome+".jpg")

        update_descricao(current_user.id, descricao)

        if (descricao or imagem):
            flash('Perfil atualizado!', category='success')
            return redirect(url_for('views.perfil'))

    return render_template("edit_profile.html", user=current_user)

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

    user = get_user_by_id(current_user.id)
    print(user.tempo_assistido)
    novo_tempo = (user.tempo_assistido or 0) + minutos

    update_minutos(current_user.id, novo_tempo)
    
    add_new_movie(titulo, diretor, ano, minutos, genero, user_ID, image_path, sinopse, movie_ID)
    lista_filmes = get_all_geral()
    return render_template("movies_list.html", user=current_user, filmes=lista_filmes)

@views.route('/movie_page/<int:filme_id>', methods=['GET', 'POST'])
@login_required
def show_movie(filme_id):
    filme = get_movie_by_id_geral(filme_id)
    return render_template('movie_page.html', filme=filme)