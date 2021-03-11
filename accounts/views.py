from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.db import transaction
from BM_System import processing
from django.shortcuts import *
from .forms import *


# Create your views here.           

class MyLoginView(LoginView):
    form_class = LoginForm
    template_name = "accounts/login.html"

class MyLogoutView(LoginRequiredMixin, LogoutView):
    template_name = "accounts/logout.html"

class IndexView(TemplateView):
    template_name = "BM_System/home.html"

def create_info(request):
    user_form = UserCreationForm(request.POST or None)
    profile_form = account_info(request.POST or None)
    if request.method == "POST" and user_form.is_valid() and profile_form.is_valid():
        if processing.exist_submit_token(request):
            # Userモデルの処理。ログインできるようis_activeをTrueにし保存
            user = user_form.save(commit=False)
            user.is_active = True
            user.save()

            # Profileモデルの処理。↑のUserモデルと紐づけましょう。
            profile = profile_form.save(commit=False)
            profile.gender = profile_form.cleaned_data["gender"]
            profile.age = profile_form.cleaned_data["age"]
            profile.birth_date = profile_form.cleaned_data["birthday"]
            profile.book_title = None
            profile.user = user
            profile.save()

            # ログイン
            login_user = authenticate(username=user.username, password=user.password)
            login(request, user)
            return redirect("stock")
    submit_token = processing.set_submit_token(request)
    data = {
        "form1": user_form,
        "form2": profile_form,
        'submit_token': submit_token,
    }
    return render(request, 'accounts/create.html', data)


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


