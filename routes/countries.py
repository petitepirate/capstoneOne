from flask import render_template, request, flash, redirect, session, g, abort
from models import db, connect_db, User, Job
from . import routes
from secrets import API_KEY
import requests
BASE_API_URL = "https://api.tugo.com/v1/travelsafe/countries/"
from helpers import get_advisory, check_user, get_average, get_list, get_jobs
from sqlalchemy import func

CURR_USER_KEY = "curr_user"
TITLES= ('Lead PAM', 'Lead PSO', 'Lead PSO/PAM', 'PSO/PAM', 'PAM', 'PSO')

@routes.route("/alaska", methods=["GET"])
def alaska():
    if not g.user:
        
        return redirect("/home")

    country = 'US'
    name = 'Alaska'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/angola", methods=["GET"])
def angola():
    if not g.user:
        
        return redirect("/home")
    country = 'AO'
    name = 'Angola' 
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/antarctica", methods=["GET"])
def antarctica():
    if not g.user:
        
        return redirect("/home")
    country = 'AQ'
    name = 'Antartica'
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/arctic_ocean", methods=["GET"])
def arctic_ocean():

    if not g.user:
        
        return redirect("/home")
    country = 'GL'  # No real country code for arctic - uses greenland since thats the likely launching place
    name = 'Arctic Ocean'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/argentina", methods=["GET"])
def argentina():

    if not g.user:
        
        return redirect("/home")
    country = 'AR'
    name = 'Argentina'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)
@routes.route("/australia_newzealand", methods=["GET"])
def australia_newzealand():

    if not g.user:
        
        return redirect("/home")
    country = 'AU'
    name = 'Australia & New Zealand'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/black_sea", methods=["GET"])
def black_sea():

    if not g.user:
        
        return redirect("/home")
    country = 'TR'  #uses Turkey
    name = 'Black Sea'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/brazil", methods=["GET"])
def brazil():

    if not g.user:
        
        return redirect("/home")
    country = 'BR'
    name = 'Brazil'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/california", methods=["GET"])
def california():

    if not g.user:
        
        return redirect("/home")
    country = 'US'
    name = 'California'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/canada", methods=["GET"])
def canada():

    if not g.user:
        
        return redirect("/home")
    country = 'US' #api is a canadian travel api and so doesnt have canadian advisories since that is their home country
    name = 'Canada'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/caribbean", methods=["GET"])
def caribbean():

    if not g.user:
        
        return redirect("/home")
    country = 'BS'  #uses Bahamas 
    name = 'Caribbean'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/caspian_sea", methods=["GET"])
def caspian_sea():

    if not g.user:
        
        return redirect("/home")
    country = 'IR'  #uses Iran
    name = 'Caspian Sea'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/chile", methods=["GET"])
def chile():

    if not g.user:
        
        return redirect("/home")
    country = 'CL'
    name = 'Chile'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/china_vietnam", methods=["GET"])
def china_vietnam():

    if not g.user:
        
        return redirect("/home")
    country = 'CN'
    name = 'China & Vietnam'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/columbia", methods=["GET"])
def columbia():

    if not g.user:
        
        return redirect("/home")
    country = 'CO'
    name = 'Columbia'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/ecuador", methods=["GET"])
def ecuador():

    if not g.user:
        
        return redirect("/home")
    country = 'EC'
    name = 'Ecuador'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/ethiopia", methods=["GET"])
def ethiopia():

    if not g.user:
        
        return redirect("/home")
    country = 'ET'
    name = 'Ethiopia'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/falkland_islands", methods=["GET"])
def falkland_islands():

    if not g.user:
        
        return redirect("/home")
    country = 'FK'
    name = 'Falkland Islands'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/french_guiana", methods=["GET"])
def french_guiana():

    if not g.user:
        
        return redirect("/home")
    country = 'GF'
    name = 'French Guiana'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/gabon", methods=["GET"])
def gabon():

    if not g.user:
        
        return redirect("/home")
    country = 'GA'
    name = 'Gabon'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/ghana", methods=["GET"])
def ghana():

    if not g.user:
        
        return redirect("/home")
    country = 'GH'
    jobs = (Job.query.filter(Job.location == "Ghana").all())
    name = 'Ghana'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/greenland", methods=["GET"])
def greenland():

    if not g.user:
        
        return redirect("/home")
    country = 'GL'
    name = 'Greenland'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/gulf_of_mexico", methods=["GET"])
def gulf_of_mexico():

    if not g.user:
        
        return redirect("/home")
    country = 'US'
    name = 'Gulf of Mexico'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/guyana", methods=["GET"])
def guyana():

    if not g.user:
        
        return redirect("/home")
    country = 'GY'
    name = 'Guyana'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/hawaii", methods=["GET"])
def hawaii():

    if not g.user:
        
        return redirect("/home")
    country = 'US'
    name = 'Hawaii'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/iceland", methods=["GET"])
def iceland():

    if not g.user:
        
        return redirect("/home")
    country = 'IS'
    name = 'Iceland'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/india_srilanka", methods=["GET"])
def india_srilanka():

    if not g.user:
        
        return redirect("/home")
    country = 'IN'
    name = 'India & Sri Lanka'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/indonesia", methods=["GET"])
def indonesia():

    if not g.user:
        
        return redirect("/home")
    country = 'ID'
    name = 'Indonesia'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/madagascar", methods=["GET"])
def madagascar():

    if not g.user:
        
        return redirect("/home")
    country = 'MG'
    name = 'Madagascar'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/malaysia", methods=["GET"])
def malaysia():

    if not g.user:
        
        return redirect("/home")
    country = 'MY'
    name = 'Malaysia'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/mauritania", methods=["GET"])
def mauritania():

    if not g.user:
        
        return redirect("/home")
    country = 'MR'
    name = 'Mauritania'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/mediterranean", methods=["GET"])
def mediterranean():

    if not g.user:
        
        return redirect("/home")
    country = 'EG' #uses egypt
    name = 'Mediterranean Sea'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/mexico", methods=["GET"])
def mexico():

    if not g.user:
        
        return redirect("/home")
    country = 'MX'
    name = 'Mexico (Pacific Ocean)'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/mozambique", methods=["GET"])
def mozambique():

    if not g.user:
        
        return redirect("/home")
    country = 'MZ'
    name = 'Mozambique'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/namibia", methods=["GET"])
def namibia():

    if not g.user:
        
        return redirect("/home")
    country = 'NA'
    name = 'Namibia'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/nigeria", methods=["GET"])
def nigeria():

    if not g.user:
        
        return redirect("/home")
    country = 'NG'
    name = 'Nigeria'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/north_atlantic", methods=["GET"])
def north_atlantic():

    if not g.user:
        
        return redirect("/home")
    country = 'US'
    name = 'US East Coast (N. Atlantic Ocean)'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/north_sea", methods=["GET"])
def north_sea():

    if not g.user:
        
        return redirect("/home")
    country = 'GB'  #uses england but could use norway
    name = 'North Sea'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)


    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/nw_africa_morocco", methods=["GET"])
def nw_africa_morocco():

    if not g.user:
        
        return redirect("/home")
    country = 'MA'
    name = 'NW Africa / Morocco'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/persian_gulf", methods=["GET"])
def persian_gulf():

    if not g.user:
        
        return redirect("/home")
    country = 'QA' #uses Qatar
    name = 'Persian Gulf'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/peru", methods=["GET"])
def peru():
    if not g.user:
        
        return redirect("/home")
    country = 'PE'
    name = 'Peru'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/philippines", methods=["GET"])
def philippines():

    if not g.user:
        
        return redirect("/home")
    country = 'PH'
    name = 'Philippines'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/russia", methods=["GET"])
def russia():

    if not g.user:
        
        return redirect("/home")
    country = 'RU'
    name = 'Russia'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/s_china", methods=["GET"])
def s_china():

    if not g.user:
        
        return redirect("/home")
    country = 'CN'
    name = 'Southern China'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/sierra_leone", methods=["GET"])
def sierra_leone():

    if not g.user:
        
        return redirect("/home")
    country = 'SL'
    name = 'Sierra Leone'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/skorea_japan", methods=["GET"])
def skorea_japan():

    if not g.user:
        
        return redirect("/home")
    country = 'JP'
    name = 'South Korea & Japan'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/somalia", methods=["GET"])
def somalia():

    if not g.user:
        
        return redirect("/home")
    country = 'SO'
    name = 'Somalia'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/south_africa", methods=["GET"])
def south_africa():

    if not g.user:
        
        return redirect("/home")
    country = 'ZA'
    name = 'South Africa'  
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/suriname", methods=["GET"])
def suriname():

    if not g.user:
        
        return redirect("/home")
    country = 'SR'
    name= 'Suriname'
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)

@routes.route("/uruguay", methods=["GET"])
def uruguay():

    if not g.user:
        
        return redirect("/")
    country = 'UY'
    name = 'Uruguay'
    advisory = get_advisory(country)

    listofrates= get_list(name)
    data= zip(TITLES, listofrates)

    jobs = get_jobs(name)

    return render_template('/country.html', jobs=jobs, name=name, listofrates=listofrates, data=data, advisory=advisory)


## make routes dynamic with {{Country}}
