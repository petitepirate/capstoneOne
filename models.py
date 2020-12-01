from flask_sqlalchemy import SQLAlchemy
#from flask_bcrpyt import Bcrypt


db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

DEFAULT_IMG = "https://images.unsplash.com/photo-1562037283-072818fb6d8f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=250&q=80"

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(20), primary_key=True, nullable=False, unique=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False, unique=True)
    image_url = db.Column(db.Text,
                          nullable=False, default=DEFAULT_IMG)
    password = db.Column(db.Text, nullable=False)

    def __repr__(self):
        u = self
        return f"<User id={u.id} user_name={u.user_name} first_name={u.first_name} last_name={u.last_name} email={u.email}>"

class Job(db.Model):
        
    __tablename__ = 'jobs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    job_title = db.Column(db.Text, nullable=False, unique=True)
    location = db.Column(db.Text, nullable=False)
    start_year = db.Column(db.Integer, nullable=False)
    day_rate = db.Column(db.Integer, nullable=False, unique=True)
    user_name = db.Column(db.Text, db.ForeignKey('users.user_name'))

    users = db.relationship('User', backref='jobs')
