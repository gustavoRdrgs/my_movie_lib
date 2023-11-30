from flask import request, jsonify, make_response

from ..models.comentarios import Comentarios
from ..schemas.comentarios import ComentariosSchema

comentarios_schema = ComentariosSchema()
comentarios_list_schema = ComentariosSchema(many=True)

def get_comentario_by_movie_id(movie_id):

    return Comentarios.find_by_movie_id(movie_id)