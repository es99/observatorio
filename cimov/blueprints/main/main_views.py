from flask import Blueprint, render_template, redirect, url_for, flash, request
from cimov.extensions.forms import MainForm

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    form = MainForm()
    
    print(f"\n{'='*50}")
    print(f"Method: {request.method}")
    print(f"Form data: {request.form}")
    
    if form.validate_on_submit():
        print("\n=== FORMULÁRIO VÁLIDO ===")
        print(f"Nome: {form.nome_territorio.data}")
        print(f"Bairro: {form.bairro_territorio.data}")
        flash('Formulário enviado com sucesso!', 'success')
        return redirect(url_for('main.index'))
    
    elif request.method == 'POST':
        print("\n=== ERROS DE VALIDAÇÃO ===")
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Erro no campo {getattr(form, field).label.text}: {error}", 'danger')
    
    return render_template('index.html', form=form)