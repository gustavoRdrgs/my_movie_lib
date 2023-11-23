from flask import request, jsonify, make_response

from ..models.movies import Movies
from ..schemas.movies import MoviesSchema

users_schema = MoviesSchema()
users_list_schema = MoviesSchema(many=True)

def add_new_movie(titulo, diretor, ano, minutos, genero, user_ID, image_path, sinopse, movie_ID):

    return Movies.add_new_movie(titulo, diretor, ano, minutos, genero, user_ID, image_path, sinopse, movie_ID)

def find_by_user_id(user_id):

    return Movies.find_by_user_id(user_id)

def get_movie_by_id(movie_id):

    return Movies.find_by_movie_id(movie_id)

def get_genero_most_repeat(user_ID):

    return Movies.find_genero_most_repeat(user_ID)

def get_movies_watched(user_ID):

    return Movies.find_number_movies_watched(user_ID)