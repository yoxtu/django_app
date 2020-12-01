from django import forms

class calcPayment(forms.Form):
    hourly_wage = forms.IntegerField(label='時給')
    hour = forms.IntegerField(label='時間')
    minutes = forms.IntegerField(label='分')
    night_hour = forms.IntegerField(label="夜勤時間")
    night_minutes = forms.IntegerField(label="夜分")

