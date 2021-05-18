from datetime import datetime, timedelta
import unittest, os, time
from selenium import webdriver
from app import app, db
from app.models import User, Course, Quiz

# get the path of ChromeDriverServer
basedir = os.path.abspath(os.path.dirname(__file__))

class SystemTest(unittest.TestCase):
    driver = None
    
    def setUp(self):
        db.init_app(app)
        db.create_all()

        # Windows chromedriver
        chromedriver = os.path.join(basedir, 'drivers','chromedriver_win32 (90)', 'chromedriver.exe')
        self.driver = webdriver.Chrome(executable_path=chromedriver)

        # Linux chromedriver
        # chromedriver = os.path.join(basedir, 'drivers','chromedriver_linux64', 'chromedriver.exe')

        # Mac chromedriver
        # chromedriver = os.path.join(basedir, 'drivers','chromedriver_mac64', 'chromedriver.exe')

        # geckodriver = os.path.join(basedir, 'drivers', 'geckodriver.exe')
        # self.driver = webdriver.Firefox(executable_path=geckodriver)
        
        if not self.driver:
             self.skipTest('Web browser not available')
        else:
            u1 = User(username='random', email='random@example.com', password_hash=123)
           
            db.session.add(u1)
            db.session.commit()

            self.driver.maximize_window()
            self.driver.get('http://localhost:5000/')

    def tearDown(self):
        if self.driver:
            self.driver.close()
            u1 = db.session.query(User).filter_by(username='random').first()
            u2 = db.session.query(User).filter_by(username='somebody').first()
            
            db.session.delete(u1)
            if u2:
                db.session.delete(u2)
            db.session.commit()
            db.session.remove()

    def test_validuser(self):

        # Valid sign up
        self.driver.get('http://localhost:5000/sign_up')
        self.driver.implicitly_wait(5)

        username = self.driver.find_element_by_id('username')
        username.send_keys('somebody')
        email = self.driver.find_element_by_id('email')
        email.send_keys('somebody@example.com')
        password = self.driver.find_element_by_id('password')
        password.send_keys('123456')
        password2 = self.driver.find_element_by_id('password2')
        password2.send_keys('123456')

        time.sleep(1)
        self.driver.implicitly_wait(5)
        submit = self.driver.find_element_by_id('submit')
        submit.click()

        self.driver.implicitly_wait(5)
        time.sleep(1)

        # check sign up success - redirect to login page
        login = self.driver.find_element_by_class_name('login')
        self.assertEqual(login.get_attribute('innerHTML'), 'Sign In')


        # Login new user
        self.driver.implicitly_wait(5)
        username = self.driver.find_element_by_id('username')
        username.send_keys('somebody')
        password = self.driver.find_element_by_id('password')
        password.send_keys('123456')

        time.sleep(1)
        self.driver.implicitly_wait(5)

        submit = self.driver.find_element_by_id('submit')
        submit.click()

        self.driver.implicitly_wait(5)
        time.sleep(1)

        # check login success - has logout option
        logout = self.driver.find_element_by_xpath("//a[contains(@href,'logout')]")
        self.assertIsNotNone(logout)


        # Enrol a course 
        # view all courses
        self.driver.find_element_by_xpath("//a[contains(@href,'content')]").click()
        self.driver.implicitly_wait(5)
        time.sleep(1)

        # choose a course
        self.driver.find_element_by_xpath("//a[contains(@href,'ds')]").click()
        self.driver.implicitly_wait(5)
        time.sleep(1)

        # go back to dashboard
        self.driver.find_element_by_xpath("//a[contains(@href,'dashboard')]").click()
        self.driver.implicitly_wait(5)
        time.sleep(1)

        # check if enrolled course in displayed
        ds = self.driver.find_element_by_xpath("//a[contains(@href, 'ds')]")
        self.assertIsNotNone(ds)

        # Attempt a quiz
         # view all quizes
        self.driver.find_element_by_xpath("//a[contains(@href,'quiz')]").click()
        self.driver.implicitly_wait(5)
        time.sleep(1)

        # choose a quiz
        self.driver.find_element_by_xpath("//a[contains(@href,'ds_quiz')]").click()
        self.driver.implicitly_wait(5)
        time.sleep(1)

        # do the quiz
        # answers = ["b", "c", "c", "b", "c"]
        self.driver.find_element_by_id('q1b').click()
        time.sleep(1)
        self.driver.find_element_by_id('q2b').click()
        time.sleep(1)
        self.driver.find_element_by_id('q3c').click()
        time.sleep(1)
        self.driver.find_element_by_id('q4a').click()
        time.sleep(1)
        self.driver.find_element_by_id('q5c').click()
        time.sleep(1)

        self.driver.find_element_by_id('submit').click()
        time.sleep(1)


        # check if the feedback return
        # result = self.driver.find_element_by_id('results')
        # self.assertEqual(result.get_attribute('innerHTML'), 'Your result is 3 out of 5')

        # check if result display on that dashboard
        self.driver.find_element_by_xpath("//a[contains(@href,'dashboard')]").click()

        ds =  self.driver.find_element_by_xpath("//a[contains(@href,'ds')]")
        self.assertIsNotNone(ds)

    def test_signup_invalid(self):

        # Invalid sign up - username already exists
        self.driver.get('http://localhost:5000/sign_up')
        self.driver.implicitly_wait(5)

        username = self.driver.find_element_by_id('username')
        username.send_keys('random')
        email = self.driver.find_element_by_id('email')
        email.send_keys('random@example.com')
        password = self.driver.find_element_by_id('password')
        password.send_keys('123456')
        password2 = self.driver.find_element_by_id('password2')
        password2.send_keys('123456')

        time.sleep(1)
        self.driver.implicitly_wait(5)

        submit = self.driver.find_element_by_id('submit')
        submit.click()

        self.driver.implicitly_wait(5)
        time.sleep(1)

        # check sign up fail - stay at the register page
        login = self.driver.find_element_by_class_name('login')
        self.assertEqual(login.get_attribute('innerHTML'), 'Register')


    def test_login_invalid(self):        
        self.driver.get('http://localhost:5000/login')
        self.driver.implicitly_wait(5)

        username = self.driver.find_element_by_id('username')
        username.send_keys('random')
        password = self.driver.find_element_by_id('password')
        password.send_keys(12345)

        time.sleep(1)
        self.driver.implicitly_wait(5)

        submit = self.driver.find_element_by_id('submit')
        submit.click()

        self.driver.implicitly_wait(5)
        time.sleep(1)

        # check login fail - still at login page
        login = self.driver.find_element_by_class_name('login')
        self.assertEqual(login.get_attribute('innerHTML'), 'Sign In')


    def test_redirect_login(self):
        self.driver.get('http://localhost:5000/quiz')
        self.driver.implicitly_wait(5)
        time.sleep(1)

        # check if login page
        login = self.driver.find_element_by_class_name('login')
        self.assertEqual(login.get_attribute('innerHTML'), 'Sign In')


if __name__=='__main__':
  unittest.main(verbosity=2)
