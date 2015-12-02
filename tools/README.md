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
```
cd /path/to/tools
pip install -r requirements.txt
```