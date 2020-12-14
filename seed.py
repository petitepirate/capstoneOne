from models import db, User, Job
from app import app

# db.drop_all()
db.create_all()




c1 = Job(
    job_title="Lead PSO/PAM",
    location="Alaska",
    start_year=2000,
    day_rate=300,
    cont_company='RPS',
    user_id=1
)
c2 = Job(
    job_title="Lead PSO",
    location="Alaska",
    start_year=2000,
    day_rate=290,
    cont_company='RPS',
    user_id=1
)
c3 = Job(
    job_title="Lead PAM",
    location="Alaska",
    start_year=2000,
    day_rate=340,
    cont_company='RPS',
    user_id=1
)
c4 = Job(
    job_title="PSO/PAM",
    location="Alaska",
    start_year=2000,
    day_rate=300,
    cont_company='RPS',
    user_id=1
)




db.session.add_all([c1, c2, c3, c4])
db.session.commit()
# # 
