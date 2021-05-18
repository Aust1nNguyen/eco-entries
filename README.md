# EcoEntries

A flask app provide users basic economic contents and quizes to attempt after finish the course

## Getting Started

Activate the python virtual environment:  
```$source venv/bin/activate```

To run the app:  
```$flask run```

To stop the app:  
```$^C```

To exit the environment:  
```$deactivate```

### Prerequisites

Requires python3, flask, venv, and sqlite

### Launching

Install python3, sqlite3

1. Set up a virtual environment:
    + create a virtual environment  
      ```python3 -m venv venv```
    + start the virtual environment  
        + On *nix  
          ```source venv/bin/activate```
        + On windows  
          ```venv\Scripts\activate```
    + install all dependecies  
      ```pip install -r requirements.txt```

2. Install sqlite
    + On *nix  
      ```sudo apt-get install sqlite```
    + On windows, follow the link  
      [https://www.sqlitetutorial.net/download-install-sqlite/]([https://www.sqlitetutorial.net/download-install-sqlite/)

3. Build the database
    + Initialize database  
      ```flask db init```
    + Migrate the database for the first run  
      ```flask db migrate```
    + Upgrade the databse for the first run  
      ```flask db upgrade```

4. Run flask app  
  ```flask run```

This should start the app running on localhost at port 5000, i.e.  
[http://localhost:5000/index](http://localhost:5000/index)

### Running tests

Firstly, run the flask app on localhost  
  ```flask run```

There are two tests for this app, unit test and system test

1. Unit test
  To run unit tests, use command  
    ```python3 unit_test.py```

2. System test
  System test supports running test on Chrome using chromedriver. The newest chromedriver version is ran and test on Window. To download another version of chromedriver, follow this link  
    [https://sites.google.com/a/chromium.org/chromedriver/downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads)  
  
  To test on Mac or Linux, simply uncomment the chromedriver part in the system_test.py  

  To run system tests, use command  
    ```python3 system_test.py```

### Acknowledgements

+ [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) by Miguel Grinberg
+ [W3 schools](https://www.w3schools.com/)
