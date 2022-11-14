from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404
from app1.forms import ItemForm
from app1.models import Item, Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from datetime import timedelta, date
from django.http import JsonResponse


# Create your views here.
@login_required
def list_item(request):
    items = Item.objects.filter(author=request.user.id).order_by('valid_to')
    # data  = Item.objects.filter(author=request.user.id)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            # Return an object without saving to the DB
            obj = form.save(commit=False)
            obj.author = Profile.objects.get(
                id=request.user.id)  # Add an author field which will contain current user's id
            obj.save()  #

        messages.success(request, "Successfully Item added...!!!")
        return redirect('item_list')

    else:
        form = ItemForm()

    for item in items:
        three_days_from_today = date.today()+timedelta(days=3)
        today = date.today()
        valid_to = item.valid_to
        count_rows = (len(items)) 
        total = Item.objects.all().count

        #<-------Status-only------->
        # meat = Item.objects.filter(food_type = 'meat')
        # fruits = Item.objects.filters(food_type = 'fruits')
        expired = Item.objects.filter(status = 'Expired')
        warning = Item.objects.filter(status = 'Warning')
        good = Item.objects.filter(status = 'Good')



        # check_status_count = Item.objects.filter(author=request.user.id).values('status')
        # countstatus = 0
        # for s in check_status_count:
        #     if(s.status == 'Expired'):
        #         countstatus += s['status']
        #     print(countstatus)

        prices = Item.objects.filter(author=request.user.id).values('price')
        totalcost = 0
        for p in prices:
            totalcost += p['price']

        if valid_to < today:
            item.status = 'Expired'

        elif valid_to <= three_days_from_today:
            item.status = 'Warning'
        else:
            item.status = 'Good'

    context = {
        'items': items,
        'totalcost': totalcost,
        'warning': warning,
        'good': good,
        'expired':expired,
        'count_rows' : count_rows,
        'form': form,
    }
    return render(request, 'index.html', context)

@login_required
def item_update(request, pk):
    data = get_object_or_404(Item, pk=pk, author=request.user.id)
    form = ItemForm(instance=data)
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated item ...!!!")
            return redirect('item_list')
    context = {
        "form": form
    }
    return render(request, 'update_item.html', context)


def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        messages.success(request, "Successfully deleted item ...!!!")
        return redirect('item_list')
    return render(request, 'delete_item.html', {'object': item})

# Search Functionality
def search(request):
    items = Item.objects.order_by('valid_to')
    print(items)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()

    # search items by title(name), type(dairy,meat etc...)
    qs = Item.objects.filter(author=request.user.id).order_by('valid_to')
    query = request.GET.get('q')

    if query:
        qs = qs.filter(
            Q(food_title__icontains=query) |
            Q(food_type__icontains=query) |
            Q(valid_from__icontains=query) |
            Q(valid_to__icontains=query)
        ).distinct()
        if query and qs:
            messages.success(
                request, "Search Item found '%s' ...!!!" % (query))
        else:
            messages.warning(request, "Search Item Not found '%s' ...!!!" % (query),
                             "search another Item...???")


    for item in qs:
        three_days_from_today = date.today()+timedelta(days=3)
        today = date.today()
        valid_to = item.valid_to

        if valid_to < today:
            item.status = 'Expired'
        elif valid_to <= three_days_from_today:
            item.status = 'Warning'
        else:
            item.status = 'Good'

    context = {
        "item_obj": qs,
        'form': form,
    }

    return render(request, 'search_results.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f"Your account has been created! {username} your now able to login")
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect('profile_update')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "u_form": u_form,
        "p_form": p_form
    }
    return render(request, 'my_account.html', context)


@login_required(login_url='/login/')
def meals(request):
    context = {
        'title': "Reccomended Meals",
    }
    return render(request, 'meals.html', context=context)


@login_required(login_url='/login/')
def recipes(request):
    context = {
        'title': "Reccomended Recipes",
    }
    return render(request, 'recipes.html', context=context)


@login_required
def item_update_quantity(request, pk):
    """Update item quantity view.

    method: POST
    """
    if request.method == "POST":
        # Here we will get value of quantity, that is given with the request
        # the data that is passed through form-data can be accessed as below.
        quantity = request.POST.get("quantity", None)
        if quantity:
            obj = get_object_or_404(Item, pk=pk)
            obj.quantity = quantity  # this will just update the value in object
            obj.save()  # This call the db operation, and update the quantity
            return JsonResponse(status=200, data={"id": pk, "quantity": quantity})
            # The below two responses can be ignored if you don't want.
            # but it is a good practice to have them, these errors can be handled from
            # client. Anyway these will not occur in this current situation.
        return JsonResponse(status=400, data={"message": "quantity is required!"})
    return JsonResponse(status=405, data={"message": "only post requests are allowed"})
