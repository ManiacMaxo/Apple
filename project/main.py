from flask import Flask, render_template, request, redirect, url_for, session
from functools import wraps
import os

from user import User
from task import Task
from log_config import info_logger, error_logger
from form_config import check_password, RegistrationForm, LoginForm, TaskForm

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

def require_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not session.get("SIGNED_IN"):
            return redirect('/login')
        return func(*args, **kwargs)
    return wrapper


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
        info_logger.info("%s registered successfully", request.form['email'])
        return redirect("/tasks")
    else:
        if request.method == "POST":
            error_logger.error("%s failed to register", request.form["email"])
    
    return render_template("register.html", form = form)


@app.route("/login", methods = ["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.find_by_email(request.form["email"])
        session["SIGNED_IN"] = True
        session["EMAIL"] = request.form["email"]
        info_logger.info("%s logined in successfully", request.form['email'])
        return redirect("/tasks")
    else:
        if request.method == "POST":
            error_logger.error("%s failed to log in", request.form["email"])
    
    return render_template("login.html", form = form)

@app.route("/logout")
def logout():
    info_logger.info("%s logged out successfully", session.get("EMAIL"))
    session["SIGNED_IN"] = False
    session["EMAIL"] = None
    return redirect("/")


@app.route("/tasks")
@require_login
def show_tasks():
    user = User.find_by_email(session.get("EMAIL"))
    all_to_do = Task.get_to_do(user.id)
    all_in_progress = Task.get_in_progress(user.id)
    all_completed = Task.get_completed(user.id)
    return render_template("tasks.html", 
        user = user, 
        all_to_do = all_to_do, 
        all_in_progress = all_in_progress, 
        all_completed = all_completed
    )


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
        info_logger.info("Task with title %s created successfully", request.form["title"])
        return redirect("/tasks")
    
    return render_template("new_task.html", user = user, form = form)


@app.route("/edit_task/<int:id>", methods = ["GET", "POST"])
@require_login
def edit_task(id):
    task = Task.find_by_id(id)
    form = TaskForm()
    user = User.find_by_email(session.get("EMAIL"))

    if user.id != task.user_id:
        return redirect("/login")

    form.title.data = task.title
    form.date.data = task.date
    form.description.data = task.description

    if form.validate_on_submit():
        task.title = request.form["title"]
        task.date = request.form["date"]
        task.description = request.form["description"]
        task.save()
        info_logger.info("Task with title %s edited successfully", request.form["title"])
        return redirect("/tasks")
    
    return render_template("edit_task.html", user = user, form = form, task_id = task.id)

@app.route("/deleted")
@require_login
def show_deleted():
    user = User.find_by_email(session.get("EMAIL"))
    all_deleted = Task.get_deleted(user.id)
    return render_template("deleted.html", 
        user = user, 
        all_deleted = all_deleted
    )


@app.route("/to_do/<int:id>")
@require_login
def to_do(id):
    task = Task.find_by_id(id)
    user = User.find_by_email(session.get("EMAIL"))
    if user.id != task.user_id:
        error_logger.error("Couldn't move task with title %s to to_do. Forbidden access", task.title)
        return redirect("/login")

    task.move_to_to_do()
    info_logger.info("Task with title %s moved to to_do successfully", task.title)
    return redirect("/tasks")


@app.route("/in_progress/<int:id>")
@require_login
def in_progress(id):
    task = Task.find_by_id(id)
    user = User.find_by_email(session.get("EMAIL"))
    if user.id != task.user_id:
        error_logger.error("Couldn't move task with title %s to in_progress. Forbidden access", task.title)
        return redirect("/login")

    task.move_to_in_progress()
    info_logger.info("Task with title %s moved to in_progress successfully", task.title)
    return redirect("/tasks")


@app.route("/completed/<int:id>")
@require_login
def completed(id):
    task = Task.find_by_id(id)
    user = User.find_by_email(session.get("EMAIL"))
    if user.id != task.user_id:
        error_logger.error("Couldn't move task with title %s to completed. Forbidden access", task.title)
        return redirect("/login")

    task.move_to_completed()
    info_logger.info("Task with title %s moved to completed successfully", task.title)
    return redirect("/tasks")


@app.route("/deleted/<int:id>")
@require_login
def deleted(id):
    task = Task.find_by_id(id)
    user = User.find_by_email(session.get("EMAIL"))
    if user.id != task.user_id:
        error_logger.error("Couldn't move task with title %s to deleted. Forbidden access", task.title)
        return redirect("/login")

    task.move_to_deleted()
    info_logger.info("Task with title %s moved to deleted successfully", task.title)
    return redirect("/tasks")
