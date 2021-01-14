from django.urls import path
from . import views

# app_name = 'BM_System'
urlpatterns = [
    path('',views.home,name='home'),
    path('stock/',views.stock,name='stock'),
    path('lended/<int:num>', views.lended, name = 'lended' ),
    path('lending/',views.lending,name='lending'),
    path('contact/',views.contact,name='contact'),
    path('contact/done/',views.done,name='done'), 
    # path('management/',vews.management,name='management'),
]