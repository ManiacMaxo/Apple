# python imports
from flask import Flask, render_template, request, redirect, url_for, session
from functools import wraps
import os

# imports from .py files
from user import User
from task import Task
from log_config import info_logger, error_logger
from form_config import check_password, RegistrationForm, LoginForm, TaskForm

# app config
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)

# require login config
def require_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # if there isn't a logged user
        if not session.get("SIGNED_IN"):
            return redirect('/login')
        return func(*args, **kwargs)
    return wrapper


# main page
@app.route("/")
def hello():
    return render_template("index.html")


# register page
@app.route("/register", methods = ["GET", "POST"])
def register():
    # defined in form_config.py
    form = RegistrationForm()

    # if form is valid
    if form.validate_on_submit():
        # get value and create user
        values = (
            None,
            request.form["username"],
            request.form["email"],
            User.hash_password(request.form["password"])
        )
        User(*values).create()

        # get the user and put him in the session
        user = User.find_by_email(request.form["email"])
        session["SIGNED_IN"] = True
        session["EMAIL"] = request.form["email"]

        # success log
        info_logger.info("%s registered successfully", request.form['email'])

        return redirect("/tasks")

    else:
        # error log
        if request.method == "POST":
            error_logger.error("%s failed to register", request.form["email"])
    
    # template the registration form
    return render_template("register.html", form = form)


# login page
@app.route("/login", methods = ["GET", "POST"])
def login():
    # defined in form_config.py
    form = LoginForm()

    # if form is valid
    if form.validate_on_submit():
        # get the user and put him in the session
        user = User.find_by_email(request.form["email"])
        session["SIGNED_IN"] = True
        session["EMAIL"] = request.form["email"]

        # success log
        info_logger.info("%s logined in successfully", request.form['email'])

        return redirect("/tasks")

    else:
        # error log
        if request.method == "POST":
            error_logger.error("%s failed to log in", request.form["email"])
    
    # template the login form
    return render_template("login.html", form = form)


# logout page
@app.route("/logout")
def logout():
    # success log
    info_logger.info("%s logged out successfully", session.get("EMAIL"))

    # remove user from the session
    session["SIGNED_IN"] = False
    session["EMAIL"] = None

    return redirect("/")


# edit user info
@app.route("/edit_profile/<int:id>")
@require_login
def edit_profile(id):
    # defined in form_config.py
    # same form is being used because the information and the input boxes are the same
    form = RegistrationForm()
    
    # get user, whose profile will be edited
    user = User.find_by_id(id)

    # set default username and email
    # email won't be able to be changed by the user
    form.username.data = user.username
    form.email.data = user.email

    # if form is valid
    if form.validate_on_submit():
        # get user info and save it
        user.username = request.form["username"]
        user.password = hash_password(request.form["password"])
        user.save()

        # success log
        info_logger.info("%s updated their profile successfully", request.form['email'])
        
        return redirect("/tasks")
    
    else:
        # error log
        if request.method == "POST":
            error_logger.error("%s failed to update their profile", request.form["email"])
    
    # template edit_profile form
    return render_template("edit_profile.html", form = form, user = user)

# page listing all tasks of a user
@app.route("/tasks")
@require_login
def show_tasks():
    # get user, whose tasks will be shown from session
    user = User.find_by_email(session.get("EMAIL"))

    # all to_do, in_progress and completed tasks are in one page for simplifying user's action
    all_to_do = Task.get_to_do(user.id)
    all_in_progress = Task.get_in_progress(user.id)
    all_completed = Task.get_completed(user.id)

    # template all tasks
    return render_template("tasks.html", 
        user = user, 
        all_to_do = all_to_do, 
        all_in_progress = all_in_progress, 
        all_completed = all_completed
    )


# page for creating new tasks
@app.route("/new_task", methods=["GET", "POST"])
@require_login
def create_new_task():
    # defined in form_config.py
    form = TaskForm()

    # get user, who is creating a new task
    user = User.find_by_email(session.get("EMAIL"))

    # if form is valid
    if form.validate_on_submit():
        # get values and create a task
        values = (
            None,
            request.form["title"],
            request.form["description"],
            request.form["deadline"],
            request.form["state"],
            user.id
        )
        print(values)
        Task(*values).create()

        # success log
        info_logger.info("Task with title %s created successfully", request.form["title"])
        
        return redirect("/tasks")
    
    # template new task form
    return render_template("new_task.html", user = user, form = form)


# page for editing tasks
@app.route("/edit_task/<int:id>", methods = ["GET", "POST"])
@require_login
def edit_task(id):
    # get task and the user who has the task
    task = Task.find_by_id(id)
    user = User.find_by_email(session.get("EMAIL"))

    # defined in form_config.py
    # same form as in new_task, because it is the same thing
    form = TaskForm(state = task.state)

    # if wrong user is logged, so he can't access other users' tasks
    if user.id != task.user_id:
        error_logger.error("Couldn't move with title %s couldn't be edited. Forbidden access", task.title)
        return redirect('/tasks')
    
    # get old task information
    form.title.data = task.title
    form.deadline.data = task.deadline
    form.description.data = task.description

    # if form is valid
    if form.validate_on_submit():
        # get new task information and save it
        task.state = request.form["state"]
        task.title = request.form["title"]
        task.deadline = request.form["deadline"]
        task.description = request.form["description"]
        task.save()

        # success log
        info_logger.info("Task with title %s edited successfully", request.form["title"])
        
        return redirect("/tasks")
    
    # template edit task form
    return render_template("edit_task.html", user = user, form = form, task = task)


# page for listing deleted tasks
@app.route("/deleted")
@require_login
def show_deleted():
    # get user from session and their deleted tasks
    # they are not on the same page as to_do, in_progress and completed, because it's not neaded
    user = User.find_by_email(session.get("EMAIL"))
    all_deleted = Task.get_deleted(user.id)
    
    # templated user's deleted tasks
    return render_template("deleted.html", user = user, all_deleted = all_deleted)


# page for recovering deleted tasks
@app.route("/edit_deleted_task/<int:id>")
@require_login
def edit_deleted_task(id):
    # get task and the user who has the task
    task = Task.find_by_id(id)
    user = User.find_by_email(session.get("EMAIL"))

    # if wrong user is logged, so he can't access other users' tasks
    if user.id != task.user_id:
        error_logger.error("Couldn't move with title %s couldn't be edited. Forbidden access", task.title)
        return redirect('/tasks')
    
    # get task information
    info = [task.title, task.deadline, task.description]

    # template edit task form
    return render_template("edit_deleted_task.html", user = user, info = info, task_id = task.id)