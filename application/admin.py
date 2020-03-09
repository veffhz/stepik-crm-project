from flask import url_for, request
from flask_login import current_user
from flask_admin.contrib.sqla import ModelView
from werkzeug.utils import redirect

from application.models import db, User, Group, Applicant


class AdminView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login', next=request.url))


class UserView(AdminView):
    column_exclude_list = ['password']
    column_searchable_list = ['name', 'email']

    form_widget_args = {
        'password': {
            'type': 'password'
        }
    }


def init_admin(admin):
    admin.add_view(UserView(User, db.session))
    admin.add_view(ModelView(Group, db.session))
    admin.add_view(ModelView(Applicant, db.session))
