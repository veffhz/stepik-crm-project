from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email
from wtforms import StringField, SubmitField


class LoginForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()])
    password = StringField(validators=[InputRequired()])
    submit = SubmitField('submit')


class RequestForm(FlaskForm):
    name = StringField(validators=[InputRequired()])
    submit = SubmitField('request_submit')
