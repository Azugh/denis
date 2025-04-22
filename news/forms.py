from django import forms
from .models import pictures, comments, Feedback

class PictureForm(forms.ModelForm):
    class Meta:
        model = pictures
        fields = ('title', 'image')
        labels = {'title': 'Заголовок', 'image': 'Путь к картинке'}

class CommentForm(forms.ModelForm):
    class Meta:
        model = comments
        fields = ('text',)
        labels = {'text': 'Текст комментария'}

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'city', 'job', 'gender', 'internet', 'notice', 'email', 'message']
        labels = {
            'name': 'Ваше имя',
            'city': 'Ваш город',
            'job': 'Ваш род деятельности',
            'gender': 'Ваш пол',
            'internet': 'Вы пользуетесь интернетом',
            'notice': 'Получать новости сайта на e-mail?',
            'email': 'Ваш e-mail',
            'message': 'Коротко о себе',
        }
        widgets = {
            'gender': forms.Select(choices=[('1', 'Мужской'), ('2', 'Женский')]),
            'internet': forms.Select(choices=[('1', 'Ежедневно'), ('2', 'Пару часов в день'), ('3', 'Пару часов в неделю'), ('4', 'Пару часов в месяц')]),
        }
        