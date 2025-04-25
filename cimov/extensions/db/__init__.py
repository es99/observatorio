from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
    db.init_app(app)
    
class DiagnosticoTerritorial(db.Model):
    __tablename__ = "territorios"
    id = db.Column(db.Integer, primary_key=True)
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