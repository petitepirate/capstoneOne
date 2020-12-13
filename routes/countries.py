from flask import render_template, request, flash, redirect, session, g, abort
from models import db, connect_db, User, Job
from . import routes
from secrets import API_KEY
import requests
BASE_API_URL = "https://api.tugo.com/v1/travelsafe/countries/"
from helpers import get_advisory, check_user

CURR_USER_KEY = "curr_user"


@routes.route("/alaska", methods=["GET"])
def alaska():
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'US'
    name = 'Alaska'  
    advisory = get_advisory(country)
    
    PSO_highest= (Job.query.filter(Job.job_title =='Lead PSO', Job.location == f"{name}").order_by(Job.day_rate.desc()).limit(1).all())   #.order_by(Job.day_rate.desc()).limit(1)
    print('************************************************************')
    print(PSO_highest)
    jobs = (Job.query.filter(Job.location == f"{name}").all())
    print('************************************************************')
    print(jobs)
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name, PSO_highest=PSO_highest)

@routes.route("/angola", methods=["GET"])
def angola():
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'AO'
    name = 'Angola' 
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())
    PSO_highest= Job.get_highest('Lead PAM', f"{name}")
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name, PSO_highest=PSO_highest)

@routes.route("/antarctica", methods=["GET"])
def antarctica():
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'AQ'
    name = 'Antartica'
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/arctic_ocean", methods=["GET"])
def arctic_ocean():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'GL'  # No real country code for arctic - uses greenland since thats the likely launching place
    name = 'Arctic Ocean'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/argentina", methods=["GET"])
def argentina():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'AR'
    name = 'Argentina'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/australia_newzealand", methods=["GET"])
def australia_newzealand():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'AU'
    name = 'Australia & New Zealand'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/black_sea", methods=["GET"])
def black_sea():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'TR'  #uses Turkey
    name = 'Black Sea'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/brazil", methods=["GET"])
def brazil():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'BR'
    name = 'Brazil'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/california", methods=["GET"])
def california():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'US'
    name = 'California'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/canada", methods=["GET"])
def canada():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'US' #api is a canadian travel api and so doesnt have canadian advisories since that is their home country
    name = 'Canada'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/caribbean", methods=["GET"])
def caribbean():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'BS'  #uses Bahamas 
    name = 'Caribbean'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/caspian_sea", methods=["GET"])
def caspian_sea():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'IR'  #uses Iran
    name = 'Caspian Sea'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/chile", methods=["GET"])
def chile():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'CL'
    name = 'Chile'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/china_vietnam", methods=["GET"])
def china_vietnam():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'CN'
    name = 'China & Vietnam'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/columbia", methods=["GET"])
def columbia():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'CO'
    name = 'Columbia'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/ecuador", methods=["GET"])
def ecuador():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'EC'
    name = 'Ecuador'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/ethiopia", methods=["GET"])
def ethiopia():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'ET'
    name = 'Ethiopia'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/falkland_islands", methods=["GET"])
def falkland_islands():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'FK'
    name = 'Falkland Islands'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/french_guiana", methods=["GET"])
def french_guiana():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'GF'
    name = 'French Guiana'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/gabon", methods=["GET"])
def gabon():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'GA'
    name = 'Gabon'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/ghana", methods=["GET"])
def ghana():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'GH'
    jobs = (Job.query.filter(Job.location == "Ghana").all())
    name = 'Ghana'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/greenland", methods=["GET"])
def greenland():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'GL'
    name = 'Greenland'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/gulf_of_mexico", methods=["GET"])
def gulf_of_mexico():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'US'
    name = 'Gulf of Mexico'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/guyana", methods=["GET"])
def guyana():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'GY'
    name = 'Guyana'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/hawaii", methods=["GET"])
def hawaii():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'US'
    name = 'Hawaii'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/iceland", methods=["GET"])
def iceland():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'IS'
    name = 'Iceland'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/india_srilanka", methods=["GET"])
def india_srilanka():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'IN'
    name = 'India & Sri Lanka'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/indonesia", methods=["GET"])
def indonesia():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'ID'
    name = 'Indonesia'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/madagascar", methods=["GET"])
def madagascar():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'MG'
    name = 'Madagascar'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())  
   
    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/malaysia", methods=["GET"])
def malaysia():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'MY'
    name = 'Malaysia'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/mauritania", methods=["GET"])
def mauritania():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'MR'
    name = 'Mauritania'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/mediterranean", methods=["GET"])
def mediterranean():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'EG' #uses egypt
    name = 'Mediterranean Sea'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/mexico", methods=["GET"])
def mexico():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'MX'
    name = 'Mexico (Pacific Ocean)'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/mozambique", methods=["GET"])
def mozambique():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'MZ'
    name = 'Mozambique'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/namibia", methods=["GET"])
def namibia():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'NA'
    name = 'Namibia'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/nigeria", methods=["GET"])
def nigeria():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'NG'
    name = 'Nigeria'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/north_atlantic", methods=["GET"])
def north_atlantic():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'US'
    name = 'US East Coast (N. Atlantic Ocean)'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/north_sea", methods=["GET"])
def north_sea():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'UK'  #uses england but could use norway
    name = 'North Sea'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/nw_africa_morocco", methods=["GET"])
def nw_africa_morocco():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'MA'
    name = 'NW Africa / Morocco'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/persian_gulf", methods=["GET"])
def persian_gulf():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'QA' #uses Qatar
    name = 'Persian Gulf'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/peru", methods=["GET"])
def peru():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'PE'
    name = 'Peru'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/philippines", methods=["GET"])
def philippines():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'Ph'
    name = 'Philippines'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/russia", methods=["GET"])
def russia():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'RU'
    name = 'Russia'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/s_china", methods=["GET"])
def s_china():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'CN'
    name = 'Southern China'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/sierra_leone", methods=["GET"])
def sierra_leone():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'SL'
    name = 'Sierra Leone'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/skorea_japan", methods=["GET"])
def skorea_japan():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'JP'
    name = 'South Korea & Japan'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/somalia", methods=["GET"])
def somalia():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'SO'
    name = 'Somalia'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/south_africa", methods=["GET"])
def south_africa():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'ZA'
    name = 'South Africa'  
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/suriname", methods=["GET"])
def suriname():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")
    country = 'SR'
    name= 'Suriname'
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)

@routes.route("/uruguay", methods=["GET"])
def uruguay():

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")
    country = 'UY'
    name = 'Uruguay'
    advisory = get_advisory(country)
    jobs = (Job.query.filter(Job.location == f"{name}").all())

    return render_template('/country.html', jobs=jobs, advisory=advisory, name=name)



## break out res/data/advisory into a function and call it in all the country routes  (return redirect should be to "/", NOT '/home')
## make routes dynamic with {{Country}}
