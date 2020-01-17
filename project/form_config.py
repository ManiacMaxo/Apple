from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, EqualTo, Length, NoneOf, ValidationError

from user import User

def check_password(form, password):
    user = User.find_by_email(request.form["email"])               
    if not user or not user.verify_password(password.data):
        raise ValidationError("Incorrect Email or Password!")


class RegistrationForm(FlaskForm):
    username = StringField("username", [InputRequired()])
    email = EmailField("email", [InputRequired(), NoneOf(User.all_emails(), message = "An account with this email address already exists!")])
    password = PasswordField("password", [InputRequired(), Length(min = 8, message = "Password must be at least 8 characters!")])
    confirm = PasswordField("confirm", [EqualTo("password", message = "Passwords must match!")])


class LoginForm(FlaskForm):
    email = EmailField("email", [InputRequired(message = "Email is required!")])
    password = PasswordField("password", [InputRequired(message = "Password is required"), check_password])


class TaskForm(FlaskForm):
    title = StringField("title", [InputRequired()])
    date = StringField("date")
    description = StringField("description") 