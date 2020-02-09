from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from wtforms import StringField, SubmitField


class BookingForm(FlaskForm):
    name = StringField(validators=[InputRequired()])
    submit = SubmitField('booking_submit')


class RequestForm(FlaskForm):
    name = StringField(validators=[InputRequired()])
    submit = SubmitField('request_submit')
