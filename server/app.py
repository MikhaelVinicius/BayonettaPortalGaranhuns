from flask import Flask, jsonify, render_template
from flask_login import LoginManager
from flask import Flask, request

from flask_login import login_required
from flask_sqlalchemy import SQLAlchemy
import config
from flask_cors import CORS
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView






app = Flask(__name__)

CORS(app)
app.config.from_object(config)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://Bayonetta:$Mika2023@127.0.0.1/bayo_portal_garanhuns_bd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Bayonetta'
db = SQLAlchemy(app)

# definição do modelo de dados para pontos turísticos


class PontoTuristico(db.Model):
    __tablename__ = 'pontos_turisticos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(500), nullable=False)
    localizacao = db.Column(db.String(100), nullable=False)
    imagem_url = db.Column(db.String(255))

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'descricao': self.descricao,
            'localizacao': self.localizacao
        }




class Comentarios(db.Model):
    __tablename__ = 'comentarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    comentario = db.Column(db.Text, nullable=False)
    data_comentario = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp())
    
    def __repr__(self):
        return '<comentarios %r>' % self.nome
    
    
class Administradores(db.Model):
    __tablename__ = 'administradores'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(255), nullable=False)    
    
    def __repr__(self):
        return '<administradores %r>' % self.nome



# Rota para exibir todos os pontos turísticos em formato JSON
@app.route('/api/pontos_turisticos')
def listar_pontos_turisticos_json():
    pontos_turisticos = PontoTuristico.query.all()
    return jsonify([ponto_turistico.to_dict() for ponto_turistico in pontos_turisticos])


def validar_dados_ponto_turistico(dados):
    erros = {}

    # validar nome
    if not dados.get('nome'):
        erros['nome'] = 'Campo obrigatório.'

    # validar descrição
    if not dados.get('descricao'):
        erros['descricao'] = 'Campo obrigatório.'

    # validar localização
    if not dados.get('localizacao'):
        erros['localizacao'] = 'Campo obrigatório.'

    return erros


@app.route('/api/pontos_turisticos/novo', methods=['POST'])
@login_required
def adicionar_ponto_turistico():
    dados_ponto_turistico = request.json

    # validar dados do ponto turístico
    erros = validar_dados_ponto_turistico(dados_ponto_turistico)
    if erros:
        return jsonify({'erros': erros}), 400

    novo_ponto_turistico = PontoTuristico(
        nome=dados_ponto_turistico['nome'],
        descricao=dados_ponto_turistico['descricao'],
        localizacao=dados_ponto_turistico['localizacao'],
        imagem_url=dados_ponto_turistico['imagem_url']
    )

    db.session.add(novo_ponto_turistico)
    db.session.commit()

    return jsonify({'mensagem': 'Ponto turístico adicionado com sucesso!'})

@app.route('/api/pontos_turisticos/<int:id>', methods=['DELETE'])
@login_required
def excluir_ponto_turistico(id):
    ponto_turistico = PontoTuristico.query.get(id)

    if not ponto_turistico:
        return jsonify({'mensagem': 'Ponto turístico não encontrado!'}), 404

    db.session.delete(ponto_turistico)
    db.session.commit()

    return jsonify({'mensagem': 'Ponto turístico excluído com sucesso!'})


@app.route('/api/pontos_turisticos/<int:id>', methods=['PUT'])
@login_required
def editar_ponto_turistico(id):
    ponto_turistico = PontoTuristico.query.get(id)

    if not ponto_turistico:
        return jsonify({'mensagem': 'Ponto turístico não encontrado!'}), 404

    dados_ponto_turistico = request.json

    # validar dados do ponto turístico
    erros = validar_dados_ponto_turistico(dados_ponto_turistico)
    if erros:
        return jsonify({'erros': erros}), 400

    ponto_turistico.nome = dados_ponto_turistico['nome']
    ponto_turistico.descricao = dados_ponto_turistico['descricao']
    ponto_turistico.localizacao = dados_ponto_turistico['localizacao']
    ponto_turistico.imagem_url = dados_ponto_turistico['imagem_url']

    db.session.commit()

    return jsonify({'mensagem': 'Ponto turístico atualizado com sucesso!'})




#################################################

# Rota para exibir todos os pontos turísticos
@app.route('/')
def listar_pontos_turisticos():
    pontos_turisticos = PontoTuristico.query.all()
    return render_template('listar_pontos_turisticos.html', pontos_turisticos=pontos_turisticos)


# Rota para exibir os detalhes de um ponto turístico específico
@app.route('/ponto_turistico/<int:id>')
def exibir_ponto_turistico(id):
    ponto_turistico = PontoTuristico.query.get(id)
    return render_template('exibir_ponto_turistico.html', ponto_turistico=ponto_turistico)






# Rota para exibir todos os comentários
@app.route('/comentarios')
def listar_comentarios():
    comentarios = Comentarios.query.all()
    return render_template('listar_comentarios.html', comentarios=comentarios)


# Rota para exibir os detalhes de um comentário específico
@app.route('/comentario/<int:id>')
def exibir_comentario(id):
    comentario = Comentarios.query.get(id)
    return render_template('exibir_comentario.html', comentario=comentario)


# Rota para exibir todos os administradores
@app.route('/administradores')
def listar_administradores():
    administradores = Administradores.query.all()
    return render_template('listar_administradores.html', administradores=administradores)


# Rota para exibir os detalhes de um administrador específico
@app.route('/administrador/<int:id>')
def exibir_administrador(id):
    administrador = Administradores.query.get(id)
    return render_template('exibir_administrador.html', administrador=administrador)

admin = Admin(app, name='Admin', template_mode='bootstrap3')
admin.add_view(ModelView(PontoTuristico, db.session))

if __name__ == '__main__':
    app.config['DEBUG'] = True

    app.run()