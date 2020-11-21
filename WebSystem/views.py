from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .processing import *
# Create your views here.

def CalcPayment(request):
    params = {
        'title': '給料計算',
        'form': CalcPaymentForm(),
    }
    if(request.method == 'POST'):
        params['message'] ='支給額(A):'
        params['result'] = CalcPay(request.POST['hourly_wage'],\
            request.POST['hour'],request.POST['minute']) + \
            CalcPay(request.POST['hourly_wage'],request.POST['night_hour'],\
            request.POST['night_minute'],1.25)
        params['form'] = CalcPaymentForm(request.POST)
    return render(request, 'WebSystem/index.html', params)
    #     params['message'] = request.POST['hourly_wage'] + '<br>' +\
    #         request.POST['hour'] + '<br>' +\
    #         request.POST['minute'] + '<br>'+\
    #         request.POST['night_hour'] + '<br>' +\
    #         request.POST['night_minute']
    #     params['form'] = WebSystemForm(request.POST)
    # return render(request, 'WebSystem/index.html',params)

