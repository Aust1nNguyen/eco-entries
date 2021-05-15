from datetime import datetime, timedelta
import unittest, os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from app import app, db
from app.models import User, Course, Quiz

# get the path of ChromeDriverServer
basedir = os.path.abspath(os.path.dirname(__file__))

#To do, find simple way for switching from test context to development to production.


class SystemTest(unittest.TestCase):
    driver = None

    def setUp(self):
        chromedriver = os.path.join(basedir, 'chromedriver.exe')
        options = Options()
        options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        driver = webdriver.Chrome(executable_path=chromedriver, options=options)
        driver.get('http://google.com/')
        # if not self.driver:
        #     self.skipTest('Web browser not available')
        # else:

        #     self.driver.get('http://google.com')

    def tearDown(self):
        pass

    def test_register(self):
       pass

if __name__ == '__main__':
    unittest.main(verbosity=2)