from secrets import API_KEY
from flask import Flask, render_template, request, flash, redirect, session, g, abort
import requests
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
