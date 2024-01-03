from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class SignupForm(FlaskForm):
    username = StringField(label='Username')
    email = StringField(label='Email')
    password = StringField('Password')
    password2 = StringField('Confirm Password')
    submit = SubmitField("Submit")

