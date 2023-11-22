from flask import request, jsonify, make_response

from ..models.movies_geral import MoviesGeral
from ..schemas.movies_geral import MoviesGeralSchema

users_schema = MoviesGeralSchema()
users_list_schema = MoviesGeralSchema(many=True)

def add_new_movie_geral(titulo, diretor, ano, minutos, genero, image_path, sinopse):

    return MoviesGeral.add_new_movie_geral(titulo, diretor, ano, minutos, genero, image_path, sinopse)

def get_all_geral():

    return MoviesGeral.find_all_geral()

def get_movie_by_id_geral(movie_id):

    return MoviesGeral.find_by_movie_id_geral(movie_id)