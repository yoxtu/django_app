from django.contrib import admin
from .models import Book_stock,Book_details,Lending_log

# Register your models here.

admin.site.register(Book_stock)
admin.site.register(Book_details)
admin.site.register(Lending_log)