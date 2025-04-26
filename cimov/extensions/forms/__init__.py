from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, SelectMultipleField, TextAreaField, BooleanField, PasswordField
from wtforms.validators import DataRequired, InputRequired, Length, Email, EqualTo
from wtforms.widgets import ListWidget, CheckboxInput
from cimov.extensions.db import User
from wtforms import ValidationError

class MainForm(FlaskForm):
    nome_territorio = StringField('1. Nome do território atendido', validators=[DataRequired()])
    bairro_territorio = StringField('2. Bairro onde está localizado', validators=[DataRequired()])
    qtd_familias = IntegerField('3. Aproximadamente, quantas famílias vivem na área?')
    
    tempo_ocupacao = SelectField(
        '4. Há quanto tempo existe a ocupação?',
        choices=[
            ('menos_1', 'Menos de 1 ano'),
            ('1_5', '1 a 5 anos'),
            ('6_10', '6 a 10 anos'),
            ('mais_10', 'Mais de 10 anos')
        ],
    )
    
    infraestrutura = SelectMultipleField(
        '5. A comunidade é atendida por quais serviços de infraestrutura básica? (Marque os que existem)',
        choices=[
            ('esgoto', 'Esgotamento sanitário'),
            ('agua', 'Abastecimento de água'),
            ('energia', 'Energia elétrica'),
            ('iluminacao', 'Iluminação pública'),
            ('calcamento', 'Calçamento ou pavimentação'),
            ('nenhum', 'Nenhum')
        ],
        option_widget=CheckboxInput(),
        widget=ListWidget(prefix_label=False),
        validators=[InputRequired(message="Selecione pelo menos uma opção")]
    )
    
    risco_ambiental = SelectMultipleField(
        '6. A comunidade está localizada em área de risco ambiental? (Marque os que se aplicam)',
        choices=[
            ('deslizamento', 'Deslizamento de terra'),
            ('enchente', 'Enchente'),
            ('nenhum', 'Não se aplica'),
            ('outros', 'Outros (escreva no espaço abaixo)')
        ],
        option_widget=CheckboxInput(),
        widget=ListWidget(prefix_label=False),
        validators=[InputRequired(message="Selecione pelos menos uma opção")]
    )   
    risco_ambiental_outro = StringField('6.1 Risco ambiental que não esteja elencado acima')
    
    tradicional = SelectField(
        '7. A comunidade se reconhece como tradicional?',
        choices=[
            ('sim', 'Sim'),
            ('nao', 'Não'),
            ('nao_sabe_informar', 'Não sabe informar'),
        ],
    )
    
    impacto_grande_projeto = SelectField(
        '8. A área é impactada por algum grande projeto (ex: obras de infraestrutura urbana, polo turístico, etc.)?',
        choices=[
            ('sim', 'Sim'),
            ('nao', 'Não'),
        ],
    )
    
    impacto_grande_projeto_sim = StringField('8.1 Se sim, qual?')
    
    processo_judicial = SelectField(
        '9. A comunidade tem conhecimento da existência de processo judicial de reintegração de posse?',
        choices=[
            ('sim', 'Sim'),
            ('nao', 'Não')
        ],
    )
    
    processo_judicial_sim = StringField('9.1 Se sim, qual o número do processo (se souber)')
    
    conhece_titularidade = SelectField(
        '10. A comunidade conhece a titularidade da área ocupada?',
        choices=[
            ('sim', 'Sim'),
            ('nao', 'Não')
        ],
    )
    
    conhece_titularidade_sim = StringField('10.1 Se sim, quem é o/a proprietário/a ou órgão público responsável?')
    
    conflitos_fundiarios = SelectField(
        '11. Há relatos de violência relacionados a conflitos fundiários?',
        choices=[
            ('sim', 'Sim'),
            ('nao', 'Não')
        ],
    )
    
    conflitos_fundiarios_sim = TextAreaField('11.1 Se sim, quais?')
    
    ameacas = SelectField(
        '12. Há conhecimento de ameaças direcionadas às lideranças locais?',
        choices=[
            ('sim', 'Sim'),
            ('nao', 'Não')
        ],
    )
    
    ameacas_relatos = TextAreaField('12.1 Se sim, gostaria de relatar?')
    
    relatos_de_violencia = TextAreaField('13. Campo aberto para relatos adicionais sobre violências ou conflitos na comunidade')
    
    submit = SubmitField('Enviar')
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(message='Campo obrigatório!'),
        Length(min=1, max=64),
        Email(message='Formato de email inválido!')
    ])
    password = PasswordField('Senha', validators=[
        DataRequired(message='Campo obrigatório!'),
        Length(min=8, message='A senha deve ter pelo menos 8 caracteres')
    ])
    remember_me = BooleanField('Lembrar-me')
    
class RegistroForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(message='Campo obrigatório!'),
        Email(message='Formato de email inválido!')
    ])
    nome = StringField('Nome Completo', validators=[
        DataRequired(message='Campo obrigatório!')
    ])
    cpf = StringField('CPF', validators=[
        DataRequired(message='Campo obrigatório!'),
        Length(min=14, max=14)
    ])
    telefone = StringField('Tel', validators=[
        DataRequired(message='Campo obrigatório'),
        Length(min=8, max=15)
    ])
    password = PasswordField('Senha', validators=[
        DataRequired(message="Campo obrigatório!"),
        EqualTo('password2', message='As senhas devem ser iguais.')
    ])
    password2 = PasswordField('Confirme a senha', validators=[
        DataRequired(message="Campo obrigatório!")
    ])
    submit = SubmitField('Registrar')
    
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Este email já encontra-se registrado!')