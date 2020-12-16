from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('stock',views.stock,name='stock'),
    path('lending',views.lending,name='lending'),
    path('login',views.login,name='login'),
    path('contact',views.contact,name='contact')
]