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
        'data':'data',
    }
    return render(request, 'BM_System/index.html',params)

def lending(request):
    params = {
        'title': 'BM_System',
        'data':'data',
    }
    return render(request, 'BM_System/index.html',params)

def login(request):
    params = {
        'title': 'BM_System',
        'data':'data',
    }
    return render(request, 'BM_System/index.html',params)

def contact(request):
    params = {
        'title': 'BM_System',
        'data':'data',
    }
    return render(request, 'BM_System/index.html',params)