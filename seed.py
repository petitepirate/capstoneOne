from models import db, User, Job
from app import app

db.drop_all()
db.create_all()

