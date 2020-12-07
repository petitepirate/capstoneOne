from datetime import datetime
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

DEFAULT_IMG = "https://images.unsplash.com/photo-1562037283-072818fb6d8f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=250&q=80"

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    user_name = db.Column(db.String(20), nullable=False, unique=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False, unique=True)
    image_url = db.Column(db.Text,
                          nullable=False, default=DEFAULT_IMG)
    password = db.Column(db.Text, nullable=False)
    jobs = db.relationship('Job')
    
    @classmethod
    def signup(cls, user_name, first_name, last_name, email, password, image_url):
        """Sign up user.

        Hashes password and adds user to system.
        """

        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

        user = User(
            user_name=user_name,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=hashed_pwd,
            image_url=image_url,
        )

        db.session.add(user)
        # db.session.commit()
        return user

    @classmethod
    def authenticate(cls, user_name, password):
        """Find user with `username` and `password`.

        This is a class method (call it on the class, not an individual user.)
        It searches for a user whose password hash matches this password
        and, if it finds such a user, returns that user object.

        If can't find matching user (or if password is wrong), returns False.
        """

        user = cls.query.filter_by(user_name=user_name).first()

        if user:
            is_auth = bcrypt.check_password_hash(user.password, password)
            if is_auth:
                return user

        return False


class Job(db.Model):
        
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    job_title = db.Column(db.Text, nullable=False)
    location = db.Column(db.Text, nullable=False)
    start_year = db.Column(db.Integer, nullable=False)
    day_rate = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer,
        db.ForeignKey('users.id',  ondelete='cascade')
    )

    user = db.relationship('User')
