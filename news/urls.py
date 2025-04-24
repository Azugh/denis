from django.urls import path
from . import views

urlpatterns = [
    path('', views.redir, name='redir'),
    path('site/', views.news, name='news'),
    path('site/add', views.add_article, name='add_article'),
    path('site/<int:n>', views.article, name='article'),
    path('arts/', views.arts, name='arts'),
    path('arts/<int:n>', views.art, name='art'),
    path('arts/new', views.newart, name='newart'),

    path('feedback/', views.feedback, name='feedback'),
    path('feedback_success/', views.feedback_success, name='feedback_success'),

    
    
]