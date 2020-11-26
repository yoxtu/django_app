from django.urls import path
from . import views


urlpatterns = [
    path('calc-payment/', views.calcPaymentEX, name='form'),
]