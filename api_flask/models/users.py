from api_flask import db
from flask_login import UserMixin
from sqlalchemy.orm import sessionmaker
from typing import List
from ..utils.ConnectionHandler import ConnectionHandler

class Users(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    primeiro_nome = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    senha = db.Column(db.String(200), nullable=False)
    lista_filmes = db.Column(db.String(2000), nullable=True)

    @classmethod
    def find_by_email(cls, email) -> List['Users']:

        engine = ConnectionHandler.get_engine()
        Session = sessionmaker(engine)
        
        with Session() as session:

            return session.query(Users).filter_by(email = email).first()
        
    @classmethod
    def add_new_user(cls, firstName, email, senha):

        engine = ConnectionHandler.get_engine()
        Session = sessionmaker(engine)
        with Session() as session:
            new_user = Users(primeiro_nome=firstName, email=email, senha=senha)
            session.add(new_user)
            session.commit()
        return new_user