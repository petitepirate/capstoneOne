"""User Model tests."""

# run these tests like:
#
#    FLASK_ENV=production python -m unittest test_user_model.py


import os
from unittest import TestCase
from sqlalchemy.exc import IntegrityError
from models import db, connect_db, User, Job, DEFAULT_IMG


os.environ['DATABASE_URL'] = "postgresql:///psopayscale-test"


from app import app, CURR_USER_KEY


db.create_all()

app.config['WTF_CSRF_ENABLED'] = False


class UserModelTestCase(TestCase):
    """Test model for Users."""

    def setUp(self):
        """Create test client, add sample data."""

        db.drop_all()
        db.create_all()

        user1 = User.signup('user1', 'u1_first', 'u1_last', 'test1@test.nil', 'testpw1', DEFAULT_IMG)
        uid1 = 111
        user1.id = uid1

        user2 = User.signup('user2', 'u2_first', 'u2_last', 'test2@test.nil', 'testpw2', DEFAULT_IMG)
        uid2 = 222
        user2.id = uid2

        db.session.commit()

        u1 = User.query.get(uid1)
        u2 = User.query.get(uid2)

        self.u1 = u1
        self.uid1 = uid1

        self.u2 = u2
        self.uid2 = uid2

        self.client = app.test_client()

    def tearDown(self):
        res = super().tearDown()
        db.session.rollback()
        return res
    
    def test_user_model(self):
        """Does basic model work?"""

        u = User(

            user_name="testuser",
            first_name="firstname",
            last_name="lastname",
            email="test@test.com",
            password="HASHED_PASSWORD",
            image_url="DEFAULT_IMG"
        )

        db.session.add(u)
        db.session.commit()

        # User should have no jobs
        self.assertEqual(len(u.jobs), 0)

    # Tests for user signup
    def test_valid_signup(self):
        u_test = User.signup("testtesttest", "testfirst", "testlast", "testtest@test.com", "password", None)
        uid = 99999
        u_test.id = uid
        db.session.commit()

        u_test = User.query.get(uid)
        self.assertIsNotNone(u_test)
        self.assertEqual(u_test.user_name, "testtesttest")
        self.assertEqual(u_test.first_name, "testfirst")
        self.assertEqual(u_test.last_name, "testlast")
        self.assertEqual(u_test.email, "testtest@test.com")
        self.assertNotEqual(u_test.password, "password")
        # Bcrypt strings should start with $2b$
        self.assertTrue(u_test.password.startswith("$2b$"))


    def test_invalid_password_signup(self):
        with self.assertRaises(ValueError) as context:
            User.signup("testtest", "testfirst", "testlast", "testtest@test.com", "", None)
        
        with self.assertRaises(ValueError) as context:
            User.signup("testtest", "testfirst", "testlast", "testtest@test.com", None, None)

    # Tests for user authentication
    def test_valid_authentication(self):
        u = User.authenticate(self.u1.user_name, "password")
        self.assertIsNotNone(u)
        self.assertEqual(self.uid1, 111)
    
    def test_invalid_username(self):
        self.assertFalse(User.authenticate("badusername", "password"))

    def test_wrong_password(self):
        self.assertFalse(User.authenticate(self.u1.user_name, "badpassword"))

