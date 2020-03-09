from flask import url_for, request
from flask_admin import AdminIndexView, expose, Admin
from flask_login import current_user, login_required
from flask_admin.contrib.sqla import ModelView
from werkzeug.utils import redirect
from wtforms import ValidationError

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


class ApplicantView(ModelView):
    def group_limit(form, field):
        if field.data.is_complete:
            raise ValidationError('Group limit exceeded!')

    form_args = dict(
        group=dict(validators=[group_limit])
    )


class DashboardView(AdminIndexView):

    @login_required
    @expose('/')
    def index(self):
        applicants = Applicant.query.all()
        new_applicants = [applicant for applicant in applicants
                          if applicant.status == 'new']
        groups = Group.query.all()

        applicants_data = {
            'new_applicants': new_applicants,
            'length': len(applicants),
            'news': len(new_applicants),
            'diff': len(applicants) - len(new_applicants)
        }

        return self.render('admin_dashboard.html', groups=groups,
                           applicants_data=applicants_data)


def init_admin(app):
    admin_manager = Admin(app, index_view=DashboardView(name='Главная'), name='Stepik CRM')
    admin_manager.add_view(UserView(User, db.session, name='Пользователи'))
    admin_manager.add_view(ModelView(Group, db.session, name='Группы'))
    admin_manager.add_view(ApplicantView(Applicant, db.session, name='Заявки'))
    return admin_manager
