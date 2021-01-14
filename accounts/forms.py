from django.contrib.auth import forms as auth_forms
from .models import *
from django import forms

class LoginForm(auth_forms.AuthenticationForm):
    '''ログインフォーム'''
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label

class account_info(forms.ModelForm):
    # std_num = forms.CharField(label='学生番号', required = True)
    age = forms.IntegerField(label='年齢',min_value = 1,max_value = 120, required = True)
    choice = [('男性','男'),('女性','女')]
    gender = forms.ChoiceField(label='性別',widget=forms.RadioSelect(),choices=choice, required=False)
    class  Meta:
        model = Profile
        fields =['std_num']
        labels = {
            'std_num': '学生番号',
        }
        # help_texts = {
        #     'std_num': ('Some useful help text.'),
        #     'age': ('Some useful help text.'),
        # }
        # error_messages = {
        #     'std_num': {
        #         'max_length': ("This writer's name is too long."),
        #     },
        #     'age': {
        #         'max_length': ("This writer's name is too long."),
        #     },
        # }