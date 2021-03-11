from django.db import models
from django.core import validators


# Create your models here.

from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="profile")
    # name
    # mail
    # password
    studentNum = models.CharField(max_length=10)
    gender = models.CharField(max_length=5)
    birthday = models.DateField(null=True, blank=True)
    age = models.IntegerField(default=0)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return '学番:' + self.studentNum + ' 性別:'+ self.gender + ' 年齢:' + str(self.age) + '歳' +\
            ' \n借りている本:' + str(self.isbn)