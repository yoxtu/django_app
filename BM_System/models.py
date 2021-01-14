from django.db import models

# Create your models here.

class Book_stock(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year_issue = models.DateField()
    number_books = models.IntegerField(default=0)
    registration_date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return 'id:' + str(self.id)+ ' タイトル:' + self.title+ ' 著者名:'+ self.author+ ' 発行年:'+ str(self.year_issue)+\
            ' 冊数:'+ str(self.number_books)+ ' 登録日:'+ str(self.registration_date)



