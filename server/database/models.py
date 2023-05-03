from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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
    
    
 
class Atividade(db.Model):
    __tablename__ = 'atividades'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.Text)
    localizacao = db.Column(db.String(255))
    imagem_url = db.Column(db.String(255))      
    
    
    def __repr__(self):
        return '<Atividade %r>' % self.nome 
 
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
    
    def __repr__(self):
        return '<Hotel %r>' % self.nome      


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