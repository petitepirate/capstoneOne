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

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
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
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'ZM'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]

    jobs = (Job.query.filter(Job.location == "Alaska").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/angola", methods=["GET"])
def angola():
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'AO'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]

    jobs = (Job.query.filter(Job.location == "Angola").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/antarctica", methods=["GET"])
def antarctica():
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'AQ'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]

    jobs = (Job.query.filter(Job.location == "Antarctica").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/arctic_ocean", methods=["GET"])
def arctic_ocean():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'GL'  # No real country code for arctic - uses greenland since thats the likely launching place
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "Arctic Ocean").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/argentina", methods=["GET"])
def argentina():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'AR'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "Argentina").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/australia_newzealand", methods=["GET"])
def australia_newzealand():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'AU'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "Australia / New Zealand").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/black_sea", methods=["GET"])
def black_sea():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'TR'  #uses Turkey
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "Black Sea").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/brazil", methods=["GET"])
def brazil():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'BR'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "Brazil").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/california", methods=["GET"])
def california():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'US'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "California").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/canada", methods=["GET"])
def canada():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'US' #App is a canadian travel app and so doesnt have canadian advisories since that is their home country
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "Canada").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/caribbean", methods=["GET"])
def caribbean():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'BS'  #uses Bahamas 
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "Caribbean").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/caspian_sea", methods=["GET"])
def caspian_sea():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'IR'  #uses Iran
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "Caspian Sea").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/chile", methods=["GET"])
def chile():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'CL'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "Chile").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/china_vietnam", methods=["GET"])
def china_vietnam():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'CN'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "China / Vietnam").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/columbia", methods=["GET"])
def columbia():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'CO'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "Columbia").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/ecuador", methods=["GET"])
def ecuador():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'EC'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "Ecuador").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/ethiopia", methods=["GET"])
def ethiopia():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'ET'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "Ethiopia").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/falkland_islands", methods=["GET"])
def falkland_islands():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'FK'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "Falkland Islands").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/french_guiana", methods=["GET"])
def french_guiana():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'GF'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "French Guiana").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/gabon", methods=["GET"])
def gabon():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'GA'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "Gabon").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/ghana", methods=["GET"])
def ghana():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'GH'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "Ghana").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/greenland", methods=["GET"])
def greenland():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'GL'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "Greenland").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/gulf_of_mexico", methods=["GET"])
def gulf_of_mexico():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'US'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "Gulf of Mexico").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/guyana", methods=["GET"])
def guyana():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'GY'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "Guyana").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/hawaii", methods=["GET"])
def hawaii():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'US'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "Hawaii").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/iceland", methods=["GET"])
def iceland():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'IS'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "Iceland").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/india_srilanka", methods=["GET"])
def india_srilanka():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'IN'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "India / Sri Lanka").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/indonesia", methods=["GET"])
def indonesia():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'ID'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "Indonesia").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/madagascar", methods=["GET"])
def madagascar():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'MG'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "Madagascar").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/malaysia", methods=["GET"])
def malaysia():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'MY'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "Malaysia").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/mauritania", methods=["GET"])
def mauritania():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'MR'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "Mauritania").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/mediterranean", methods=["GET"])
def mediterranean():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'EG' #uses egypt
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "Mediterranean Sea").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/mexico", methods=["GET"])
def mexico():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'MX'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "Mexico (Pacific)").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/mozambique", methods=["GET"])
def mozambique():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'MZ'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "Mozambique").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/namibia", methods=["GET"])
def namibia():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'NA'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "Namibia").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/nigeria", methods=["GET"])
def nigeria():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'NG'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "Nigeria").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/north_atlantic", methods=["GET"])
def north_atlantic():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'US'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "US East Coast (N. Atlantic Ocean)").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/north_sea", methods=["GET"])
def north_sea():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'UK'  #uses england but could use norway
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "North Sea").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/nw_africa_morocco", methods=["GET"])
def nw_africa_morocco():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'MA'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "NW Africa / Morocco").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/persian_gulf", methods=["GET"])
def persian_gulf():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'QA' #uses Qatar
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "Persian Gulf").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/peru", methods=["GET"])
def peru():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'PE'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "Peru").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/philippines", methods=["GET"])
def philippines():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'Ph'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "Philippines").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/russia", methods=["GET"])
def russia():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'RU'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "Russia").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/s_china", methods=["GET"])
def s_china():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'CN'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "Southern China").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/sierra_leone", methods=["GET"])
def sierra_leone():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'SL'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "Sierra Leone").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/skorea_japan", methods=["GET"])
def skorea_japan():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'JP'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "S. Korea / Japan").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/somalia", methods=["GET"])
def somalia():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'SO'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "Somalia").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/south_africa", methods=["GET"])
def south_africa():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'ZA'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    
    jobs = (Job.query.filter(Job.location == "South Africa").all())
    name = 'XXXXXXXXXXXXXXXXXX'  #*******************************************************************************TO FILL IN
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/suriname", methods=["GET"])
def suriname():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'SR'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    name= 'Suriname'
    jobs = (Job.query.filter(Job.location == "Suriname").all())
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@app.route("/uruguay", methods=["GET"])
def uruguay():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'UY'
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
    name = 'Uruguay'

    jobs = (Job.query.filter(Job.location == "Uruguay").all())
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)



## break out res/data/advisory into a function and call it in all the country routes
## make routes dynamic with {{Country}}









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
