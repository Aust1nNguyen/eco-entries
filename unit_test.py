from datetime import datetime, timedelta
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

    def test_enrol(self):
        u1 = User(username='austin', email='austin@example.com')
        c1 = Course(coursename='course1')
        c2 = Course(coursename='course2')
        db.session.add(u1)
        db.session.add(c1)
        db.session.add(c2)
        db.session.commit()
        self.assertEqual(u1.courses.all(), [])

        u1.enrol(c1)
        db.session.commit()
        self.assertTrue(u1.is_enrolling(c1))
        self.assertEqual(u1.courses.count(), 1)
        self.assertEqual(u1.courses.first().coursename, 'course1')

        u1.enrol(c2)
        db.session.commit()
        self.assertTrue(u1.is_enrolling(c2))
        self.assertEqual(u1.courses.count(), 2)
        self.assertEqual(u1.courses[1].coursename, 'course2')

    def test_quizclass(self):
        now = datetime.utcnow()

        u1 = User(username='austin', email='austin@example.com')
        q1 = Quiz(quizname='quiz1', quiz_scoreoutofhundred = 80,
                    user=u1, timestamp=now + timedelta(seconds=1))
        q2 = Quiz(quizname='quiz2', quiz_scoreoutofhundred = 70,
                    user=u1, timestamp=now + timedelta(seconds=2))
        db.session.add(u1)
        db.session.add(q1)
        db.session.add(q2)
        db.session.commit()
        
        self.assertEqual(u1.quizes.all(), [q1, q2])
        self.assertEqual(u1.quizes.count(), 2)
        self.assertEqual(u1.quizes[0].quizname, 'quiz1')
        self.assertEqual(u1.quizes[1].quizname, 'quiz2')
        self.assertEqual(u1.quizes[1].user, u1)


    def test_user_courses(self):
        # create four users
        u1 = User(username='austin', email='austin@example.com')
        u2 = User(username='henry', email='henry@example.com')
        u3 = User(username='wayne', email='wayne@example.com')
        u4 = User(username='rambo', email='rambo@example.com')
        db.session.add_all([u1, u2, u3, u4])

        # create four courses
        c1 = Course(coursename='course1')
        c2 = Course(coursename='course2')
        c3 = Course(coursename='course3')
        c4 = Course(coursename='course4')
        db.session.add_all([c1, c2, c3, c4])
        db.session.commit()

        # let users enrol courses
        u1.enrol(c1)
        u1.enrol(c2)
        u2.enrol(c2)
        u2.enrol(c3)
        u3.enrol(c3)
        u3.enrol(c4)
        u3.enrol(c1)
        u3.enrol(c2)
        db.session.commit()

        # check the enrolled courses of each user
        e1 = u1.enrolled_course().all()
        e2 = u2.enrolled_course().all()
        e3 = u3.enrolled_course().all()
        e4 = u4.enrolled_course().all()

        self.assertEqual(e1, [c1, c2])
        self.assertEqual(e2, [c2, c3])
        self.assertEqual(e3, [c3, c4, c1, c2])
        self.assertEqual(e4, [])

    def test_user_quizes(self):
        # create four users
        u1 = User(username='austin', email='austin@example.com')
        u2 = User(username='henry', email='henry@example.com')
        u3 = User(username='wayne', email='wayne@example.com')
        u4 = User(username='rambo', email='rambo@example.com')
        db.session.add_all([u1, u2, u3, u4])
        
        now = datetime.utcnow()
        # create four courses
        q1 = Quiz(quizname='quiz1', quiz_scoreoutofhundred = 80,
                    user=u1, timestamp=now + timedelta(seconds=1))
        q2 = Quiz(quizname='quiz2', quiz_scoreoutofhundred = 70,
                    user=u2, timestamp=now + timedelta(seconds=2))
        q3 = Quiz(quizname='quiz2', quiz_scoreoutofhundred = 60,
                    user=u1, timestamp=now + timedelta(seconds=3))
        q4 = Quiz(quizname='quiz1', quiz_scoreoutofhundred = 85,
                    user=u2, timestamp=now + timedelta(seconds=4))

        db.session.add_all([q1, q2, q3, q4])
        db.session.commit()

        # check the completed quizes of each user
        cq1 = u1.completed_quiz()
        cq2 = u2.completed_quiz()
        cq3 = u3.completed_quiz()
        cq4 = u4.completed_quiz()

        self.assertEqual(cq1, [q3, q1])
        self.assertEqual(cq2, [q4, q2])
        self.assertEqual(cq3, [])
        self.assertEqual(cq4, [])

if __name__ == '__main__':
    unittest.main(verbosity=2)
