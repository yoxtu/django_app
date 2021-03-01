from django.contrib.auth import forms as auth_forms
from .models import *
from django import forms

class LoginForm(auth_forms.AuthenticationForm):
    '''ログインフォーム'''
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label

class DateInput(forms.DateInput):
    input_type = 'date'

class account_info(forms.ModelForm):
    age = forms.IntegerField(label='年齢',min_value = 1,max_value = 120, required = True)
    choice = [('男','男性'),('女','女性')]
    gender = forms.ChoiceField(label='性別',widget=forms.RadioSelect(),choices=choice, required=True)
    class  Meta:
        model = Profile
        fields =['studentNum','birthday']
        labels = {
            'studentNum': '学生番号',
            'birthday': '誕生日'
        }
        widgets = {
            'birthday': DateInput(),
        }