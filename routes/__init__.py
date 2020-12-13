from flask import Blueprint
routes = Blueprint('routes', __name__)

from .countries import *
from .regions import *
