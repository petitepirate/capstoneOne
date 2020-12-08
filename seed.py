from models import db, User, Job
from app import app

# db.drop_all()
db.create_all()





j1 = Job(
    job_title="PSO",
    location="Antarctica",
    start_year='2019',
    day_rate='175',
    cont_company='RPS',
    user_id='1'
)

j2 = Job(
    job_title="PSO",
    location="Alaska",
    start_year='2019',
    day_rate='175',
    cont_company='RPS',
    user_id='1'
)

j3 = Job(
    job_title="Lead PAM",
    location="Antarctica",
    start_year='2019',
    day_rate='175',
    cont_company='RPS',
    user_id='1'
)

j4 = Job(
    job_title="Lead PAM",
    location="Alaska",
    start_year='2019',
    day_rate='175',
    cont_company='RPS',
    user_id='1'
)

db.session.add_all([j1, j2, j3, j4])
db.session.commit()
