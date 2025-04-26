from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from cimov.extensions.login import login_manager

db = SQLAlchemy()

def init_app(app):
    db.init_app(app)
    
class DiagnosticoTerritorial(db.Model):
    __tablename__ = "territorios"
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(120), index=True, unique=False)
    nome = db.Column(db.String(120), index=True, unique=False)
    bairro = db.Column(db.String(120), index=True, unique=False)
    qtd_familias = db.Column(db.Integer)
    tempo_ocupacao = db.Column(db.String(64), unique=False)
    infraestrutura_bas = db.Column(db.Text)
    risco_ambiental = db.Column(db.Text)
    risco_ambiental_outro = db.Column(db.String(120), index=True, unique=False)
    comunid_tradicional = db.Column(db.String(20), index=True, unique=False)
    impacto_grande_proj = db.Column(db.String(20), index=True, unique=False)
    qual_grande_projeto = db.Column(db.String(120), index=True, unique=False)
    existe_proc_judicial = db.Column(db.String(20), index=True, unique=False)
    num_proc_judicial = db.Column(db.String(120), index=True, unique=False)
    conhece_titular = db.Column(db.String(20), index=True, unique=False)
    titular = db.Column(db.String(120), index=True, unique=False)
    relatos_violencia = db.Column(db.String(20), index=True, unique=False)
    quais_relatos = db.Column(db.Text)
    ameacas_liderancas = db.Column(db.String(20), index=True, unique=False)
    quais_ameacas = db.Column(db.Text)
    relatos_violencia_adicionais = db.Column(db.Text)
    data = db.Column(db.String(64), index=True)
    
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    nome_completo = db.Column(db.String(64), unique=False, index=True)
    cpf = db.Column(db.String(20), unique=True, index=True)
    telefone = db.Column(db.String(20), unique=False, index=True)
    password_hash = db.Column(db.Text())
    
    @property
    def password(self):
        raise AttributeError('password is not readable attribute')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return '<User %r>' % self.username
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)