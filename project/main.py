from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, EqualTo, Length, NoneOf, ValidationError
import os

from task import Task
from user import User

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

auth = HTTPBasicAuth()

def check_password(form, password):
    user = User.find_by_email(request.form["email"])               
    if not user or not user.verify_password(password.data):
        raise ValidationError("Incorrect Email or Password!")

class RegistrationForm(FlaskForm):
    username = StringField("username", [InputRequired(message = "Username is required!")])
    email = EmailField("email", [InputRequired(message = "Email is required"), NoneOf(User.all_emails(), message = "An account with this email address already exists!")])
    password = PasswordField("password", [InputRequired(message = "Password is required!"), Length(min = 8, message = "Password must be at least 8 characters!")])
    confirm = PasswordField("confirm", [EqualTo("password", message = "Passwords must match!")])

class LoginForm(FlaskForm):
    email = EmailField("email", [InputRequired(message = "Email is required!")])
    password = PasswordField("password", [InputRequired(message = "Password is required"), check_password])


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/register", methods = ["GET", "POST"])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():
        values = (
            None,
            request.form["username"],
            request.form["email"],
            User.hash_password(request.form["password"])
        )
        User(*values).create()
        user = User.find_by_email(request.form["email"])
        return redirect(url_for("show_profile", id = user.id))
    
    return render_template("register.html", form=form)


@app.route("/login", methods = ["GET", "POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        return redirect(url_for("show_profile", id = user.id))

    return render_template("login.html", form=form)


@app.route("/profile/<int:id>")
def show_profile(id):
    user = User.find_by_id(id)
    return render_template("profile.html", user = user)
