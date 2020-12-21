from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    params = {
        'title': 'BM_System',
        'data':'data',
    }
    return render(request, 'BM_System/index.html',params)

def stock(request):
    params = {
        'title': 'BM_System',
    }
    return render(request, 'BM_System/stock.html',params)

def lending(request):
    params = {
        'title': 'BM_System',
    }
    return render(request, 'BM_System/lending.html',params)

def login(request):
    params = {
        'title': 'BM_System',
    }
    return render(request, 'BM_System/login.html',params)

def contact(request):
    params = {
        'title': 'BM_System',
    }
    return render(request, 'BM_System/contact.html',params)