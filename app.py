from flask import Flask, render_template, request, flash, redirect, session, g, abort
from models import db, connect_db, User, Job
from forms import NewUserForm, LoginForm
from sqlalchemy.exc import IntegrityError
import os

CURR_USER_KEY = "curr_user"

app = Flask(__name__)

CURR_USER_KEY = "curr_user"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'postgresql:///psopayscale2')
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', '12345678')


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
                image_url=form.image_url.data or None)

            # db.session.add(user)
            db.session.commit()

            # session["user_id"] = user.id

        except IntegrityError:
            flash("Username already taken", 'danger')
            return render_template('new_user.html', form=form)

        do_login(user)

        return redirect("/login")

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
            return redirect("/home")

        flash("Invalid credentials.", 'danger')

    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    """Handle logout of user."""

    do_logout()
    flash("Goodbye for now!", "success")
    return redirect("/")


@app.route("/user/info/<int:user_id>", methods=["GET"])
def user_page(user_id):
    user = User.query.get_or_404(user_id)
    image_url = user.image_url
    return render_template('user_info.html',  user=user, image_url=image_url)

@app.route("/users/<int:user_id>/edit")
def edit_user(user_id):
    """Show edit form"""
    user = User.query.get_or_404(user_id)
    return render_template("edit_user.html", user=user)


@app.route('/users/<int:user_id>/edit', methods=["POST"])
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

    return redirect("/user/info/<int:user_id>")


#### HOME ROUTES ####
@app.route("/")
def enterpage():
    data = open('index.html').read()    
    return data

@app.route("/home")
def homepage():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/login")

    return render_template('index2.html')

@app.route("/about")
def aboutpage():
    return render_template('about.html')

@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 Page"""

    return render_template('404.html'), 404
# @app.route("/regions")
# def aboutpage():
#     return render_template('regions.html')


#### JOBS ROUTES #####













#### INITIAL ROUTES ####
@app.route("/ocean/01", methods=["GET"])
def ocean1_page():
    return render_template('/initial_routes/square01.html')
    
@app.route("/ocean/02", methods=["GET"])
def ocean2_page():
    return render_template('/initial_routes/square02.html')

@app.route("/ocean/03", methods=["GET"])
def ocean3_page():
    return render_template('/initial_routes/square03.html')

@app.route("/ocean/04", methods=["GET"])
def ocean4_page():
    return render_template('/initial_routes/square04.html')

@app.route("/ocean/05", methods=["GET"])
def ocean5_page():
    return render_template('/initial_routes/square05.html')

@app.route("/ocean/06", methods=["GET"])
def ocean6_page():
    return render_template('/initial_routes/square06.html')

@app.route("/ocean/07", methods=["GET"])
def ocean7_page():
    return render_template('/initial_routes/square07.html')

@app.route("/ocean/08", methods=["GET"])
def ocean8_page():
    return render_template('/initial_routes/square08.html')

@app.route("/ocean/09", methods=["GET"])
def ocean9_page():
    return render_template('/initial_routes/square09.html')

@app.route("/ocean/10", methods=["GET"])
def ocean10_page():
    return render_template('/initial_routes/square10.html')

@app.route("/ocean/11", methods=["GET"])
def ocean11_page():
    return render_template('/initial_routes/square11.html')

@app.route("/ocean/12", methods=["GET"])
def ocean12_page():
    return render_template('/initial_routes/square12.html')

@app.route("/ocean/13", methods=["GET"])
def ocean13_page():
    return render_template('/initial_routes/square13.html')

@app.route("/ocean/14", methods=["GET"])
def ocean14_page():
    return render_template('/initial_routes/square14.html')

@app.route("/ocean/15", methods=["GET"])
def ocean15_page():
    return render_template('/initial_routes/square15.html')

@app.route("/ocean/16", methods=["GET"])
def ocean16_page():
    return render_template('/initial_routes/square16.html')
    
@app.route("/ocean/17", methods=["GET"])
def ocean17_page():
    return render_template('/initial_routes/square17.html')

@app.route("/ocean/18", methods=["GET"])
def ocean18_page():
    return render_template('/initial_routes/square18.html')

@app.route("/ocean/19", methods=["GET"])
def ocean19_page():
    return render_template('/initial_routes/square19.html')

@app.route("/ocean/20", methods=["GET"])
def ocean20_page():
    return render_template('/initial_routes/square20.html')

@app.route("/ocean/21", methods=["GET"])
def ocean21_page():
    return render_template('/initial_routes/square21.html')

@app.route("/ocean/22", methods=["GET"])
def ocean22_page():
    return render_template('/initial_routes/square22.html')

@app.route("/ocean/23", methods=["GET"])
def ocean23_page():
    return render_template('/initial_routes/square23.html')

@app.route("/ocean/24", methods=["GET"])
def ocean24_page():
    return render_template('/initial_routes/square24.html')

@app.route("/ocean/25", methods=["GET"])
def ocean25_page():
    return render_template('/initial_routes/square25.html')

@app.route("/ocean/26", methods=["GET"])
def ocean26_page():
    return render_template('/initial_routes/square26.html')

@app.route("/ocean/27", methods=["GET"])
def ocean27_page():
    return render_template('/initial_routes/square27.html')

@app.route("/ocean/28", methods=["GET"])
def ocean28_page():
    return render_template('/initial_routes/square28.html')

@app.route("/ocean/29", methods=["GET"])
def ocean29_page():
    return render_template('/initial_routes/square29.html')

@app.route("/ocean/30", methods=["GET"])
def ocean30_page():
    return render_template('/initial_routes/square30.html')

@app.route("/ocean/31", methods=["GET"])
def ocean31_page():
    return render_template('/initial_routes/square31.html')

@app.route("/ocean/32", methods=["GET"])
def ocean32_page():
    return render_template('/initial_routes/square32.html')


#### INDIVIDUAL COUNTRIES ROUTES ####
@app.route("/alaska", methods=["GET"])
def alaska():
    return render_template('/countries/alaska.html')
