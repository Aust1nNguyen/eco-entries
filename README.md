# EcoEntries

A simple flask app to learn basic economic context

## Getting Started

Activate the python virtual environment:
`$source venv/bin/activate`

To run the app:
`$flask run`

To stop the app:
`$^C`

To exit the environment:
`$deactivate`

### Prerequisites

Requires python3, flask, venv, and sqlite

### Installing

Install python3, sqlite3

1. Set up a virtual environment:
    + create a virtual environment
    `python3 -m venv venv`
    + start the virtual environment
    `source venv/bin/activate`
    + install all dependecies
    `pip install -r requirements.txt`

2. Install sqlite

    + In *nix
    `sudo apt-get install sqlite`
3. Build the database
`flask db init`
4. Run flask app
`flask run`
This should start the app running on localhost at port 5000, i.e. 
[http://localhost:5000/index]

### Running the tests
