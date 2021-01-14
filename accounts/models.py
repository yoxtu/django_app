from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # name
    # mail
    # password
    std_num = models.CharField(max_length=10)
    gender = models.CharField(max_length=1)
    birth_date = models.DateField(null=True, blank=True)
    age = models.IntegerField(default=0)
    book_title = models.CharField(max_length=100,null=True, blank=True)