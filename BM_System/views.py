from django.shortcuts import *
from django.http import HttpResponse

#追加 お問い合わせ時
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from .forms import ContactForm
from BM_System.processing import *
# ここまで

# Create your views here.


def home(request):
    params = {
        'title': 'BM_System',
        'data':'data',
        'user_name' : str(request.user) 
    }
    return render(request, 'BM_System/home.html',params)

def stock(request):
    params = {
        'title': '在庫一覧',
        'user_name' : str(request.user) 
    }
    return render(request, 'BM_System/stock.html',params)

def lending(request):
    params = {
        'title': '貸し出し状況',
        'user_name' : str(request.user) 
    }
    return render(request, 'BM_System/lending.html',params)

# お問い合わせ作成

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
            return redirect('contact/done')
    else:
        form = ContactForm()
    params = {
        'title' : 'お問い合わせ',
        'user_name' :  str(request.user),
        'form' : form
    }
    return render(request, 'BM_System/contact.html',params)

def done(request):
    params = {
        'title' : '完了',
        'user_name' : str(request.user),
    }
    return render(request, 'BM_System/done.html')

# ここまで