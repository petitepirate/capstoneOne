from secrets import API_KEY
from flask import Flask, render_template, request, flash, redirect, session, g, abort
from models import Job, db
import requests
from sqlalchemy import func
BASE_API_URL = "https://api.tugo.com/v1/travelsafe/countries/"

COUNTRIES = [("Alaska", "alaska"), ("Angola", "angola"),("Antarctica", "antarctica"),("Arctic Ocean", "arctic_ocean"), ("Argentina", "argentina"),("Australia / New Zealand", "australia_newzealand"),("Black Sea", "black_sea"),("Brazil", "brazil"),
("California", "california"),("Canada", "canada"),("Caribbean", "caribbean"),("Caspian Sea", "caspian_sea"),("Chile", "chile"),("China / Vietnam", "china_vietnam"),("Columbia", "columbia"),("Ecuador", "ecuador"),("Ethiopia", "ethiopia"),
("Falkland Islands", "falkland_islands"),("French Guiana", "french_guiana"),("Gabon", "gabon"),("Ghana", "ghana"),("Greenland", "greenland"),("Gulf of Mexico", "gulf_of_mexico"),("Guyana", "guyana"),("Hawaii", "hawaii"),("Iceland", "iceland"),
("India / Sri Lanka", "india_srilanka"),("Indonesia", "indonesia"),("Madagascar", "madagascar"),("Malaysia", "malaysia"),("Mauritania", "mauritania"),("Mediterranean Sea", "mediterranean"),("Mexico (Pacific)", "mexico"),("Mozambique", "mozambique"),
("Namibia", "namibia"),("Nigeria", "nigeria"),("US East Coast (N. Atlantic Ocean)", "north_atlantic"),("North Sea", "north_sea"),("NW Africa / Morocco", "nw_africa_morocco"),("Persian Gulf", "persian_gulf"),("Peru", "peru"),("Philippines", "philippines"),("Russia", "russia"),
("Southern China", "s_china"),("Sierra Leone", "sierra_leone"),("S. Korea / Japan", "skorea_japan"),("Somalia", "somalia"),("South Africa", "south_africa"),("Suriname", "suriname"),("Uruguay", "uruguay")]

def get_advisory(country):
    try:
        res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"}, timeout=5.0)
        data=res.json()
        advisory= data["entryExitRequirement"]["description"]
        return advisory
    except requests.exceptions.Timeout:
        advisory='No Data Available'
        return advisory


def check_user():
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")

def get_average(title, name):
    try:
        avg_dec = db.session.query(func.avg(Job.day_rate)).filter(Job.job_title == f"{title}", Job.location == f"{name}").scalar()
        avg_rate=int(avg_dec)
        return avg_rate
    except:
        avg_rate='No Data Available'
        return avg_rate 

def get_list(name):
    avg_LPAM = get_average('Lead PAM', name)
    avg_LPSO = get_average('Lead PSO', name)
    avg_LDual = get_average('Lead PSO/PAM', name)
    avg_Dual = get_average('PSO/PAM', name)
    avg_PAM = get_average('PAM', name)
    avg_PSO = get_average('PSO', name)
    listobj = [avg_LPAM, avg_LPSO, avg_LDual, avg_Dual, avg_PAM, avg_PSO]

    return listobj

def get_jobs(name):
    jobs = (Job.query.filter(Job.location == f"{name}").all())
    return jobs

def get_region_avg(name):
    try:
        avg_dec = db.session.query(func.avg(Job.day_rate)).filter(Job.location == f"{name}").scalar()
        avg_rate=int(avg_dec)
        return avg_rate
    except:
        avg_rate='No Data Available'
        return avg_rate 
