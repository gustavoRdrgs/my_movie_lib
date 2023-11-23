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
    path_profile_pic = db.Column(db.String(300))
    tempo_assistido = db.Column(db.Integer)
    descricao = db.Column(db.String(1000), nullable=True)
    
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
    
    @classmethod
    def update_tempo_user(cls, user_ID, minutos):

        engine = ConnectionHandler.get_engine()
        Session = sessionmaker(engine)
        with Session() as session:
            user_update = session.query(Users).filter(Users.id == user_ID).update({Users.tempo_assistido: minutos})
            session.commit()
        return user_update
    
    @classmethod
    def find_by_id(cls, id) -> List['Users']:

        engine = ConnectionHandler.get_engine()
        Session = sessionmaker(engine)
        
        with Session() as session:

            return session.query(Users).filter_by(id = id).first()
    
    @classmethod
    def update_descricao_user(cls, user_ID, descricao):

        engine = ConnectionHandler.get_engine()
        Session = sessionmaker(engine)
        with Session() as session:
            user_update = session.query(Users).filter(Users.id == user_ID).update({Users.descricao: descricao})
            session.commit()
        return user_update
    
    @classmethod
    def update_profile_pic_user(cls, user_ID, image_path):

        engine = ConnectionHandler.get_engine()
        Session = sessionmaker(engine)
        with Session() as session:
            user_update = session.query(Users).filter(Users.id == user_ID).update({Users.path_profile_pic: image_path})
            session.commit()
        return user_update