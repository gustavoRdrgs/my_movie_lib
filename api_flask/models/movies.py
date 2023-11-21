from api_flask import db
from sqlalchemy.orm import sessionmaker
from typing import List
from ..utils.ConnectionHandler import ConnectionHandler

class Movies(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    diretor = db.Column(db.String(100))
    ano = db.Column(db.Integer)
    minutos = db.Column(db.Integer)
    genero = db.Column(db.String(50))
    user_ID = db.Column(db.Integer, db.ForeignKey('users.id'))
    image_path = db.Column(db.String(300))
    sinopse = db.Column(db.String(1000))

    @classmethod
    def find_by_user_id(cls, user_id) -> List['Movies']:

        engine = ConnectionHandler.get_engine()
        Session = sessionmaker(engine)
        
        with Session() as session:

            return session.query(Movies).filter_by(user_ID = user_id).all()
        
    @classmethod
    def add_new_movie(cls, titulo, diretor, ano, minutos, genero, user_ID, image_path, sinopse):

        engine = ConnectionHandler.get_engine()
        Session = sessionmaker(engine)
        with Session() as session:
            new_movie = Movies(titulo=titulo, diretor=diretor, ano=ano, minutos=minutos, genero=genero, user_ID=user_ID, image_path=image_path, sinopse=sinopse)
            session.add(new_movie)
            session.commit()
        return new_movie