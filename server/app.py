from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import json
from database.models import PontoTuristico




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://Bayonetta:$Mika2023@127.0.0.1/bayo_portal_garanhuns_bd'
db = SQLAlchemy(app)


@app.route('/pontos_turisticos', methods=['GET'])
def obter_pontos_turisticos():
    pontos_turisticos = PontoTuristico.query.all()
    resultado = []
    for ponto_turistico in pontos_turisticos:
        resultado.append({
            'id': ponto_turistico.id,
            'nome': ponto_turistico.nome,
            'descricao': ponto_turistico.descricao,
            'localizacao': ponto_turistico.localizacao,
            'imagem_url': ponto_turistico.imagem_url
        })
    return jsonify(resultado)

@app.route('/pontos_turisticos', methods=['POST'])
def cadastrar_ponto_turistico():
    nome = request.json['nome']
    descricao = request.json['descricao']
    localizacao = request.json['localizacao']
    imagem_url = request.json['imagem_url']
    
    novo_ponto_turistico = PontoTuristico(nome=nome, descricao=descricao, localizacao=localizacao, imagem_url=imagem_url)
    db.session.add(novo_ponto_turistico)
    db.session.commit()
    
    return jsonify({'mensagem': 'Ponto turístico cadastrado com sucesso!'})


@app.route('/pontos_turisticos', methods=['POST'])
def cadastrar_ponto_turistico():
    nome = request.json['nome']
    descricao = request.json['descricao']
    localizacao = request.json['localizacao']
    imagem_url = request.json['imagem_url']
    
    novo_ponto_turistico = PontoTuristico(nome=nome, descricao=descricao, localizacao=localizacao, imagem_url=imagem_url)
    db.session.add(novo_ponto_turistico)
    db.session.commit()
    
    return jsonify({'mensagem': 'Ponto turístico cadastrado com sucesso!'})


@app.route('/login', methods=['POST'])
def login():
    email = request.json['email']
    senha = request.json['senha']
    
    usuario = Usuario.query.filter_by(email=email).first()
    
    if not usuario or not usuario.verificar_senha(senha):
        return jsonify({'mensagem': 'Email ou senha incorretos!'}), 401
    
    token = jwt.encode({'id': usuario.id}, app.config['SECRET_KEY'])
    
    return jsonify({'token': token.decode('utf-8')})

@app.route('/pontos_turisticos/<int:id>/comentarios', methods=['POST'])
@token_required
def cadastrar_comentario(id):
    ponto_turistico = PontoTuristico.query.get_or_404(id)
    
    comentario = Comentario(texto=request.json['texto'], usuario_id=g.usuario_id, ponto_turistico_id=id)
    db.session.add(comentario)
    db.session.commit()
    
    return jsonify({'mensagem': 'Comentário cadastrado com sucesso!'})
