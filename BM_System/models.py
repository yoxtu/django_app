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
            ' 冊数:'+ str(self.number_books)


"""
Book_stockに必要なデータ

id(タイトル別)
タイトル
著者名
冊数
発行年

--new sql--

id(タイトル別)
isbn
タイトル
著者名


"""
"""
user→借りる→idを記入
id参照→返す→userから消す

---new sql---
title（大きなDB）：タイトル、isbn、著者名.book（本ごとのデータ）


"""