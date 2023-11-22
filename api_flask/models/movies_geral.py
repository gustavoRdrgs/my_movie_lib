from api_flask import db
from sqlalchemy.orm import sessionmaker
from typing import List
from ..utils.ConnectionHandler import ConnectionHandler

class MoviesGeral(db.Model):
    __tablename__ = "movies_geral"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    diretor = db.Column(db.String(100))
    ano = db.Column(db.Integer)
    minutos = db.Column(db.Integer)
    genero = db.Column(db.String(50))
    image_path = db.Column(db.String(300))
    sinopse = db.Column(db.String(1000))
        
    @classmethod
    def find_by_movie_id_geral(cls, movie_id):

        engine = ConnectionHandler.get_engine()
        Session = sessionmaker(engine)
        
        with Session() as session:

            return session.query(MoviesGeral).filter_by(id = movie_id).first()
        
    @classmethod
    def find_all_geral(cls):

        engine = ConnectionHandler.get_engine()
        Session = sessionmaker(engine)
        
        with Session() as session:

            return session.query(MoviesGeral).all()
        
    @classmethod
    def add_new_movie_geral(cls, titulo, diretor, ano, minutos, genero, image_path, sinopse):

        engine = ConnectionHandler.get_engine()
        Session = sessionmaker(engine)
        with Session() as session:
            new_movie = MoviesGeral(titulo=titulo, diretor=diretor, ano=ano, minutos=minutos, genero=genero, image_path=image_path, sinopse=sinopse)
            session.add(new_movie)
            session.commit()
        return new_movie