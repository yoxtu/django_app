from django.shortcuts import render
from .forms import *
from .sum import *

# Create your views here.
def calcPaymentEX(request):
    params = {
        'title': 'バイト給与計算',
        'form': calcPayment()
    }
    if request.method == 'POST':
        params['result'] = sum(request.POST['hourly_wage'],request.POST['hour'],request.POST['minutes'],1) + sum2(request.POST['hourly_wage'],request.POST['hour'],request.POST['minutes'],1.25)
        params['form'] = calcPaymentEX(request.POST)
    return render(request, 'WebSystem/index.html', params)

