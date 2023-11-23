from api_flask import db
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
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
    movie_ID = db.Column(db.Integer, db.ForeignKey('movies_geral.id'))

    @classmethod
    def find_by_user_id(cls, user_id) -> List['Movies']:

        engine = ConnectionHandler.get_engine()
        Session = sessionmaker(engine)
        
        with Session() as session:

            return session.query(Movies).filter_by(user_ID = user_id).all()
        
    @classmethod
    def find_by_movie_id(cls, movie_id):

        engine = ConnectionHandler.get_engine()
        Session = sessionmaker(engine)
        
        with Session() as session:

            return session.query(Movies).filter_by(id = movie_id).first()
        
    @classmethod
    def add_new_movie(cls, titulo, diretor, ano, minutos, genero, user_ID, image_path, sinopse, movie_ID):

        engine = ConnectionHandler.get_engine()
        Session = sessionmaker(engine)
        with Session() as session:
            new_movie = Movies(titulo=titulo, diretor=diretor, ano=ano, minutos=minutos, genero=genero, user_ID=user_ID, image_path=image_path, sinopse=sinopse, movie_ID=movie_ID)
            session.add(new_movie)
            session.commit()
        return new_movie
    
    @classmethod
    def find_genero_most_repeat(cls, user_id):

        engine = ConnectionHandler.get_engine()
        Session = sessionmaker(engine)

        with Session() as session:
            genero_mais_comum = session.query(Movies.genero, func.count(Movies.genero).label('contagem')) \
            .filter_by(user_ID = user_id) \
            .group_by(Movies.genero) \
            .order_by(func.count(Movies.genero).desc()) \
            .first()

        return genero_mais_comum
    
    @classmethod
    def find_number_movies_watched(cls, user_id):

        engine = ConnectionHandler.get_engine()
        Session = sessionmaker(engine)

        with Session() as session:
             quantidade_filmes = session.query(func.count(Movies.id)).filter_by(user_ID = user_id).scalar()

        return quantidade_filmes
        