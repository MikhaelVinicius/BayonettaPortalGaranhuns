from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import config
app = Flask(__name__)


app.config.from_object(config)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://Bayonetta:$Mika2023@127.0.0.1/bayo_portal_garanhuns_bd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# definição do modelo de dados para pontos turísticos
class PontoTuristico(db.Model):
    __tablename__ = 'pontos_turisticos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.Text)
    localizacao = db.Column(db.String(255))
    imagem_url = db.Column(db.String(255))

    def __repr__(self):
        return '<PontoTuristico %r>' % self.nome


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


if __name__ == '__main__':
    app.run()