from app import Base
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.database import Base

class PontoTuristico(Base):
    __tablename__ = "ponto_turistico"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), unique=True, index=True)
    descricao = Column(String(500))
    comentarios = relationship("Comentario", back_populates="ponto_turistico")

    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao



Base = SQLAlchemy()

class Exemplo(Base.Model):
    id = Base.Column(Base.Integer, primary_key=True)
    nome = Base.Column(Base.String(50))




class Usuario(Base.Model):
    __tablename__ = 'usuarios'

    id = Base.Column(Base.Integer, primary_key=True)
    nome = Base.Column(Base.String(100), nullable=False)
    email = Base.Column(Base.String(100), nullable=False, unique=True)
    senha = Base.Column(Base.String(255), nullable=False)

    def verificar_senha(self, senha):
        return check_password_hash(self.senha, senha)

    def __repr__(self):
        return '<Usuario %r>' % self.nome

class Comentario(Base.Model):
    __tablename__ = 'comentarios'

    id = Base.Column(Base.Integer, primary_key=True)
    texto = Base.Column(Base.Text, nullable=False)
    data = Base.Column(Base.DateTime, nullable=False, default=datetime.utcnow)
    usuario_id = Base.Column(Base.Integer, Base.ForeignKey('usuarios.id'), nullable=False)
    ponto_turistico_id = Base.Column(Base.Integer, Base.ForeignKey('pontos_turisticos.id'), nullable=False)

    usuario = Base.relationship('Usuario', backref=Base.backref('comentarios', lazy=True))
    ponto_turistico = Base.relationship('PontoTuristico', backref=Base.backref('comentarios', lazy=True))

    def __repr__(self):
        return '<Comentario %r>' % self.texto
