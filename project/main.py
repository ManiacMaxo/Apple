from flask import Flask
from flask import render_template, request, redirect, url_for, jsonify
import json

from task import Task
from user import User

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('../front-end/index.html')


@app.route('/tasks')
def list_posts():
    return render_template('../front-end/lists.html', tasks=Task.all())