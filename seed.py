from models import db, User, Job
from app import app

# db.drop_all()
db.create_all()

u1 = User(
    user_name='msmegan',
    first_name= 'Megan',
    last_name= 'McManus',
    email='wildlife.megan@gmail.com',
    image_url="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg",
    password='pirate'
)

u2 = User(
    user_name='mskelly',
    first_name= 'Kelly',
    last_name= 'McManus',
    email='kam@gmail.com',
    image_url="https://images.unsplash.com/photo-1576618148400-f54bed99fcfd?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80",
    password='pirate2'
)

j1 = Job(
    job_title="Protected Species Observer",
    location="Gulf of Mexico",
    start_year='2019',
    day_rate='175',
    user_name='msmegan'
)

db.session.add_all([u1, u2, j1])
db.session.commit()
