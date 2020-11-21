from django.urls import path
from . import views

urlpatterns = [
    path('CalcPayment', views.CalcPayment, name='CalcPayment'),
    # path('index', views.index, name='index'),
]