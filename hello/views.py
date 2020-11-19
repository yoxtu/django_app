from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Friend
from .forms import FriendForm

def index(request):
    data = Friend.objects.all()
    params = {
        'title': 'HELLO',
        'data':data,
    }
    return render(request, 'hello/index.html',params)
# Create your views here.
# Create model
def create(request):
    if (request.method == 'POST'):
        obj = Friend()
        friend.save()
        return redirect(to='/hello')
    params = {
        'title':'Hello',
        'form':FriendForm(),
    }
    return render(request,'hello/create.html',params)

def edit(request,num):
    obj = Friend.objects.get(id = num)
    if (request.method == 'POST'):
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'title':'HELLo',
        'id': num,
        'form':FriendForm(instance=obj),
    }
    return render(request, 'hello/edit.html',params)

