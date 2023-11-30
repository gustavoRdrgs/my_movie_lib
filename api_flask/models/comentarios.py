from api_flask import db
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from typing import List
from ..utils.ConnectionHandler import ConnectionHandler

class Comentarios(db.Model):
    __tablename__ = "comentarios"

    comentario_id = db.Column(db.Integer, primary_key=True)
    texto_comentario = db.Column(db.Text)
    path_imagem_perfil = db.Column(db.Text)
    usuario_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    filme_id = db.Column(db.Integer, db.ForeignKey('movies_geral.id'))

    @classmethod
    def find_by_movie_id(cls, movie_id) -> List['Comentarios']:

        engine = ConnectionHandler.get_engine()
        Session = sessionmaker(engine)
        
        with Session() as session:

            return session.query(Comentarios).filter_by(filme_id = movie_id).all()