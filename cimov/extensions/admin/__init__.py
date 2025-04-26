from flask_admin import Admin
from flask import redirect, url_for, request
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from cimov.extensions.db import db, User, DiagnosticoTerritorial

admin = Admin(name='Bancos de dados - CIMOV')


class TerritoriosView(ModelView):
    can_delete = False
    can_edit = False
    can_create = False
    can_view_details = True

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login', next=request.url))


class UserView(ModelView):
    can_delete = True
    can_edit = True
    can_create = False
    can_view_details = True

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login', next=request.url))


admin.add_view(UserView(User, db.session))
admin.add_view(TerritoriosView(DiagnosticoTerritorial, db.session))


def init_app(app):
    admin.init_app(app)
