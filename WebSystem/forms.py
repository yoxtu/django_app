from django import forms

class CalcPaymentForm(forms.Form):
    hourly_wage = forms.IntegerField(label='給料')
    hour = forms.IntegerField(label='時間')
    minute = forms.IntegerField(label='分')
    night_hour = forms.IntegerField(label='深夜時間')
    night_minute = forms.IntegerField(label='深夜分')