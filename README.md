# Fridge

# Purpose
Fridge was created by Amritvir Randhawa, Andrew Moskowitz, Karandeep Dhillon, and Tamanna Haider for a Chico State Software Engineering project. When this group of students were asked, “What is a common problem you face that could be fixed with software?”, they had a plethora of thoughts on the matter. But they all agreed on one thing: keeping track of food items, tracking food waste, and budgeting were all difficult tasks, not just for college students, but for many households.

The purpose of this project was to provide a way to keep track of current food items, even when you’re not near your fridge. You can see which items are still good, expiring soon, or expired, so you know what you can count on eating when you get home, or use grocery items before they go bad. This encourages people to limit the amount of food that is wasted. This tool is also great for budgeting, as you can see how much money was “thrown away” with the food that went bad. Seeing how much money could be saved is a great motivator to only buy what is needed.

### Design
<img width="1438" alt="Screen Shot 2022-12-06 at 2 24 02 PM" src="https://user-images.githubusercontent.com/107584457/206037865-ece7ffdc-72d2-4cf2-b0bc-eca57fd770d4.png">

<img width="1440" alt="Screen Shot 2022-12-06 at 2 24 22 PM" src="https://user-images.githubusercontent.com/107584457/206037996-2615de27-b5c0-42c8-98eb-614ece5ebedc.png">
<img width="1440" alt="Screen Shot 2022-12-06 at 2 24 30 PM" src="https://user-images.githubusercontent.com/107584457/206037999-d2ba4b08-8947-4678-905f-7f2dabaa36ec.png">
<img width="1440" alt="Screen Shot 2022-12-06 at 2 24 38 PM" src="https://user-images.githubusercontent.com/107584457/206038001-4fa2df2e-33fd-42ff-82d8-1f6f727efce9.png">
<img width="1440" alt="Screen Shot 2022-12-06 at 2 25 03 PM" src="https://user-images.githubusercontent.com/107584457/206038002-c27ef504-2c66-4c4c-8907-6265ffa817dc.png">
<img width="1439" alt="Screen Shot 2022-12-06 at 2 25 16 PM" src="https://user-images.githubusercontent.com/107584457/206038004-6416a455-a0ea-470c-b00f-e32d55d7c3d2.png">
<img width="1440" alt="Screen Shot 2022-12-06 at 2 25 56 PM" src="https://user-images.githubusercontent.com/107584457/206038006-c0bebc47-329e-4a9d-9736-aa6b13f6cb75.png">
<img width="1439" alt="Screen Shot 2022-12-06 at 2 26 22 PM" src="https://user-images.githubusercontent.com/107584457/206038007-2633c7ff-bd47-408b-b1dc-6d0fa6eacb05.png">
<img width="1439" alt="Screen Shot 2022-12-06 at 2 26 35 PM" src="https://user-images.githubusercontent.com/107584457/206038008-39e7be6b-c977-412f-8602-00666645774d.png">
<img width="1440" alt="Screen Shot 2022-12-06 at 2 26 44 PM" src="https://user-images.githubusercontent.com/107584457/206038009-09a2d222-8a7e-4a84-a436-c7246687eaeb.png">
<img width="1435" alt="Screen Shot 2022-12-06 at 2 28 42 PM" src="https://user-images.githubusercontent.com/107584457/206038011-56d603f9-de14-4d13-8908-c92f50bef2d0.png">
<img width="1440" alt="Screen Shot 2022-12-06 at 2 28 54 PM" src="https://user-images.githubusercontent.com/107584457/206038014-8eae3d88-55ef-4039-85bc-877e3440d2d6.png">
<img width="1440" alt="Screen Shot 2022-12-06 at 2 29 12 PM" src="https://user-images.githubusercontent.com/107584457/206038017-882b16fe-ae04-46ba-abb7-9e3e65d8a915.png">
<img width="1440" alt="Screen Shot 2022-12-06 at 2 29 23 PM" src="https://user-images.githubusercontent.com/107584457/206038018-728823f5-3876-4fc4-85ec-ddb511dc0b12.png">
<img width="1435" alt="Screen Shot 2022-12-06 at 2 29 44 PM" src="https://user-images.githubusercontent.com/107584457/206038020-914e9e47-937e-4933-93c5-e5d606753111.png">



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

# how to run this code  :
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
