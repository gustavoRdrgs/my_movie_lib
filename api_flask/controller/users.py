from flask import request, jsonify, make_response

from ..models.users import Users
from ..schemas.users import UsersSchema

users_schema = UsersSchema()
users_list_schema = UsersSchema(many=True)

def get_user_by_email(email):

    return Users.find_by_email(email)
    
def add_user(firstName, email, senha):

    return Users.add_new_user(firstName, email, senha)
    