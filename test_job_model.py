"""Job Model tests."""


# run these tests like:
#
#    FLASK_ENV=production python -m unittest test_job_model.py


import os
from unittest import TestCase
from sqlalchemy.exc import IntegrityError
from models import db, connect_db, User, Job, DEFAULT_IMG

os.environ['DATABASE_URL'] = "postgresql:///psopayscale-test"


from app import app, CURR_USER_KEY

db.create_all()

app.config['WTF_CSRF_ENABLED'] = False


class JobModelTestCase(TestCase):
    """Test model for Users."""

    def setUp(self):

        db.drop_all()
        db.create_all()

        self.uid = 94566
        u = User.signup('user1', 'u1_first', 'u1_last', 'test1@test.nil', 'testpw1', DEFAULT_IMG)
        u.id = self.uid
        db.session.commit()

        self.u = User.query.get(self.uid)

        self.client = app.test_client()

    def tearDown(self):
        res = super().tearDown()
        db.session.rollback()
        return res


    def test_job_model(self):
        """Does basic model work?"""

        j= Job(job_title="PSO", location="Alaska", start_year="2012", day_rate="210", cont_company="RPS", user_id="94566")
        db.session.add(j)
        db.session.commit()


        # User should have one jobs
        self.assertEqual(len(self.u.jobs), 1)
        self.assertEqual(self.u.jobs[0].location, 'Alaska')
        self.assertEqual(self.u.jobs[0].start_year, 2012)
        self.assertEqual(self.u.jobs[0].day_rate, 210)

