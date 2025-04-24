from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import articles, pictures, comments
from .forms import PictureForm, CommentForm, ReviewForm, ArticleForm
from django.contrib import messages

def redir(request):
    assert isinstance(request, HttpRequest)
    return redirect('news')

def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            messages.success(request, 'Новость успешно добавлена!')
            return redirect('news')
    else:
        form = ArticleForm()
    
    return render(request, 'news/add_article.html', {'form': form})

def news(request):

    return render(
        request,
        'news/index.html',
        {
            'title': 'Новости сайта',
            'newslist': articles.objects.all(),
            'year': datetime.now().year,
        }
    )
def article(request, n):
    assert isinstance(request, HttpRequest)
    return render(
        request, 'news/article.html',
        {
            'title':articles.objects.get(id = n),
            'year':datetime.now().year,
        }
    )
    
def arts(request):
    assert isinstance(request, HttpRequest)
    return render(
        request, 'news/arts.html',
        {
            'title':'Лента',
            'artslist':pictures.objects.all(),
            'year':datetime.now().year,
        }
    )

def feedback(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    data = None
    gender = {'1': 'Мужчина', '2':'Женщина'}
    internet = {'1': 'Ежедневно' , '2': 'Пару часов в день', '3': 'Пару часов в неделю', '4': 'Пару часов в месяц'}

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = dict()
            data['name'] = form.cleaned_data['name']
            data['city'] = form.cleaned_data['city']
            data['job'] = form.cleaned_data['job']
            data['gender'] = gender[ form.cleaned_data['gender'] ]
            data['internet'] = internet[ form.cleaned_data['internet'] ]
            if(form.cleaned_data['notice'] == True):
                data['notice'] = 'Да'
            else:
                data['notice'] = 'Нет'
            data['email'] = form.cleaned_data['email']
            data['message'] = form.cleaned_data['message']
            form = None
    else:
        form = ReviewForm()
    return render(
        request,
        'news/feedback.html',
        {
            'form': form,
            'data': data,
            'year':datetime.now().year},
        )

def feedback_success(request):
    return render(request, 'news/feedback_success.html')

def art(request, n):
    artn = pictures.objects.get(id = n)
    comms = comments.objects.filter(post = n)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            commf = form.save(commit = False)
            commf.author = request.user
            commf.date = datetime.now()
            commf.post = pictures.objects.get(id = n)
            commf.save()
            return redirect('art', n = artn.id)
    else:
        form = CommentForm()
    assert isinstance(request, HttpRequest)
    return render(
        request, 'news/art.html',
        {
            'title':artn,
            'comms':comms,
            'form':form,
            'year':datetime.now().year,
        }
    )

def newart(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            blogf = form.save(commit = False)
            blogf.date = datetime.now()
            blogf.author = request.user
            blogf.save()
            return redirect('arts')
    else:
        form = PictureForm()
    assert isinstance(request, HttpRequest)
    return render(
        request, 'news/newart.html',
        {
            'title':'Добавить арт',
            'form':form,
            'year':datetime.now().year,
        }
    )
    
