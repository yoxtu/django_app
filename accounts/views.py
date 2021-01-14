from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,CreateView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.db import transaction
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

        # Userモデルの処理。ログインできるようis_activeをTrueにし保存
        user = user_form.save(commit=False)
        user.is_active = True
        user.save()

        # Profileモデルの処理。↑のUserモデルと紐づけましょう。
        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()
        return redirect("stock")

    context = {
        "form1": user_form,
        "form2": profile_form,
    }
    return render(request, 'accounts/create.html', context)






















# class UserCreateView(CreateView):
#     form_class = UserCreationForm
#     form_class2 = account_info
#     template_name = "accounts/create.html"
#     success_url = reverse_lazy("login")

#     def get_context_data(self, **kwargs):
#         context= CreateView.get_context_data(self, **kwargs)
#         form2 = self.form_class2(self.request.GET or None)
#         context.update({'form2':form2})
#         return context

#     def form_valid(self, form):
#         form2 = self.form_class2(self.request.POST or None)

#         if form2.is_valid():
#             with transaction.atomic():
#                 form.save()
#                 form2.save() 
#         else:
#             self.form_invalid(form)


#         return HttpResponseRedirect(self.get_success_url())

#     def get_success_url(self):
#         return reverse_lazy('lending')