from django.shortcuts import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#追加 お問い合わせ時
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from .forms import ContactForm
from BM_System.processing import *
# ここまで

from .models import Book_stock
from accounts.models import Profile

from django.db import transaction

# 検索
from django.views.generic import ListView
from django.db.models import Q

# Create your views here.


def home(request):
    params = {
        'title': 'BM_System',
        'data':'data',
        'user_name':str(request.user),
        'user_staff' : request.user.is_staff,
    }
    return render(request, 'BM_System/home.html',params)

# 貸出処理
@login_required
def stock(request):
    book = Book_stock.objects.all()
    params = {
        'title': '在庫一覧',
        'user_name':str(request.user),
        'user_staff' : request.user.is_staff,
        'data':book,
    }
    return render(request, 'BM_System/stock.html',params)

"""
借りる時の処理順序
前提　本は一冊以上あること、カメラのversionは考慮しない、借りている本が3冊未満
1．ユーザ側が本の借りるボタンを押下
2．カメラを起動し、バーコードを読み取る
3.システムは、読み取ったバーコードがDBにあるかどうか判定する
4－1．あった場合、システムはuserにISBNCordを追加、Book_stockから一冊引きsaveする
4－2．なかった場合、実行しない

"""
@login_required
@transaction.atomic
def lended(request, ID):
    lend_jage = False
    book_obj = Book_stock.objects.get(id = ID)
    user = User.objects.get(id = request.user.id)
    lender_list = list_check(make_list(user.profile.book_title))
    if len(lender_list) < 3:
        if book_obj.number_books >= 1:
            # 本から冊数を引く
            book_obj.number_books -= 1
            # Profileにtitleを足す処理
            if serch_list(lender_list,str(ID)):
                lender_list.append(str(ID))
                user.profile.book_title = make_text(lender_list)
                # セーブする
                user.profile.save()
                book_obj.save()
                # 成否をする
                lend_jage = True
            else:
                messege = ''
    paramas = {
        'title':book_obj,
        'lend_jage':lend_jage,
        'book_number': len(make_list(user.profile.book_title))
    }
    return render(request, 'BM_System/stock_after.html',paramas)

# 貸出処理ここまで
@login_required
def lending(request):
    user = User.objects.get(id = request.user.id)
    user_title_list = make_list(user.profile.isbn)
    title_list = []
    user_title_list = list_check(user_title_list)
    for i in user_title_list:
        title_list.append(Book_stock.objects.get(id = i))
    params = {
        'title': '貸し出し状況',
        'title_list': title_list,
        'user_name':str(request.user),
        'user_staff' : request.user.is_staff,
    }
    return render(request, 'BM_System/lending.html',params)

# 返す処理
@login_required
@transaction.atomic
def bookReturn(request, ID):
    book = Book_stock.objects.get(id = ID)
    book.number_books += 1
    user = User.objects.get(id = request.user.id)
    return_list = list_check(make_list(user.profile.book_title),ID)
    user.profile.book_title = make_text(return_list)
    user.profile.save()
    book.save()
    judg = True
    params = {
        'judg' : judg,
        'book_title' : str(book),
        'userName' : str(request.user),
        'user_staff' : request.user.is_staff,
        'book_number': len(make_list(user.profile.book_title))
    }
    return render(request, 'BM_System/lending_after.html',params)

    # if request.method == "POST":
    #     if security.exist_submit_token(request):
    #         comment = '正常にクリックが行われました'	
    #     else:
    #         comment = '多重クリックが行われました'
    # else:
    #     comment = 'クリックの判定を行います'
    # submit_token = security.set_submit_token(request)
    # context = {
    #     'comment': comment,
    #     'submit_token': submit_token,
    # }
    # return render(request, 'app/test_token_check.html', context)

# お問い合わせ作成
@login_required
def contact(request):
    form = ContactForm(request.POST or None)
    error_msg = ""
    if request.method == 'POST':
        if not exist_submit_token(request):
            # Error
            error_msg = "トークンが正しくありません。もう一度やり直してください。"
        else:
            if form.is_valid():
                name = form.cleaned_data['name']
                user = User.objects.get(id = request.user.id)
                message = "お問い合わせ内容:\n" + form.cleaned_data['message']
                email = form.cleaned_data['email']
                myself = form.cleaned_data['myself']
                recipients = settings.EMAIL_HOST_ADMIN
                recipients.append(settings.EMAIL_HOST_USER)
                if myself:
                    return_msg = "お問い合わせありがとうございます。\n" + message + "\nお問い合わせいただき、ありがとうございました。"
                    send_mail("BMシステムへのお問い合わせ",return_msg,email,[email])
                message += str(Import_mail_template(request.user ,email ,user.profile.std_num))
                try:
                    send_mail(name, message, email, recipients)
                except BadHeaderError:
                    return HttpResponse('無効なヘッダーが見つかりました。')
                return redirect('done')
    else:
        form = ContactForm()
    submit_token = set_submit_token(request)
    params = {
        'title' : 'お問い合わせ',
        'user_name':str(request.user),
        'user_staff' : request.user.is_staff,
        'form' : form,
        'submit_token' : submit_token,
        'error_msg' : error_msg, 
    }
    return render(request, 'BM_System/contact.html',params)

@login_required
def done(request):
    params = {
        'title' : '完了',
        'user_name':str(request.user),
        'user_staff' : request.user.is_staff,
    }
    return render(request, 'BM_System/done.html', params)

# ここまで

# 検索用関数
def bookserch(request):
    book = Book_stock.objects.order_by('-id')
    q_word = request.GET.get('query')
    if q_word:
        data = Book_stock.objects.filter(
            Q(title__icontains=q_word) | Q(author__icontains=q_word)
        )
    else:
        data = Book_stock.objects.all()
    params = {
        'user_staff' : request.user.is_staff,
        'data': data,
    }
    return render(request, 'BM_System/stock.html',params)
# ここまで