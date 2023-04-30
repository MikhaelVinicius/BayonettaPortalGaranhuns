from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

import jwt
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'mysql://Bayonetta:$Mika2023@127.0.0.1/bayo_portal_garanhuns_bd')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'chave-secreta')

Base = SQLAlchemy(app)

def token_required(f):
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'mensagem': 'Token não fornecido!'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            usuario_id = data['id']
        except:
            return jsonify({'mensagem': 'Token inválido ou expirado!'}), 401
        return f(usuario_id, *args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper


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
   nome = request.json.get('nome', '')
   descricao = request.json.get('descricao', '')
   localizacao = request.json.get('localizacao', '')
   imagem_url = request.json.get('imagem_url', '')

   novo_ponto_turistico = PontoTuristico(nome=nome, descricao=descricao, 
   localizacao=localizacao, imagem_url=imagem_url)
   Base.session.add(novo_ponto_turistico)
   Base.session.commit()
    
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
def cadastrar_comentario(usuario_id, id):
    ponto_turistico = PontoTuristico.query.get_or_404(id)
    
    comentario = Comentario(texto=request.json['texto'], usuario_id=usuario_id, ponto_turistico_id=id)
    Base.session.add(comentario)
    Base.session.commit()
    
    return jsonify({'mensagem': 'Comentário cadastrado com sucesso!'})

@app.route('/')
def index():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run()