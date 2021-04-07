from django import forms
from .models import *

# お問い合わせフォーム作成用
class ContactForm(forms.Form):
    name = forms.CharField(label='お名前', max_length=50)
    email = forms.EmailField(label='メールアドレス', help_text='※ご確認の上、正しく入力してください。')
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)
    myself = forms.BooleanField(label='内容を受け取る', required=False)

class book_stock_form(forms.ModelForm):
    class  Meta:
        model = Book_stock
        fields =[
            'title',
            'isbnCord',
            'author',
            'bookYearOfIssue',
            'money',
            'numBooks',
            'majorClass',
            'middleClass'
            ]
        labels = {
            'title':'タイトル',
            'isbnCord':'ISBN',
            'author':'著者',
            'bookYearOfIssue':'発行年月日',
            'money':'金額',
            'numBooks':'冊数',
            'majorClass':'大分類',
            'middleClass':'中分類'
        }
        widgets = {
        }

class book_details_form(forms.ModelForm):
    class Meta:
        model = Book_details
        fields=[
            'bookDetails',
            'bookStatus'
        ]
        labels={
            'bookDetails':'本の詳細情報',
            'bookStatus':'本の状態'
        }
        widgets={
            'bookDetails':''
        }