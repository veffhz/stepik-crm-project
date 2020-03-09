from flask_admin.contrib.sqla import ModelView

from application.models import db, User, Group, Applicant


def init_admin(admin):
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Group, db.session))
    admin.add_view(ModelView(Applicant, db.session))
