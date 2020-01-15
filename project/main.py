from flask import Flask
from flask import render_template, request, redirect, url_for, jsonify
from flask_httpauth import HTTPBasicAuth

from task import Task
from user import User

app = Flask(__name__)
auth = HTTPBasicAuth()


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    
    elif request.method == 'POST':
        values = (
            None,
            request.form['username'],
            request.form['email'],
            User.hash_password(request.form['password'])
        )
        User(*values).create()
        user = User.find_by_email(request.form['email'])

        return url_for('show_profile', user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    elif request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.find_by_email(email)
        
        if user and user.verify_password(password):
            return redirect('/profile')
        
        return url_for('show_profile', user=user)


@app.route('/profile')
def show_profile(user):
    return render_template('profile.html', user=user)
