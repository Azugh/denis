from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import articles, pictures, comments
from .forms import PictureForm, CommentForm, ReviewForm

def redir(request):
    assert isinstance(request, HttpRequest)
    return redirect('news')

def news(request):
    assert isinstance(request, HttpRequest)
    return render(
        request, 'news/index.html',
        {
            'title':'Новости сайта',
            'newslist':articles.objects.all(),
            'year':datetime.now().year,
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
            'title':'Арты',
            'artslist':pictures.objects.all(),
            'year':datetime.now().year,
        }
    )

def feedback(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()  # Сохранение данных в базе данных
            return redirect('feedback_success')  # Перенаправление на страницу успеха
    else:
        form = ReviewForm()
    return render(request, 'news/feedback.html', {'form': form})

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
    
