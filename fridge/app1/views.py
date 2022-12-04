import collections
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
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime
import timeago


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
    counterexpired = 0
    counterwarning = 0
    countergood = 0
    statusexpired = ''
    statuswarning = ''
    statusgood = ''
    totalwasted = 0
    totalcost = 0
    count = 0
    total = Item.objects.filter(author=request.user.id).all().count
    countermeat = Item.objects.filter(author=request.user.id).filter(food_type = 'meat')
    counterdairy = Item.objects.filter(author=request.user.id).filter(food_type = 'dairy')
    counterbeverages = Item.objects.filter(author=request.user.id).filter(food_type = 'beverages')
    counterfrozveg = Item.objects.filter(author=request.user.id).filter(food_type = 'frozen vegetables')
    counterfruits = Item.objects.filter(author=request.user.id).filter(food_type = 'fruits')
    prices = Item.objects.filter(author=request.user.id).values('price')
    
    for item in items:
        three_days_from_today = date.today()+timedelta(days=3)
        today = date.today()
        valid_to = item.valid_to

        #<-------Find Time-Ago Format------->
        valid_date = valid_to
        # For Expired
        # Today's Date + Time
        right_now = datetime.now()
        now = right_now.strftime('%Y-%m-%d %H:%M:%S')
        # Item Expired Date + Time
        valid = valid_date.strftime('%Y-%m-%d %H:%M:%S')
        item.humanize_time = (timeago.format(valid, now))

        # For Warning
        valid_date1 = valid_to
        right_now1 = datetime.now()
        add_days = right_now1 + timedelta(days = 3)
        now1 = add_days.strftime('%Y-%m-%d %H:%M:%S')
        # Item Expired Date + Time
        valid1 = valid_date1.strftime('%Y-%m-%d %H:%M:%S')
        item.humanize_time1 = (timeago.format(valid1, now1))


        #<-------Filter-Data-only------->
        exp = Item.objects.filter(status = 'Expired')

        #<-------Filter-Data-only------->
        totalcost = 0
        for p in prices:
            totalcost += p['price']
            
        if valid_to < today:
            item.status = 'Expired'
            totalwasted += item.price
            counterexpired += 1
            exp = Item.objects.filter(author=request.user.id).filter(status = 'Expired').values('price')
            statusexpired = (item,exp)

        elif valid_to <= three_days_from_today:
            
            item.status = 'Warning'
            count += item.price
            counterwarning += 1
            item.daystill = (item.valid_to - date.today()).days


        else:
            
            item.status = 'Good'
            countergood  += 1
            goo = Item.objects.filter(author=request.user.id).filter(status = 'Good')
            statusgood = (item,goo)
    totalcount = counterexpired + counterwarning



    context = {
        'items': items,
        'totalcost': totalcost,
        'counterwarning': counterwarning,
        'countergood': countergood,
        'countermeat': countermeat,
        'counterdairy': counterdairy,
        'counterbeverages': counterbeverages,
        'counterfrozveg': counterfrozveg,
        'counterfruits': counterfruits,
        'statusexpired': statusexpired,
        'statuswarning': statuswarning,
        'statusgood': statusgood,
        'totalcount': totalcount,
        'totalwasted':totalwasted,
        'count':count,
        'total' : total,
        'counterexpired':counterexpired,
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
            username = request.POST['username']
            email = request.POST['email']
            subject = 'Welcome to Fridge'
            message = f'Hi, {username} we will help you to setup your Fridge'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email] 
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f"Your account has been created! {username} you are now able to login")
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

@login_required
def about(request):
      
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "about.html")

def chart(request):
    get_all1 = Item.objects.filter(author=request.user.id).all()
    get_price_d = Item.objects.filter(author=request.user.id).values('price').filter(food_type = 'dairy')
    get_price_f = Item.objects.filter(author=request.user.id).values('price').filter(food_type = 'fruits')
    get_price_m = Item.objects.filter(author=request.user.id).values('price').filter(food_type = 'meat')
    get_price_b = Item.objects.filter(author=request.user.id).values('price').filter(food_type = 'beverages')
    get_price_fv = Item.objects.filter(author=request.user.id).values('price').filter(food_type = 'frozen vegetables')

    # get_data = Item.objects.filter(author=request.user.id).values('food_type')
    for all in get_all1:
        #Meat
        p_meat = 0
        for pm in get_price_m:
            p_meat += pm['price']

         #Dairy
        p_dairy = 0
        if all.food_type == 'dairy':
             for pd in get_price_d:
                 p_dairy += pd['price']

        #Fruits
        p_fruits = 0
        for pf in get_price_f:
            p_fruits += pf['price']

        #Beverages
        p_beverages = 0
        for pb in get_price_b:
            p_beverages  += pb['price']

        #Frozen Vegetables
        p_frozenveg = 0
        for pfv in get_price_fv:
            p_frozenveg  += pfv['price']
        

    # render function takes argument  - request
    # and return HTML as response
    return render(request, "chart_test.html",context={
        'p_dairy':p_dairy,
        'p_frozenveg':p_frozenveg,
        'p_beverages':p_beverages,
        'p_meat':p_meat,
        'p_fruits':p_fruits,
        'get_price_d':get_price_d,
        'get_price_f':get_price_f,
        'get_price_m':get_price_m,
        'get_price_b':get_price_b,
        'get_price_fv':get_price_fv,
        'get_all1':get_all1,
    })
@login_required
def chart1(request):
    TotalExpense = 0
    totalwaste = 0
    a = Item.objects.filter(author=request.user.id).order_by('valid_to')
    for v in a:
        today = date.today()
        valid_to = v.valid_to
        if valid_to < today:
            v.status = 'Expired'
            totalwaste += v.price
    Total = Item.objects.filter(author=request.user.id).values('price')
    for t in Total:
        TotalExpense += t['price']
    
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "chart_test1.html",context={
        'totalwaste':totalwaste,
        'TotalExpense':TotalExpense,
        'Total': Total,
        'a': a,
    })
@login_required
def chart2(request):
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
    counterexpired = 0
    counterwarning = 0
    countergood = 0
    statusexpired = ''
    statuswarning = ''
    statusgood = ''
    totalwasted = 0
    count = 0
    hello = ''
    total = Item.objects.filter(author=request.user.id).all().count
    countermeat = Item.objects.filter(author=request.user.id).filter(food_type = 'meat')
    counterdairy = Item.objects.filter(author=request.user.id).filter(food_type = 'dairy')
    counterbeverages = Item.objects.filter(author=request.user.id).filter(food_type = 'beverages')
    counterfrozveg = Item.objects.filter(author=request.user.id).filter(food_type = 'frozen vegetables')
    counterfruits = Item.objects.filter(author=request.user.id).filter(food_type = 'fruits')
    prices = Item.objects.filter(author=request.user.id).values('price')
    f = 0
    th = 0
    m = 0
    t = 0
    w = 0
    s = 0
    sun = 0
    for item in items:
        three_days_from_today = date.today()+timedelta(days=3)
        today = date.today()
        valid_to = item.valid_to

        #<-------Find Time-Ago Format------->
        valid_date = valid_to
        # For Expired
        # Today's Date + Time
        right_now = datetime.now()
        now = right_now.strftime('%Y-%m-%d %H:%M:%S')
        # Item Expired Date + Time
        valid = valid_date.strftime('%Y-%m-%d %H:%M:%S')
        item.humanize_time = (timeago.format(valid, now))

        # For Warning
        valid_date1 = valid_to
        right_now1 = datetime.now()
        add_days = right_now1 + timedelta(days = 3)
        now1 = add_days.strftime('%Y-%m-%d %H:%M:%S')
        # Item Expired Date + Time
        valid1 = valid_date1.strftime('%Y-%m-%d %H:%M:%S')
        item.humanize_time1 = (timeago.format(valid1, now1))


        #<-------Filter-Data-only------->
        exp = Item.objects.filter(status = 'Expired')

        #<-------Filter-Data-only------->
        totalcost = 0
        for p in prices:
            totalcost += p['price']
            
        if valid_to < today:
            item.status = 'Expired'
            totalwasted += item.price
            counterexpired += 1
            exp = Item.objects.filter(author=request.user.id).filter(status = 'Expired').values('price')
            statusexpired = (item,exp)

            daym = "Monday"
            dt = item.valid_to
            # get weekday name
            yes = (dt.strftime('%A'))
            if daym == yes:
                m += 1

            dayt = "Tuesday"
            dt = item.valid_to
            # get weekday name
            yes = (dt.strftime('%A'))
            if dayt == yes:
                t += 1

            dayw = "Wednesday"
            dt = item.valid_to
            # get weekday name
            yes = (dt.strftime('%A'))
            if dayw == yes:
                w += 1

            dayth = "Thursday"
            dt = item.valid_to
            # get weekday name
            yes = (dt.strftime('%A'))
            if dayth == yes:
                th += 1

            dayf = "Friday"
            dt = item.valid_to
            # get weekday name
            yes = (dt.strftime('%A'))
            if dayf == yes:
                f += 1

            days = "Saturday"
            dt = item.valid_to
            # get weekday name
            yes = (dt.strftime('%A'))
            if days == yes:
                s += 1

            daysun = "Sunday"
            dt = item.valid_to
            # get weekday name
            yes = (dt.strftime('%A'))
            if daysun == yes:
                sun += 1
            

        elif valid_to <= three_days_from_today:
            
            item.status = 'Warning'
            hello =  (item.food_title)
            count += item.price
            counterwarning += 1
            war = Item.objects.filter(author=request.user.id).filter(status = 'Warning')
            item.daystill = (item.valid_to - date.today()).days



        else:
            
            item.status = 'Good'
            countergood  += 1
            goo = Item.objects.filter(author=request.user.id).filter(status = 'Good')
            statusgood = (item,goo)
    totalcount = counterexpired + counterwarning



    context = {
        'items': items,
        'totalcost': totalcost,
        'counterwarning': counterwarning,
        'countergood': countergood,
        'countermeat': countermeat,
        'counterdairy': counterdairy,
        'counterbeverages': counterbeverages,
        'counterfrozveg': counterfrozveg,
        'counterfruits': counterfruits,
        'statusexpired': statusexpired,
        'statuswarning': statuswarning,
        'statusgood': statusgood,
        'totalcount': totalcount,
        'totalwasted':totalwasted,
        'count':count,
        'total' : total,
        'hello':hello,
        'counterexpired':counterexpired,
        'form': form,
        'f':f,
        'th':th,
        'm':m,
        't':t,
        'w':w,
        's':s,
        'sun':sun,

    }
    return render(request, 'chart_test2.html', context)