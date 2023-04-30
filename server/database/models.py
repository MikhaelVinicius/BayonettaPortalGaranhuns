from database import db

class PontoTuristico(db.Model):
    __tablename__ = 'pontos_turisticos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.Text)
    localizacao = db.Column(db.String(255))
    imagem_url = db.Column(db.String(255))

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Exemplo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
