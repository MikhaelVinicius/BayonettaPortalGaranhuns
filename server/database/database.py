from sqlalchemy import create_engine, Column, Integer, String, Text,Float, TIMESTAMP
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
    descricao = Column(String(10000))

    localizacao = Column(String(255))
    imagem_url = Column(String(255))
    

class Atividade(db):
    __tablename__ = 'atividades'

    id = Column(Integer, primary_key=True)
    nome = Column(String(255), nullable=False)
    descricao = Column(Text)
    localizacao = Column(String(255))
    imagem_url = Column(String(255))    
    
class Hotel(db):
    __tablename__ = 'hotel'

    id = Column(Integer, primary_key=True, autoincrement=True)
    imagem_url = Column(String(255))
    name = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)
    state = Column(String(255), nullable=False)
    country = Column(String(255), nullable=False)
    rating = Column(Float, default=0.0)
    website = Column(String(255))
    email = Column(String(255))
    phone = Column(String(20))
    created_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP', nullable=False)
    updated_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP', nullable=False)    
    
class Restaurante(db):
    __tablename__ = 'restaurantes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    endereco = Column(String(255), nullable=False)
    cidade = Column(String(255), nullable=False)
    estado = Column(String(255), nullable=False)
    telefone = Column(String(255), nullable=False)
    imagem_url = Column(String(255), nullable=False)


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
