import unittest

from app import app, db
from app.models import User, Course, Quiz

class UserModelCase(unittest.TestCase):

    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):    
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        u = User(username='austin')

        # set user password
        u.set_password('123')

        # check user password
        self.assertFalse(u.check_password('123456'))
        self.assertTrue(u.check_password('123'))

    def test_enrol_course(self):
        pass

    def test_attempt_quiz(self):
        pass

    def test_user_courses(self):
        pass

    def test_user_quizes(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
