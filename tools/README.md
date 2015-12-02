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
Load http://localhost:8000/difference/?number=n in your browser, where
`n` is any number between 0 and 100.

#### Run tests
```bash
python manage.py test
```
