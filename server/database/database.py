from sqlalchemy import create_engine, Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from database.models import db, PontoTuristico

engine = create_engine('mysql://Bayonetta:$Mika2023@127.0.0.1/bayo_portal_garanhuns_bd')
Session = sessionmaker(bind=engine)
session = Session()

db = declarative_base()


class PontosTuristicos(db):
    __tablename__ = 'pontos_turisticos'

    id = Column(Integer, primary_key=True)
    nome = Column(String(255), nullable=False)
    descricao = Column(Text)
    localizacao = Column(String(255))
    imagem_url = Column(String(255))
    

class Atividade(db):
    __tablename__ = 'atividades'

    id = Column(Integer, primary_key=True)
    nome = Column(String(255), nullable=False)
    descricao = Column(Text)
    localizacao = Column(String(255))
    imagem_url = Column(String(255))    


class Comentarios(db):
    __tablename__ = 'comentarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    comentario = Column(Text, nullable=False)
    data_comentario = Column(TIMESTAMP, nullable=False, server_default=db.func.current_timestamp())


class Administradores(db):
    __tablename__ = 'administradores'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    senha = Column(String(255), nullable=False)


db.metadata.create_all(engine)
