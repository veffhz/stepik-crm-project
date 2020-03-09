from enum import Enum

from sqlalchemy import event
from sqlalchemy_utils import ChoiceType
from werkzeug.security import generate_password_hash, check_password_hash

from application.extensions import db

GroupStatus = [
    ('enroll', 'набирается'),
    ('collected', 'набрана'),
    ('in_progress', 'идет'),
    ('archive', 'в архиве'),
]

ApplicantStatus = [
    ('new', 'новая'),
    ('processing', 'обрабатывается'),
    ('paid', 'оплачена'),
    ('distributed', 'распределена в группу'),
]

GroupCourse = Enum('GroupCourse', ['python', 'vue', 'django', 'php', 'html'])


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __str__(self):
        return f'{self.name}'


@event.listens_for(User.password, 'set', retval=True)
def hash_user_password(target, value, old_value, initiator):
    if value != old_value:
        return generate_password_hash(value)
    else:
        return old_value


class Group(db.Model):
    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    status = db.Column(ChoiceType(GroupStatus), nullable=False)
    course = db.Column(ChoiceType(GroupCourse, impl=db.Integer()), nullable=False)
    start = db.Column(db.DateTime, nullable=False)
    seats = db.Column(db.Integer)
    applicants = db.relationship("Applicant", back_populates="group", lazy='joined')

    def __str__(self):
        return f'{self.title}'


class Applicant(db.Model):
    __tablename__ = 'applicants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    status = db.Column(ChoiceType(ApplicantStatus), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey("groups.id"))
    group = db.relationship("Group", back_populates="applicants", lazy='joined')

    def __str__(self):
        return f'{self.name}'
