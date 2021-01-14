from django.db import models

class Friend(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=200)
    gender = models.BooleanField()
    age = models.IntegerField(default=0)
    birthday = models.DateField()

    def __str__(self):
        return '<Friend:id=' + str(self.id) + ',' + self.name + '(' + str(self.age) + ')>'

class Books(models.Model):
    book_name = models.CharField('書籍名', max_length=50)
    publisher = models.CharField('出版社', max_length=50)
    page = models.CharField('ページ', max_length=50)

    def __str__(self):
        return '<Book=' + self.book_name + ',' + self.name + ',' + str(self.page) + '>'
# Create your models here.
