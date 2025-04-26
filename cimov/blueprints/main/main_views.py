from flask import Blueprint, render_template, redirect, url_for, flash, request
from cimov.extensions.db import db, DiagnosticoTerritorial
from cimov.extensions.forms import MainForm
from datetime import date, datetime
from flask_login import login_required, current_user
import json

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = MainForm()
    if form.validate_on_submit():
        d = datetime.now()
        data = d.strftime("%d-%m-%Y - %H:%M")
        nome = form.nome_territorio.data
        bairro = form.bairro_territorio.data
        qtd_familias = form.qtd_familias.data
        tempo_ocupacao = form.tempo_ocupacao.data
        infra_basica = json.dumps(form.infraestrutura.data)
        risco_ambiental = json.dumps(form.risco_ambiental.data)
        risco_ambiental_outro = form.risco_ambiental_outro.data
        comun_tradicional = form.tradicional.data
        impacto_grand_proj = form.impacto_grande_projeto.data
        grande_projeto = form.impacto_grande_projeto_sim.data
        processo_jud = form.processo_judicial.data
        num_proc_judicial = form.processo_judicial_sim.data
        titular = form.conhece_titularidade.data
        qual_titular = form.conhece_titularidade_sim.data
        violencia = form.conflitos_fundiarios.data
        relato_violencia = form.conflitos_fundiarios_sim.data
        ameacas_liderancas = form.ameacas.data
        qual_ameaca = form.ameacas_relatos.data
        rel_adicionais = form.relatos_de_violencia.data
        formulario = DiagnosticoTerritorial(nome=nome, bairro=bairro, qtd_familias=qtd_familias, tempo_ocupacao=tempo_ocupacao,
                infraestrutura_bas=infra_basica, risco_ambiental=risco_ambiental, risco_ambiental_outro=risco_ambiental_outro,
                comunid_tradicional=comun_tradicional, impacto_grande_proj=impacto_grand_proj, qual_grande_projeto=grande_projeto,
                existe_proc_judicial=processo_jud, num_proc_judicial=num_proc_judicial, conhece_titular=titular,
                titular=qual_titular, relatos_violencia=violencia, quais_relatos=relato_violencia,
                ameacas_liderancas=ameacas_liderancas, quais_ameacas=qual_ameaca, relatos_violencia_adicionais=rel_adicionais,
                data=data, usuario=current_user.nome_completo)
        db.session.add(formulario)
        db.session.commit()
        flash('Formulário enviado com sucesso!', 'success')
        return redirect(url_for('main.index'))
    
    elif request.method == 'POST':
        print("\n=== ERROS DE VALIDAÇÃO ===")
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Erro no campo {getattr(form, field).label.text}: {error}", 'danger')
    
    return render_template('index.html', form=form)