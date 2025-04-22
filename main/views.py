from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from news.models import articles

def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request, 'main/index.html',
        {
            'title':'Главная',
            'lastnews':articles.objects.order_by('-data')[0:3],
            'year':datetime.now().year,
        }
    )

def contact(request):
    assert isinstance(request, HttpRequest)
    return render(
        request, 'main/contact.html',
        {
            'title':'Контакты',
            'year':datetime.now().year,
        }
    )
    
def signup(request):
    if request.method == 'POST':
        regform = UserCreationForm(request.POST)
        if regform.is_valid():
            reg_f = regform.save(commit=False)
            reg_f.is_staff = False
            reg_f.is_active = True
            reg_f.is_superuser = False
            reg_f.date_joined = datetime.now()
            reg_f.last_login = datetime.now()
            regform.save()
            return redirect('home')
    else:
        regform = UserCreationForm()
    assert isinstance(request, HttpRequest)
    return render(
        request, 'main/signup.html',
        {
            'regform': regform,
            'title':'Регистрация',
            'year':datetime.now().year,
        }
    )
