from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, validators
from wtforms.fields.html5 import EmailField, DateField
from wtforms.validators import InputRequired, EqualTo, Length, NoneOf, ValidationError

from user import User

# check login password


def check_password(form, password):
    # get user trying to log in
    user = User.find_by_email(request.form["email"])

    # if user exists and his password is correct
    if not user or not user.verify_password(password.data):
        raise ValidationError("Incorrect Email or Password!")

# registration form


class RegistrationForm(FlaskForm):
    # username -> input type - string, required
    username = StringField("username", [InputRequired()])

    # email -> input type - email, required, unique
    email = EmailField("email", [InputRequired(), NoneOf(User.all_emails(
    ), message="An account with this email address already exists!")])

    # password -> input type - password, required, at least 8 characters long
    password = PasswordField("password", [InputRequired(), Length(
        min=8, message="Password must be at least 8 characters!")])

    # confirm -> input type - password, equal to password
    confirm = PasswordField(
        "confirm", [EqualTo("password", message="Passwords must match!")])

# edit profile form


class EditProfileForm(FlaskForm):
    # username -> input type - string, required
    username = StringField("username", [InputRequired()])

    # email -> input type - email, required, unique
    email = EmailField("email")

    # password -> input type - password, required, at least 8 characters long
    password = PasswordField("password", [InputRequired(), Length(
        min=8, message="Password must be at least 8 characters!")])

    # confirm -> input type - password, equal to password
    confirm = PasswordField(
        "confirm", [EqualTo("password", message="Passwords must match!")])

# login form


class LoginForm(FlaskForm):
    # email -> input type - email, required
    email = EmailField("email", [InputRequired(message="Email is required!")])

    # password -> input type - password, verification if password is correct in db
    password = PasswordField("password", [InputRequired(
        message="Password is required"), check_password])

# create task form


class TaskForm(FlaskForm):
    # title -> input type - string, required
    title = StringField("title", [InputRequired()])

    # decription -> input type - string, optional
    description = StringField("description")

    # deadline -> input type - string
    # the input type is string because every user has their own choice on how to set the deadline
    deadline = DateField("deadline", format='%Y-%m-%d')

    # state -> input type - select
    state = SelectField("state", choices=[
                        ('0', "To Do"), ('1', "In Progress"), ('2', "Completed"), ('3', "Deleted")])
