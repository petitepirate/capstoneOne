"""Job View tests."""

# run these tests like:
#
#    FLASK_ENV=production python -m unittest test_job_view.py


import os
from unittest import TestCase
from models import db, connect_db, User, Job, DEFAULT_IMG


os.environ['DATABASE_URL'] = "postgresql:///psopayscale-test"


from app import app, CURR_USER_KEY

db.create_all()

app.config['WTF_CSRF_ENABLED'] = False


class MessageViewTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test client, add sample data."""

        User.query.delete()
        Job.query.delete()

        self.client = app.test_client()

        self.testuser = User.signup(user_name="testuser",
                                    first_name="first",
                                    last_name="last",
                                    email="test@test.com",
                                    password="testuser",
                                    image_url=None)

        db.session.commit()

    def test_add_job(self):
        """Can use add a message?"""

        # Since we need to change the session to mimic logging in,
        # we need to use the changing-session trick:

        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser.id

            # Now, that session setting is saved, so we can have
            # the rest of ours test

            resp = c.post(f"/user/{self.testuser.id}/addjob", data={"job_title": "PSO", "location": "Angola", "start_year": 2015, "day_rate": 360, "cont_company": "EPI", "user_id": 1})

            # Make sure it redirects
            self.assertEqual(resp.status_code, 302)

            job = Job.query.one()
            self.assertEqual(job.job_title, "PSO")
