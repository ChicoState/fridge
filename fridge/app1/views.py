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
        days_left = (item.valid_to - item.valid_from).days
        print("Days left: ",days_left)

        if valid_to < today:
            item.status = 'Expired'
        elif valid_to <= three_days_from_today:
            item.status = 'Warning'
        else:
            item.status = 'Good'

    context = {
        'items': items,
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
    print(qs)
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
