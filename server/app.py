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

#####################CLASSES#############################
class PontoTuristico(db.Model):
    __tablename__ = 'pontos_turisticos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(10000), nullable=False)
    localizacao = db.Column(db.String(100), nullable=False)
    imagem_url = db.Column(db.String(255))

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'descricao': self.descricao,
            'localizacao': self.localizacao,
            'imagem_url': self.imagem_url
        }


class Atividade(db.Model):
    __tablename__ = 'atividades'
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
            'localizacao': self.localizacao,
            'imagem_url': self.imagem_url
        }

class Hotel(db.Model):
    __tablename__ = 'hotel'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(255), nullable=False)
    country = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Float, default=0.0)
    website = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    created_at = db.Column(db.TIMESTAMP, server_default='CURRENT_TIMESTAMP', nullable=False)
    updated_at = db.Column(db.TIMESTAMP, server_default='CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP', nullable=False)  
    imagem_url = db.Column(db.String(255))
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'country': self.country,
            'rating': self.rating,
            'website': self.website,
            'email': self.email,
            'phone': self.phone,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
            'imagem_url': self.imagem_url
        }


class Restaurante(db.Model):
    __tablename__ = 'restaurantes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
    endereco = db.Column(db.String(255), nullable=False)
    cidade = db.Column(db.String(255), nullable=False)
    estado = db.Column(db.String(255), nullable=False)
    telefone = db.Column(db.String(255), nullable=False)
    imagem_url = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'endereco': self.endereco,
            'cidade': self.cidade,
            'estado': self.estado,
            'telefone': self.telefone,
            'imagem_url': self.imagem_url
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

##########################RotasJson##################################


##PONTOS TURISTICOS
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
        
    if not dados.get('imagem_url'):
        erros['imagem_url'] = "imagem_url"    

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


###ATIVIDADES

@app.route('/api/atividades')
def listar_atividades_json():
    atividades = Atividade.query.all()
    return jsonify([atividade.to_dict() for atividade in atividades])

def validar_dados_atividade(dados):
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
    
    if not dados.get('imagem_url'):
       erros['imagem_url'] = "imagem_url"    

    return erros

@app.route('/api/atividades/nova', methods=['POST'])
@login_required
def adicionar_atividade():
    dados_atividade = request.json
    # validar dados da atividade
    erros = validar_dados_atividade(dados_atividade)
    if erros:
       return jsonify({'erros': erros}), 400

    nova_atividade = Atividade(
         nome=dados_atividade['nome'],
         descricao=dados_atividade['descricao'],
         localizacao=dados_atividade['localizacao'],
         imagem_url=dados_atividade['imagem_url']
)

    db.session.add(nova_atividade)
    db.session.commit()

    return jsonify({'mensagem': 'Atividade adicionada com sucesso!'})


@app.route('/api/atividades/int:id', methods=['DELETE'])
@login_required
def excluir_atividade(id):
  atividade = Atividade.query.get(id)
   
  if not atividade:
    return jsonify({'mensagem': 'Atividade não encontrada!'}), 404

  db.session.delete(atividade)
  db.session.commit()

  return jsonify({'mensagem': 'Atividade excluída com sucesso!'})


@app.route('/api/atividades/int:id', methods=['PUT'])
@login_required
def editar_atividade(id):
   atividade = Atividade.query.get(id)
   
   if not atividade:
    return jsonify({'mensagem': 'Atividade não encontrada!'}), 404

   dados_atividade = request.json

# validar dados da atividade
   erros = validar_dados_atividade(dados_atividade)
   if erros:
    return jsonify({'erros': erros}), 400

   atividade.nome = dados_atividade['nome']
   atividade.descricao = dados_atividade['descricao']
   atividade.localizacao = dados_atividade['localizacao']
   atividade.imagem_url = dados_atividade['imagem_url']

   db.session.commit()

   return jsonify({'mensagem': 'Atividade atualizada com sucesso!'})


##### Hotel

@app.route('/api/hoteis')
def listar_hoteis_json():
    hoteis = Hotel.query.all()
    return jsonify([hotel.to_dict() for hotel in hoteis])

def validar_dados_hotel(dados):
    erros = {}

    # validar nome
    if not dados.get('name'):
        erros['name'] = 'Campo obrigatório.'

    # validar endereço
    if not dados.get('address'):
        erros['address'] = 'Campo obrigatório.'

    # validar cidade
    if not dados.get('city'):
        erros['city'] = 'Campo obrigatório.'

    # validar estado
    if not dados.get('state'):
        erros['state'] = 'Campo obrigatório.'

    # validar país
    if not dados.get('country'):
        erros['country'] = 'Campo obrigatório.'

    # validar número de telefone
    if not dados.get('phone'):
        erros['phone'] = 'Campo obrigatório.'
    
    if not dados.get('imagem_url'):
        erros['imagem_url'] = "imagem_url"       

    return erros

@app.route('/api/hoteis/novo', methods=['POST'])
@login_required
def adicionar_hotel():
    dados_hotel = request.json

    # validar dados do hotel
    erros = validar_dados_hotel(dados_hotel)
    if erros:
        return jsonify({'erros': erros}), 400

    novo_hotel = Hotel(
        name=dados_hotel['name'],
        address=dados_hotel['address'],
        city=dados_hotel['city'],
        state=dados_hotel['state'],
        country=dados_hotel['country'],
        rating=dados_hotel.get('rating', 0.0),
        website=dados_hotel.get('website'),
        email=dados_hotel.get('email'),
        phone=dados_hotel['phone'],
        imagem_url = dados_hotel['imagem_url']
    )

    db.session.add(novo_hotel)
    db.session.commit()

    return jsonify({'mensagem': 'Hotel adicionado com sucesso!'})

@app.route('/api/hoteis/<int:id>', methods=['DELETE'])
@login_required
def excluir_hotel(id):
    hotel = Hotel.query.get(id)

    if not hotel:
        return jsonify({'mensagem': 'Hotel não encontrado!'}), 404

    db.session.delete(hotel)
    db.session.commit()

    return jsonify({'mensagem': 'Hotel excluído com sucesso!'})


@app.route('/api/hoteis/<int:id>', methods=['PUT'])
@login_required
def editar_hotel(id):
    hotel = Hotel.query.get(id)

    if not hotel:
        return jsonify({'mensagem': 'Hotel não encontrado!'}), 404

    dados_hotel = request.json

    # validar dados do hotel
    erros = validar_dados_hotel(dados_hotel)
    if erros:
        return jsonify({'erros': erros}), 400

    hotel.name = dados_hotel['name']
    hotel.address = dados_hotel['address']
    hotel.city = dados_hotel['city']
    hotel.state = dados_hotel['state']
    hotel.country = dados_hotel['country']
    hotel.rating = dados_hotel.get('rating', 0.0)
    hotel.website = dados_hotel.get('website')
    hotel.email = dados_hotel.get('email')
    hotel.phone = dados_hotel['phone'],
    hotel.imagem_url = dados_hotel['imagem_url']

    db.session.commit()

    return jsonify({'mensagem': 'Hotel atualizado com sucesso!'})

####Restaurantes

@app.route('/api/restaurantes')
def listar_restaurantes():
    restaurantes = Restaurante.query.all()
    return jsonify([restaurante.to_dict() for restaurante in restaurantes])

def validar_dados_restaurante(dados):
    erros = {}

    if not dados.get('nome'):
        erros['nome'] = 'Campo obrigatório.'

    if not dados.get('endereco'):
        erros['endereco'] = 'Campo obrigatório.'

    if not dados.get('cidade'):
        erros['cidade'] = 'Campo obrigatório.'
        
    if not dados.get('estado'):
        erros['estado'] = 'Campo obrigatório.'
    
    if not dados.get('telefone'):
        erros['telefone'] = 'Campo obrigatório.'
        
    if not dados.get('imagem_url'):
        erros['imagem_url'] = "imagem_url"    

    return erros

@app.route('/api/restaurantes/novo', methods=['POST'])
@login_required
def adicionar_restaurante():
    dados_restaurante = request.json

    erros = validar_dados_restaurante(dados_restaurante)
    if erros:
        return jsonify({'erros': erros}), 400

    novo_restaurante = Restaurante(
        nome=dados_restaurante['nome'],
        endereco=dados_restaurante['endereco'],
        cidade=dados_restaurante['cidade'],
        estado=dados_restaurante['estado'],
        telefone=dados_restaurante['telefone'],
        imagem_url=dados_restaurante['imagem_url']
    )

    db.session.add(novo_restaurante)
    db.session.commit()

    return jsonify({'mensagem': 'Restaurante adicionado com sucesso!'})

@app.route('/api/restaurantes/<int:id>', methods=['DELETE'])
@login_required
def excluir_restaurante(id):
    restaurante = Restaurante.query.get(id)

    if not restaurante:
        return jsonify({'mensagem': 'Restaurante não encontrado!'}), 404

    db.session.delete(restaurante)
    db.session.commit()

    return jsonify({'mensagem': 'Restaurante excluído com sucesso!'})


@app.route('/api/restaurantes/<int:id>', methods=['PUT'])
@login_required
def editar_restaurante(id):
    restaurante = Restaurante.query.get(id)

    if not restaurante:
        return jsonify({'mensagem': 'Restaurante não encontrado!'}), 404

    dados_restaurante = request.json

    erros = validar_dados_restaurante(dados_restaurante)
    if erros:
        return jsonify({'erros': erros}), 400

    restaurante.nome = dados_restaurante['nome']
    restaurante.endereco = dados_restaurante['endereco']
    restaurante.cidade = dados_restaurante['cidade']
    restaurante.estado = dados_restaurante['estado']
    restaurante.telefone = dados_restaurante['telefone']
    restaurante.imagem_url = dados_restaurante['imagem_url']

    db.session.commit()

    return jsonify({'mensagem': 'Restaurante atualizado com sucesso!'})



#####################RotasTemplate############################

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
admin.add_view(ModelView(Atividade, db.session))
admin.add_view(ModelView(Hotel, db.session))
admin.add_view(ModelView(Restaurante, db.session))

if __name__ == '__main__':
    app.config['DEBUG'] = True

    app.run()