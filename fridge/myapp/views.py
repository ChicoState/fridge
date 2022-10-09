import datetime
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import JoinForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from myapp.forms import JoinForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from myapp.models import foodItem
from myapp.forms import FoodItemForm
from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url='/login/')
def index(request, page=0):
    if (request.method == "GET" and "delete" in request.GET):
        id = request.GET["delete"]
        foodItem.objects.filter(id=id).delete()
        return redirect("/")
    else:
        table_data = foodItem.objects.filter(user=request.user)
        page_list = list(range(page*10, page*10 + 10, 1))
        squares_list = [x**2 for x in range(10)]
        context = {
            'first_name': 'Fri',
            'last_name': 'dge',
            'title': 'Fridge',
            'msg': 'Hello World',
            'page_list': page_list,
            'squares_list': squares_list,
            'prev_page': page - 1,
            'next_page': page + 1,
            "table_data": table_data,
        }
        return render(request, "myapp/index.html", context=context)


def join(request):
    if (request.method == "POST"):
        join_form = JoinForm(request.POST)
        if (join_form.is_valid()):
            # Save form data to DB
            user = join_form.save()
            # Encrypt the password
            user.set_password(user.password)
            # Save encrypted password to DB
            user.save()
            # Success! Redirect to home page.
            return redirect("/")
        else:
            # Form invalid, print errors to console
            page_data = { "join_form": join_form }
            return render(request, 'myapp/join.html', page_data)
    else:
        join_form = JoinForm()
        page_data = { "join_form": join_form }
        return render(request, 'myapp/join.html', page_data)


def user_login(request):
    if (request.method == 'POST'):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # First get the username and password supplied
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            # Django's built-in authentication function:
            user = authenticate(username=username, password=password)
            # If we have a user
            if user:
                #Check it the account is active
                if user.is_active:
                    # Log the user in.
                    login(request,user)
                    # Send the user back to homepage
                    return redirect("/")
                else:
                    # If account is not active:
                    return HttpResponse("Your account is not active.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username,password))
                return render(request, 'myapp/login.html', {"login_form": LoginForm})
    else:
        #Nothing has been provided for username or password.
        return render(request, 'myapp/login.html', {"login_form": LoginForm})

# def index(request):
#     form = FoodItemForm()
#     return render(request, 'myapp/index.html',{'form':form})

@login_required(login_url='/login/')
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return redirect("/")


@login_required(login_url='/login/')
def add(request):
    if (request.method == "POST"):
        if ("add" in request.POST):
            add_form = FoodItemForm(request.POST)
            if (add_form.is_valid()):
                description = add_form.cleaned_data["description"]
                price = add_form.cleaned_data['price']
                expiredate = add_form.cleaned_data['expiredate']
                user = User.objects.get(id=request.user.id)
                foodItem(user=user, description=description, price=price, expiredate=expiredate).save()
                return redirect("/")
            else:
                context = {
                "form_data": add_form
                }
                return render(request, 'myapp/add.html', context)
        else:
                # Cancel
            return redirect("/")
    else:
        context = {
                "form_data": FoodItemForm()
                        }
    return render(request, 'myapp/add.html', context)

