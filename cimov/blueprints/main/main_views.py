from flask import Blueprint, render_template
from cimov.extensions.forms import MainForm

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = MainForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)