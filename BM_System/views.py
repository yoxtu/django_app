from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    params = {
        'title': 'BM_System',
        'data':'data',
    }
    return render(request, 'BM_System/index.html',params)