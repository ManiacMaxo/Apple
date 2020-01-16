from flask import Flask, render_template, request, redirect, url_for, session
from flask_httpauth import HTTPBasicAuth
from flask_wtf import FlaskForm
from functools import wraps
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

def require_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not session.get("SIGNED_IN"):
            return redirect('/login')
        return func(*args, **kwargs)
    return wrapper

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
        session["SIGNED_IN"] = True
        session["EMAIL"] = request.form["email"]
        return redirect("/tasks")
    
    return render_template("register.html", form = form)


@app.route("/login", methods = ["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.find_by_email(request.form["email"])
        session["SIGNED_IN"] = True
        session["EMAIL"] = request.form["email"]
        return redirect("/tasks")

    return render_template("login.html", form = form)

@app.route("/logout")
def logout():
    session["SIGNED_IN"] = False
    session["EMAIL"] = None
    return redirect("/")

@app.route("/tasks")
@require_login
def show_tasks():
    user = User.find_by_email(session.get("EMAIL"))
    all_to_do = Task.get_to_do(user.id)
    return render_template("tasks.html", user = user, all_to_do = all_to_do)

@app.route("/new_task", methods=["GET", "POST"])
@require_login
def create_new_task():
    form = TaskForm()
    user = User.find_by_email(session.get("EMAIL"))

    if form.validate_on_submit():
        values = (
            None,
            request.form["title"],
            request.form["date"],
            request.form["description"],
            0,
            user.id
        )
        Task(*values).create()
        return redirect("/tasks")

    return render_template("new_task.html", user = user, form = form)

