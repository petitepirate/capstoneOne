from flask import Flask, render_template, request, flash, redirect, session, g, abort
from models import db, connect_db, User, Job
from forms import NewUserForm, LoginForm, AddJobForm, EditUserForm
from sqlalchemy.exc import IntegrityError
from secrets import API_KEY
import os
import requests
import pdb

CURR_USER_KEY = "curr_user"
BASE_API_URL = "https://api.tugo.com/v1/travelsafe/countries/"

app = Flask(__name__)

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
                image_url=form.image_url.data or None)

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
        return redirect("/")

    user = User.query.get_or_404(user_id)
    jobs = (Job.query.filter(Job.user_id == user_id).all())

    return render_template('user_info.html', user=user, image=user.image_url, jobs=jobs)

@app.route("/user/<int:user_id>/edit")
def edit_user(user_id):
    """Show edit form"""
    form = EditUserForm()
    user = User.query.get_or_404(user_id)
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


#### HOME ROUTES ####
@app.route("/")
def enterpage():
    data = open('index.html').read()    
    return data

@app.route("/home")
def homepage():

    # if not g.user:
    #     flash("Access unauthorized.", "danger")
    #     return redirect("/user/login")

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







#### INITIAL ROUTES ####
@app.route("/region/01", methods=["GET"])
def region1_page():
    """single entry page - reroute to that country"""

    return redirect("/alaska")
    
@app.route("/region/02", methods=["GET"])
def region2_page():
    """single entry page - reroute to that country"""

    return redirect("/canada")

@app.route("/region/03", methods=["GET"])
def region3_page():


    return render_template('/initial_routes/square03.html')

@app.route("/region/04", methods=["GET"])
def region4_page():


    return render_template('/initial_routes/square04.html')

@app.route("/region/05", methods=["GET"])
def region5_page():


    return render_template('/initial_routes/square05.html')

@app.route("/region/06", methods=["GET"])
def region6_page():


    return render_template('/initial_routes/square06.html')

@app.route("/region/07", methods=["GET"])
def region7_page():


    return render_template('/initial_routes/square07.html')

@app.route("/region/08", methods=["GET"])
def region8_page():


    return redirect("/russia")

@app.route("/region/09", methods=["GET"])
def region9_page():


    return render_template('/initial_routes/square09.html')

@app.route("/region/10", methods=["GET"])
def region10_page():


    return render_template('/initial_routes/square10.html')

@app.route("/region/11", methods=["GET"])
def region11_page():


    return render_template('/initial_routes/square11.html')

@app.route("/region/12", methods=["GET"])
def region12_page():


    return render_template('/initial_routes/square12.html')

@app.route("/region/13", methods=["GET"])
def region13_page():


    return render_template('/initial_routes/square13.html')

@app.route("/region/14", methods=["GET"])
def region14_page():


    return redirect("/home")

@app.route("/region/15", methods=["GET"])
def region15_page():


    return render_template('/initial_routes/square15.html')

@app.route("/region/16", methods=["GET"])
def region16_page():


    return render_template('/initial_routes/square16.html')
    
@app.route("/region/17", methods=["GET"])
def region17_page():


    return render_template('/initial_routes/square17.html')

@app.route("/region/18", methods=["GET"])
def region18_page():


    return render_template('/initial_routes/square18.html')

@app.route("/region/19", methods=["GET"])
def region19_page():


    return render_template('/initial_routes/square19.html')

@app.route("/region/20", methods=["GET"])
def region20_page():


    return render_template('/initial_routes/square20.html')

@app.route("/region/21", methods=["GET"])
def region21_page():


    return render_template('/initial_routes/square21.html')

@app.route("/region/22", methods=["GET"])
def region22_page():


    return render_template('/initial_routes/square22.html')

@app.route("/region/23", methods=["GET"])
def region23_page():


    return render_template('/initial_routes/square23.html')

@app.route("/region/24", methods=["GET"])
def region24_page():


    return render_template('/initial_routes/square24.html')

@app.route("/region/25", methods=["GET"])
def region25_page():


    return redirect("/home")

@app.route("/region/26", methods=["GET"])
def region26_page():


    return render_template('/initial_routes/square26.html')

@app.route("/region/27", methods=["GET"])
def region27_page():


    return render_template('/initial_routes/square27.html')

@app.route("/region/28", methods=["GET"])
def region28_page():


    return render_template('/initial_routes/square28.html')

@app.route("/region/29", methods=["GET"])
def region29_page():


    return render_template('/initial_routes/square29.html')

@app.route("/region/30", methods=["GET"])
def region30_page():


    return redirect("/home")

@app.route("/region/31", methods=["GET"])
def region31_page():


    return render_template('/initial_routes/square31.html')

@app.route("/region/32", methods=["GET"])
def region32_page():


    return render_template('/initial_routes/square32.html')


#### INDIVIDUAL COUNTRIES ROUTES ####
#### EXAMPLE ####
@app.route("/areastats", methods=["GET"])
def areastats():
    # user = User.query.get_or_404(user_id)   

    # if not g.user:
    #     flash("Access unauthorized.", "danger")
    #     return redirect("/home")
    country = 'ZM'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
  

    jobs = (Job.query.filter(Job.location == 'Antarctica').all())
    # pam = (Job.query.filter(Job.location == 'Antartica', Job.job_title == 'PAM').all())


    return render_template('areastat.html', jobs=jobs, advisory=advisory) 
##############################################################

@app.route("/alaska", methods=["GET"])
def alaska():
    jobs = (Job.query.filter(Job.location == "Alaska").all())
    return render_template('/countries/alaska.html', jobs=jobs)

@app.route("/angola", methods=["GET"])
def angola():
    jobs = (Job.query.filter(Job.location == "Angola").all())
    return render_template('/countries/angola.html', jobs=jobs)

@app.route("/antarctica", methods=["GET"])
def antarctica():
    jobs = (Job.query.filter(Job.location == "Antarctica").all())
    return render_template('/countries/antarctic.html', jobs=jobs)

@app.route("/arctic_ocean", methods=["GET"])
def arctic_ocean():
    jobs = (Job.query.filter(Job.location == "Arctic Ocean").all())
    return render_template('/countries/arctic_ocean.html', jobs=jobs)

@app.route("/argentina", methods=["GET"])
def argentina():
    jobs = (Job.query.filter(Job.location == "Argentina").all())
    return render_template('/countries/argentina.html', jobs=jobs)

@app.route("/australia_newzealand", methods=["GET"])
def australia_newzealand():
    jobs = (Job.query.filter(Job.location == "Australia / New Zealand").all())
    return render_template('/countries/australia_newzealand.html', jobs=jobs)

@app.route("/black_sea", methods=["GET"])
def black_sea():
    jobs = (Job.query.filter(Job.location == "Black Sea").all())
    return render_template('/countries/black_sea.html', jobs=jobs)

@app.route("/brazil", methods=["GET"])
def brazil():
    jobs = (Job.query.filter(Job.location == "Brazil").all())
    return render_template('/countries/brazil.html', jobs=jobs)

@app.route("/california", methods=["GET"])
def california():
    jobs = (Job.query.filter(Job.location == "California").all())
    return render_template('/countries/california.html', jobs=jobs)

@app.route("/canada", methods=["GET"])
def canada():
    jobs = (Job.query.filter(Job.location == "Canada").all())
    return render_template('/countries/canada.html', jobs=jobs)

@app.route("/caribbean", methods=["GET"])
def caribbean():
    jobs = (Job.query.filter(Job.location == "Caribbean").all())
    return render_template('/countries/caribbean.html', jobs=jobs)

@app.route("/caspian_sea", methods=["GET"])
def caspian_sea():
    jobs = (Job.query.filter(Job.location == "Caspian Sea").all())
    return render_template('/countries/caspian_sea.html', jobs=jobs)

@app.route("/chile", methods=["GET"])
def chile():
    jobs = (Job.query.filter(Job.location == "Chile").all())
    return render_template('/countries/chile.html', jobs=jobs)

@app.route("/china_vietnam", methods=["GET"])
def china_vietnam():
    jobs = (Job.query.filter(Job.location == "China / Vietnam").all())
    return render_template('/countries/china_vietnam.html', jobs=jobs)

@app.route("/columbia", methods=["GET"])
def columbia():
    jobs = (Job.query.filter(Job.location == "Columbia").all())
    return render_template('/countries/columbia.html', jobs=jobs)

@app.route("/ecuador", methods=["GET"])
def ecuador():
    jobs = (Job.query.filter(Job.location == "Ecuador").all())
    return render_template('/countries/ecuador.html', jobs=jobs)

@app.route("/ethiopia", methods=["GET"])
def ethiopia():
    jobs = (Job.query.filter(Job.location == "Ethiopia").all())
    return render_template('/countries/ethiopia.html', jobs=jobs)

@app.route("/falkland_islands", methods=["GET"])
def falkland_islands():
    jobs = (Job.query.filter(Job.location == "Falkland Islands").all())
    return render_template('/countries/falkland_islands.html', jobs=jobs)

@app.route("/french_guiana", methods=["GET"])
def french_guiana():
    jobs = (Job.query.filter(Job.location == "French Guiana").all())
    return render_template('/countries/french_guiana.html', jobs=jobs)

@app.route("/gabon", methods=["GET"])
def gabon():
    jobs = (Job.query.filter(Job.location == "Gabon").all())
    return render_template('/countries/gabon.html', jobs=jobs)

@app.route("/ghana", methods=["GET"])
def ghana():
    jobs = (Job.query.filter(Job.location == "Ghana").all())
    return render_template('/countries/ghana.html', jobs=jobs)

@app.route("/greenland", methods=["GET"])
def greenland():
    jobs = (Job.query.filter(Job.location == "Greenland").all())
    return render_template('/countries/greenland.html', jobs=jobs)

@app.route("/gulf_of_mexico", methods=["GET"])
def gulf_of_mexico():
    jobs = (Job.query.filter(Job.location == "Gulf of Mexico").all())
    return render_template('/countries/gulf_of_mexico.html', jobs=jobs)

@app.route("/guyana", methods=["GET"])
def guyana():
    jobs = (Job.query.filter(Job.location == "Guyana").all())
    return render_template('/countries/guyana.html', jobs=jobs)

@app.route("/hawaii", methods=["GET"])
def hawaii():
    jobs = (Job.query.filter(Job.location == "Hawaii").all())
    return render_template('/countries/hawaii.html', jobs=jobs)

@app.route("/iceland", methods=["GET"])
def iceland():
    jobs = (Job.query.filter(Job.location == "Iceland").all())
    return render_template('/countries/iceland.html', jobs=jobs)

@app.route("/india_srilanka", methods=["GET"])
def india_srilanka():
    jobs = (Job.query.filter(Job.location == "India / Sri Lanka").all())
    return render_template('/countries/india_srilanka.html', jobs=jobs)

@app.route("/indonesia", methods=["GET"])
def indonesia():
    jobs = (Job.query.filter(Job.location == "Indonesia").all())
    return render_template('/countries/indonesia.html', jobs=jobs)

@app.route("/madagascar", methods=["GET"])
def madagascar():
    jobs = (Job.query.filter(Job.location == "Madagascar").all())
    return render_template('/countries/madagascar.html', jobs=jobs)

@app.route("/malaysia", methods=["GET"])
def malaysia():
    jobs = (Job.query.filter(Job.location == "Malaysia").all())
    return render_template('/countries/malaysia.html', jobs=jobs)

@app.route("/mauritania", methods=["GET"])
def mauritania():
    jobs = (Job.query.filter(Job.location == "Mauritania").all())
    return render_template('/countries/mauritania.html', jobs=jobs)

@app.route("/mediterranean", methods=["GET"])
def mediterranean():
    jobs = (Job.query.filter(Job.location == "Mediterranean Sea").all())
    return render_template('/countries/mediterranean.html', jobs=jobs)

@app.route("/mexico", methods=["GET"])
def mexico():
    jobs = (Job.query.filter(Job.location == "Mexico (Pacific)").all())
    return render_template('/countries/mexico.html', jobs=jobs)

@app.route("/mozambique", methods=["GET"])
def mozambique():
    jobs = (Job.query.filter(Job.location == "Mozambique").all())
    return render_template('/countries/mozambique.html', jobs=jobs)

@app.route("/namibia", methods=["GET"])
def namibia():
    jobs = (Job.query.filter(Job.location == "Namibia").all())
    return render_template('/countries/namibia.html', jobs=jobs)

@app.route("/nigeria", methods=["GET"])
def nigeria():
    jobs = (Job.query.filter(Job.location == "Nigeria").all())
    return render_template('/countries/nigeria.html', jobs=jobs)

@app.route("/north_atlantic", methods=["GET"])
def north_atlantic():
    jobs = (Job.query.filter(Job.location == "US East Coast (N. Atlantic Ocean)").all())
    return render_template('/countries/north_atlantic.html', jobs=jobs)

@app.route("/north_sea", methods=["GET"])
def north_sea():
    jobs = (Job.query.filter(Job.location == "North Sea").all())
    return render_template('/countries/north_sea.html', jobs=jobs)

@app.route("/nw_africa_morocco", methods=["GET"])
def nw_africa_morocco():
    jobs = (Job.query.filter(Job.location == "NW Africa / Morocco").all())
    return render_template('/countries/nw_africa_morocco.html', jobs=jobs)

@app.route("/persian_gulf", methods=["GET"])
def persian_gulf():
    jobs = (Job.query.filter(Job.location == "Persian Gulf").all())
    return render_template('/countries/persian_gulf.html', jobs=jobs)

@app.route("/peru", methods=["GET"])
def peru():
    jobs = (Job.query.filter(Job.location == "Peru").all())
    return render_template('/countries/peru.html', jobs=jobs)

@app.route("/philippines", methods=["GET"])
def philippines():
    jobs = (Job.query.filter(Job.location == "Philippines").all())
    return render_template('/countries/philippines.html', jobs=jobs)

@app.route("/russia", methods=["GET"])
def russia():
    jobs = (Job.query.filter(Job.location == "Russia").all())
    return render_template('/countries/russia.html', jobs=jobs)

@app.route("/s_china", methods=["GET"])
def s_china():
    jobs = (Job.query.filter(Job.location == "Southern China").all())
    return render_template('/countries/s_china.html', jobs=jobs)

@app.route("/sierra_leone", methods=["GET"])
def sierra_leone():
    jobs = (Job.query.filter(Job.location == "Sierra Leone").all())
    return render_template('/countries/sierra_leone.html', jobs=jobs)

@app.route("/skorea_japan", methods=["GET"])
def skorea_japan():
    jobs = (Job.query.filter(Job.location == "S. Korea / Japan").all())
    return render_template('/countries/skorea_japan.html', jobs=jobs)

@app.route("/somalia", methods=["GET"])
def somalia():
    jobs = (Job.query.filter(Job.location == "Somalia").all())
    return render_template('/countries/somalia.html', jobs=jobs)

@app.route("/south_africa", methods=["GET"])
def south_africa():
    jobs = (Job.query.filter(Job.location == "South Africa").all())
    return render_template('/countries/south_africa.html', jobs=jobs)

@app.route("/suriname", methods=["GET"])
def suriname():
    jobs = (Job.query.filter(Job.location == "Suriname").all())
    return render_template('/countries/suriname.html', jobs=jobs)

@app.route("/uruguay", methods=["GET"])
def uruguay():
    jobs = (Job.query.filter(Job.location == "Uruguay").all())
    return render_template('/countries/uruguay.html', jobs=jobs)














##############################################################################
# Turn off all caching in Flask
#   (useful for dev; in production, this kind of stuff is typically
#   handled elsewhere)
#
# https://stackoverflow.com/questions/34066804/disabling-caching-in-flask

@app.after_request
def add_header(req):
    """Add non-caching headers on every request."""

    req.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    req.headers["Pragma"] = "no-cache"
    req.headers["Expires"] = "0"
    req.headers['Cache-Control'] = 'public, max-age=0'
    return req
