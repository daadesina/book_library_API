from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, InputRequired

class SignupClass(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    sign_up = SubmitField('Sign Up')


class LoginClass(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    log_in = SubmitField('Login')

class FileClass(FlaskForm):
    file = FileField('Image', validators=[InputRequired()])
    