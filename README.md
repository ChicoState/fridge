# fridge
how to run this code  :
### Step 1: Create a Virtual Environment

Isolate your python project from other python projects by using the built-in [venv](https://docs.python.org/dev/library/venv.html) module:

```
python3.10 -m venv venv
```

- I recommend Python 3.8 and up
- You can use _any_ virtual environment manager (poetry, pipenv, virtualenv, etc)

### Step 2: Activate Virtual Environment

_macOS/Linux_

```
source venv/bin/activate
```

_Windows_

```
.\venv\Scripts\activate
```

### Step 3: Install Requirements

```
$(venv) python -m pip install pip --upgrade
$(venv) python -m pip install -r requirements.txt
```

- `$(venv)` is merely denoting the virtual environment is activated
- In `requirements.txt` you'll see `django>=3.2,<4.0` -- this means I'm using the latest version of Django 3.2 since it's an LTS release.
- You can use `venv/bin/python -m pip install -r requirements.txt` (mac/linux) or `venv\bin\python -m pip install -r requirements.txt` (windows)
- `pip install ...` is not as reliable as `python -m pip install ...`

### Step 4: to run on local server :
```
$(venv) python manage.py runserver
```

### Step 5: copy the link and past into chrom url bar :
```
http://127.0.0.1:8000/
```

### Step 6: User login :

```
user id : Bob
password : test123$
email-id  : bob@gmail.com

```

### Step 7: login admin user id and password :

```
Username : Fridge
password : Fridge123$
admin mail  : fridge@gmail.com

```
