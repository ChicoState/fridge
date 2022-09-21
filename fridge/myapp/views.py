from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request, page=0):
    #return HttpResponse("CSCI430 Hello World")
    page_list = list(range(page*10, page*10 + 10, 1))
    squares_list = [x**2 for x in range(10)]
    context = {
        'first_name': 'Fri',
        'last_name': 'dge',
        'title': 'CSCI430',
        'msg': 'Hello World',
        'page_list': page_list,
        'squares_list': squares_list,
        'prev_page': page - 1,
        'next_page': page + 1,
    }
    return render(request, "index.html", context=context)