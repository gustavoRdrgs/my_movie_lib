from flask import request, jsonify, make_response

from ..models.movies import Movies
from ..schemas.movies import MoviesSchema

users_schema = MoviesSchema()
users_list_schema = MoviesSchema(many=True)

def add_new_movie(titulo, diretor, ano, minutos, genero, user_ID, image_path, sinopse):

    return Movies.add_new_movie(titulo, diretor, ano, minutos, genero, user_ID, image_path, sinopse)

def find_by_user_id(user_id):

    return Movies.find_by_user_id(user_id)