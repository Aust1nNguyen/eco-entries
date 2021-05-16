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
    ```source venv/bin/activate```
    + install all dependecies
    ```pip install -r requirements.txt```

2. Install sqlite

    + In *nix
    ```sudo apt-get install sqlite```

3. Build the database
```flask db init```

4. Run flask app
```flask run```

This should start the app running on localhost at port 5000, i.e. 
[http://localhost:5000/index](http://localhost:5000/index)

### Running tests

1. Unit tests
To run unit tests, use command
```python3 unit_test.py```

2. System tests
System test supports running test on Chrome using chromedriver. The newest chromedriver version is ran and test on Window. To download another version of chromedriver, follow this [link](https://sites.google.com/a/chromium.org/chromedriver/downloads)

To run system tests, use command
```python3 system_test.py```

### Acknowledgements

+ [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) by Miguel Grinberg
+ [W3 schools](https://www.w3schools.com/)