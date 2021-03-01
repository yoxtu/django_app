from django.db import models
from django.core import validators

# Create your models here.

class Book_stock(models.Model):
    title = models.CharField(max_length=100)
    isbnCord = models.IntegerField(max_length=13)
    author = models.CharField(max_length=60)
    bookYearOfIssue = models.DateField(auto_now = False,auto_now_add = False)
    systemRegistDay = models.DateField(auto_now_add=True)
    money = models.IntegerField(default=0)
    numBooks = models.IntegerField(default=0)
    majorClass = models.IntegerField( default=0,
        validators=[validators.MinLengthValidator(0),
                    validators.MaxLengthValidator(3)])
    middleClass = models.IntegerField( default=0,
        validators=[validators.MinLengthValidator(0),
                    validators.MaxLengthValidator(3)])
    def __str__(self):
        return 'id:' + str(self.id)+ ' タイトル:' + self.title+ 'djangoBookID :'+ str(self.djangoBookID)+ ' isbnCord:'+ str(self.isbnCord)+\
            '\n 登録日:'+ self.systemRegistDay+ ' 冊数:'+ str(self.numBooks)+ ' 大分類:'+str(self.majorClass)+ ' 中分類:'+str(self.middleClass)

class Book_details(models.Model):
    djangoBookID = models.IntegerField(default=0)
    bookID = models.IntegerField(max_length=999)
    registDay = models.DateField(auto_now_add=True)
    bookDetails = models.CharField(max_length=400)
    bookStatus = models.CharField(max_length=10)
    def __str__(self):
        return 'djangoBookID:' + str(self.djangoBookID) + ' bookID:'+ str(self.bookID) + ' 登録日:' + self.registDay +' 本の詳細情報:' + self.bookDetails +\
        ' \n本の状態:' + str(self.bookStatus)

class Lending_log(models.Model):
    userDjangoID = models.IntegerField(default=0)
    user = models.CharField(max_length=10)
    eMail = models.EmailField(max_length = 254)
    borrowedBook = models.CharField(max_length=100)
    bookDjangoID = models.IntegerField(default=0)
    someProcessing = models.CharField(max_length=10)
    processingDay = models.DateField(auto_now_add=True)
    returnDay = models.CharField(max_length=10, blank=True)
    borrowedDay = models.CharField(max_length=10,blank=True)
    def __str__(self):
        return 'userDjangoID:' + str(self.userDjangoID) + ' bookDjangoID:'+ str(self.bookDjangoID) + ' user:'+ self.user + '様'+ ' メール:' + self.eMail +\
            ' \n借りた本:' + self.borrowedBook + ' 処理内容:' + self.someProcessing + ' 返却日:'+ self.returnDay+ ' 借りた日' + self.borrowedDay


"""
Book_stockに必要なデータ

id(タイトル別)
タイトル
著者名
冊数
発行年

返す時の処理順序
1．ユーザ側が本のISBNCordを使用し返却申請をする
（isbn→本の特定→リクエストフィールドをtrue→終了）
2．ユーザ側は返却ボックスに返却申請した本を投函する
3．admin側は申請された本のリストを確認or却下を判断してボタンを押下する
4―a、返却申請された本の確認された趣旨のメッセージが届く
4‐b、本の返却申請が却下された場合、その旨のメッセージが届き対応しなければならない
（理由も表示させる）

借りる時の処理順序
1．ユーザ側が本のISBNCordを読み取り、借りるボタンを押す
（借りれる本は3冊）

"""