from flask import request, jsonify, make_response

from ..models.users import Users
from ..schemas.users import UsersSchema

users_schema = UsersSchema()
users_list_schema = UsersSchema(many=True)

def get_users():

    query = users_list_schema.dump(Users.find_all())
    print(jsonify)
    print(query)
    if query:
        return 'passou'
    else:
        return None
    
def add_user(firstName, email, senha):

    return Users.add_new_user(firstName, email, senha)
    