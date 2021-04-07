from django.urls import path
from . import views

# app_name = 'BM_System'
urlpatterns = [
    path('',views.home,name='home'),#ホームのサイト
    path('stock/',views.stock,name='stock'),#本の一覧（ログイン後）
    path('lending/',views.lending,name='lending'),#（ログイン後）
    path('lended/<int:ID>', views.lended, name = 'lended' ),#（ログイン後）
    path('contact/',views.contact,name='contact'),#（ログイン後）
    path('contact/done/',views.done,name='done'), #（ログイン後）
    path('book_return/<int:ID>', views.bookReturn,name = 'book_return'),#（ログイン後）
    path('management/',views.management,name='management'),#本のデータを追加
    path('serch/', views.bookserch, name = 'serch'),#検索用
]