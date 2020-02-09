from enum import Enum

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import ChoiceType

db = SQLAlchemy()

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

GroupCourse = Enum('GroupCourse', 'python vue django php html')


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    mail = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)


class Group(db.Model):
    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    status = db.Column(ChoiceType(GroupStatus), nullable=False)
    course = db.Column(ChoiceType(GroupCourse, impl=db.Integer()), nullable=False)
    start = db.Column(db.DateTime, nullable=False)
    applicants = db.relationship("Applicant", back_populates="group")


class Applicant(db.Model):
    __tablename__ = 'applicants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    mail = db.Column(db.String(80), unique=True, nullable=False)
    status = db.Column(ChoiceType(ApplicantStatus), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey("groups.id"))
    group = db.relationship("Group", back_populates="applicants")
