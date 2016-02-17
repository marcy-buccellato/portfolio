# Tools Django App

## Setup

#### Create virtualenv

**Prereqs**
- Python 2.7
- pip

Note: /venv/tools = whatever you want the path to the application to be
```bash
pip install virtualenv
mkdir -p /venv/tools
virtualenv /venv/tools
source /venv/tools/bin/activate
```

#### Install requirements

Note: /path/to/tools = where this directory lives.
```bash
cd /path/to/tools
pip install -r requirements.txt
```

#### Setup database
```bash
python manage.py migrate
```

#### Run application
```bash
python manage.py runserver
```
Load http://localhost:8000/difference/ in your browser.
Input a number between 0-100.

#### Run tests
```bash
python manage.py test
```

## Difference
Difference is a service that will allow a user to input a query and will yield the difference between:
1. the sum of the squares of the first n natural numbers
2. the square of the sum of the same first n natural numbers
where n is an input number between 0-100.

**Example**

The sum of the squares of the first ten natural numbers is:
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is:
(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 − 385 = 2640.
