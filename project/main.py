from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, validators
from wtforms.validators import InputRequired

from task import Task
from user import User

app = Flask(__name__)
auth = HTTPBasicAuth()

class RegistrationForm(FlaskForm):
    username = StringField('username')
    email = StringField('email')
    password = PasswordField('password')
    confirm = PasswordField('confirm')


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/register", methods = ["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    
    elif request.method == "POST":

        flashes = False

        # check if mail exists
        temp_user = User.find_by_email(request.form["email"])
        if temp_user:
            flash("Account with this email already exists!", "email")
            flashes = True

        # check if passwords match
        if User.hash_password(request.form["password"]) != User.hash_password(request.form["confirm"]):
            redirect("/")
            flashes = True

        if flashes == False:
            values = (
                None,
                request.form["username"],
                request.form["email"],
                User.hash_password(request.form["password"])
            )

            User(*values).create()
            user = User.find_by_email(request.form["email"])

            return redirect(url_for("show_profile", id = user.id))

        return redirect("/")


@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    
    elif request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.find_by_email(email)
                
        if user and user.verify_password(password):
            return redirect(url_for("show_profile", id = user.id))

        return redirect("/login")


@app.route("/profile/<int:id>")
def show_profile(id):
    user = User.find_by_id(id)
    return render_template("profile.html", user = user)
