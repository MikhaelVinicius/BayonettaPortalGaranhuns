from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

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


db.metadata.create_all(engine)


novo_ponto_turistico = PontosTuristicos(nome='Novo Ponto Turistico', descricao='Descricao do novo ponto turistico', localizacao='Localizacao do novo ponto turistico', imagem_url='http://imagem.com.br')

session.add(novo_ponto_turistico)
session.commit()
