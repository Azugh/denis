from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
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


def registration(request):
    """Renders the registration page."""
    assert isinstance(request, HttpRequest)

    if request.method == "POST":
        regform = UserCreationForm(request.POST)
        if regform.is_valid():
            user = regform.save(commit=False)
            user.is_staff = False
            user.is_active = True
            user.is_superuser = False
            user.date_joined = datetime.now()
            user.save()
            
            # Автоматический вход после регистрации
            login(request, user)
            return redirect('home')
    else:
        regform = UserCreationForm()

    # Отображаем форму с ошибками, если они есть
    return render(request, 'main/signup.html', {
        'regform': regform,
        'title': 'Регистрация',
        'year': datetime.now().year,
    })