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

@app.route('/?id=register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('index.html', id = "register")
    elif request.method == 'POST':
        values = (
            None,
            request.form['username'],
            User.hash_password(request.form['password'])
        )
        User(*values).create()

        return redirect('/')


@auth.verify_password
def verify_password(username, password):
    user = User.find_by_username(username)
    if user:
        return user.verify_password(password)

    return False



@app.route('/tasks')
def list_posts():
    return render_template('lists.html', tasks=Task.all())