from flask import request, jsonify, make_response

from ..models.users import Users
from ..schemas.users import UsersSchema

users_schema = UsersSchema()
users_list_schema = UsersSchema(many=True)

def get_user_by_email(email):

    return Users.find_by_email(email)

def get_user_by_id(id):

    return Users.find_by_id(id)
    
def add_user(firstName, email, senha):

    return Users.add_new_user(firstName, email, senha)

def update_minutos(id, minutos):

    return Users.update_tempo_user(id, minutos)

def update_descricao(id, descricao):

    if descricao:
        Users.update_descricao_user(id, descricao)

    return True

def update_profile_pic(id, image_path):

    if image_path:
        Users.update_profile_pic_user(id, image_path)

    return True
    