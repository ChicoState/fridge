# Fridge

# Purpose
Fridge was created by Amritvir Randhawa, Andrew Moskowitz, Karandeep Dhillon, and Tamanna Haider for a Chico State Software Engineering project. When this group of students were asked, “What is a common problem you face that could be fixed with software?”, they had a plethora of thoughts on the matter. But they all agreed on one thing: keeping track of food items, tracking food waste, and budgeting were all difficult tasks, not just for college students, but for many households.

The purpose of this project was to provide a way to keep track of current food items, even when you’re not near your fridge. You can see which items are still good, expiring soon, or expired, so you know what you can count on eating when you get home, or use grocery items before they go bad. This encourages people to limit the amount of food that is wasted. This tool is also great for budgeting, as you can see how much money was “thrown away” with the food that went bad. Seeing how much money could be saved is a great motivator to only buy what is needed.

# Features
i. Authentication: Email/password to protect user data. 

ii. Add unilimited items in fridge. 

iii. Sort items by name, date and type.

iv. Track item expiry date and display status Expired Warning(3 days prior Expiry date) and Good. 

v. Expired item diaplay on top.

vi. Search items through voice recognition search-bar.

vii. items separated by categories: dairy, frozen veg, meat, fruits, beverages.

viii. edit/delete items 

ix. User can track Expenses and Wastage money on expired items. 

x. User can track fridge data with chart.

xi. User can also track weekly expired data.

xii. Notification - Send notification to user when item status is expire and warning. 

xiii. User can change items QTY from inc and dec button. 

xiv.  Send Welcome email when user register first time. 

# To-do
i. Send email to the user when item expires. 

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
