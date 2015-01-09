from django.shortcuts import render
from django.http import HttpResponseRedirect

def home(request):
    money_value = ""
    if 'money_value' in request.GET:
        moneyvalue = request.GET['money_value']

    return render(request, "home.html")
