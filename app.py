from flask import Flask, render_template, request, flash, redirect, session, g, abort
from models import db, connect_db, User, Job, DEFAULT_IMG
from forms import NewUserForm, LoginForm, AddJobForm, EditUserForm, EditJobForm
from sqlalchemy.exc import IntegrityError
from secrets import API_KEY
import os
import requests
import pdb
from helpers import COUNTRIES

CURR_USER_KEY = "curr_user"


app = Flask(__name__)
from routes import *
app.register_blueprint(routes)


CURR_USER_KEY = "curr_user"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'postgresql:///psopayscale2')
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', '12345678')
app.config['API_KEY'] = os.environ.get('API_KEY', 'none')

connect_db(app)
db.create_all()
# toolbar = DebugToolbarExtension(app)


#### USERS ROUTES #####
@app.before_request
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""

    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])

    else:
        g.user = None

def do_login(user):
    """Log in user."""

    session[CURR_USER_KEY] = user.id

def do_logout():
    """Logout user."""

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]

@app.route("/user/new", methods=["GET"])
def users_new_form():
    """Show a form to create a new user"""
    form= NewUserForm()

    return render_template('new_user.html', form=form)

@app.route("/user/new", methods=["POST"])
def add_user():

    form = NewUserForm()

    if form.validate_on_submit():
        try:
            user = User.signup(
                user_name=form.user_name.data,
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                email=form.email.data,
                password=form.password.data,
                image_url=DEFAULT_IMG)   #form.image_url.data or None)

            # db.session.add(user)
            db.session.commit()

            # session["user_id"] = user.id

        except IntegrityError:
            flash("Username already taken", 'danger')
            return render_template('new_user.html', form=form)

        do_login(user)

        return redirect(f"/user/{user.id}")

    else:
        return render_template('new_user.html', form=form)

    return redirect('/home')
    # return redirect('/user/info/<int:user_id>')

@app.route('/user/login', methods=["GET", "POST"])
def login():
    """Handle user login."""

    form = LoginForm()

    if form.validate_on_submit():
        user = User.authenticate(form.user_name.data,
                                 form.password.data)

        if user:
            do_login(user)
            flash(f"Hello, {user.user_name}!", "success")
            return redirect(f"/user/{user.id}")

        flash("Invalid credentials.", 'danger')

    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    """Handle logout of user."""

    do_logout()
    flash("Goodbye for now!", "success")
    return redirect("/")


@app.route("/user/<int:user_id>", methods=["GET"])
def user_page(user_id):
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")

    user = User.query.get_or_404(user_id)
    jobs = (Job.query.filter(Job.user_id == user_id).all())

    return render_template('user_info.html', user=user, image=user.image_url, jobs=jobs)

@app.route("/user/<int:user_id>/edit")
def edit_user(user_id):
    """Show edit form"""
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    user = User.query.get(g.user.id)
    form = EditUserForm(obj=user)

    return render_template("edit_user.html", user=user, form=form)


@app.route('/user/<int:user_id>/edit', methods=["POST"])
def submit_edit(user_id):
    """Edit a user"""

    user = User.query.get_or_404(user_id)
    user_name=request.form["user_name"]
    first_name=request.form["first_name"]
    last_name=request.form["last_name"]
    email=request.form["email"]
    image_url=request.form['image_url']

    db.session.add(user)
    db.session.commit()

    return redirect(f"/user/{user.id}")


@app.route('/user/delete', methods=["POST"])
def delete_user():
    """Delete user."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    do_logout()

    db.session.delete(g.user)
    db.session.commit()

    return redirect("/")


#### HOME ROUTES ####
@app.route("/")
def enterpage():
    data = open('index.html').read()    
    return data

@app.route("/home")
def homepage():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/user/login")

    return render_template('index2.html')

@app.route("/about")
def aboutpage():
    return render_template('about.html')

@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 Page"""

    return render_template('404.html')

@app.route("/list")
def countrylist():
    """list of countries for easier searching not using the map"""
    
    return render_template('list.html', COUNTRIES=COUNTRIES)

#### JOBS ROUTES #####

@app.route("/user/<int:user_id>/addjob", methods=["GET"])
def new_job(user_id):
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")

    user = User.query.get_or_404(user_id)
    form = AddJobForm()

    return render_template('add_job.html', user=user, form=form)

@app.route("/user/<int:user_id>/addjob", methods=["POST"])
def submit_job(user_id):

    user = User.query.get_or_404(user_id)
    form = AddJobForm()

    if form.validate_on_submit():
        job_title = form.job_title.data
        location = form.location.data
        start_year = form.start_year.data
        day_rate = form.day_rate.data
        cont_company = form.cont_company.data
        user_id = f"{user.id}"

        job= Job(job_title=job_title, location=location, start_year=start_year, day_rate=day_rate, cont_company=cont_company, user_id=user_id)

        db.session.add(job)
        db.session.commit()

        return redirect(f"/user/{user.id}")
    
    return render_template('add_job.html', form=form)

@app.route("/job/<int:job_id>/editjob", methods=["GET"])
def edit_job(job_id):
    """Show edit form"""
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")

    job = Job.query.get_or_404(job_id)
    form = EditJobForm(obj=job)
    user = User.query.get_or_404(g.user.id)
    return render_template("edit_job.html", user=user, job=job, form=form)

@app.route("/job/<int:job_id>/editjob", methods=["POST"])
def submit_edit_job(job_id):
    job = Job.query.get_or_404(job_id)
    form = EditJobForm()
    user = User.query.get_or_404(g.user.id)

    if form.validate_on_submit():
        job_title = form.job_title.data
        location = form.location.data
        start_year = form.start_year.data
        day_rate = form.day_rate.data
        cont_company = form.cont_company.data
        user_id = f"{user.id}"

        job= Job(job_title=job_title, location=location, start_year=start_year, day_rate=day_rate, cont_company=cont_company, user_id=user_id)

        db.session.add(job)
        db.session.commit()

        return redirect(f"/user/{user.id}")



@app.route('/job/<int:job_id>/delete', methods=["POST"])
def submit_job_edit(job_id):
 
    job = Job.query.get_or_404(job_id)
    if job.user_id != g.user.id:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    db.session.delete(job)
    db.session.commit()

    return redirect(f"/user/{g.user.id}")


##############################################################################
# Turn off all caching in Flask
#   (useful for dev; in production, this kind of stuff is typically
#   handled elsewhere)


@app.after_request
def add_header(req):
    """Add non-caching headers on every request."""

    req.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    req.headers["Pragma"] = "no-cache"
    req.headers["Expires"] = "0"
    req.headers['Cache-Control'] = 'public, max-age=0'
    return req
