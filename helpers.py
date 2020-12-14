from secrets import API_KEY
from flask import Flask, render_template, request, flash, redirect, session, g, abort
from models import Job, db
import requests
from sqlalchemy import func
BASE_API_URL = "https://api.tugo.com/v1/travelsafe/countries/"

def get_advisory(country):
    res = requests.get(f"{BASE_API_URL}{country}", headers={"X-Auth-API-Key":f"{API_KEY}"})
    data=res.json()
    advisory= data["entryExitRequirement"]["description"]
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
