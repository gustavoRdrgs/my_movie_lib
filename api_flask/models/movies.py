from api_flask import db
from sqlalchemy.orm import sessionmaker
from typing import List
from ..utils.ConnectionHandler import ConnectionHandler

class Movies(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    diretor = db.Column(db.String(100))
    ano = db.Column(db.Integer)
    minutos = db.Column(db.Integer)
    genero = db.Column(db.String(50))
    user_ID = db.Column(db.Integer, db.ForeignKey('users.id'))