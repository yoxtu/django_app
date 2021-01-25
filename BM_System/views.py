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
        'date':book,
    }
    return render(request, 'BM_System/stock.html',params)

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
    user_title_list = make_list(user.profile.book_title)
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

# お問い合わせ作成
@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = "お問い合わせ内容:\n" + form.cleaned_data['message']
            email = form.cleaned_data['email']
            myself = form.cleaned_data['myself']
            recipients = settings.EMAIL_HOST_ADMIN
            recipients.append(settings.EMAIL_HOST_USER)
            if myself:
                return_msg = "お問い合わせありがとうございます。\n" + message + "\nお問い合わせいただき、ありがとうございました。"
                send_mail("BMシステムへのお問い合わせ",return_msg,email,[email])
            message += str(Import_mail_template(request.user,email))
            try:
                send_mail(name, message, email, recipients)
            except BadHeaderError:
                return HttpResponse('無効なヘッダーが見つかりました。')
            return redirect('done')
    else:
        form = ContactForm()
    params = {
        'title' : 'お問い合わせ',
        'user_name':str(request.user),
        'user_staff' : request.user.is_staff,
        'form' : form
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

