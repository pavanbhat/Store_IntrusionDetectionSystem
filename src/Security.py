from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=5, max=20)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=7, max=60)])
    login = SubmitField('Login')


class RegisterForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=5, max=20)])
    email = StringField('email', validators=[InputRequired(), Email(message="Invalid Email ID! Please try again..."),
                                             Length(max=60)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=7, max=60)])
    register = SubmitField('Register')
