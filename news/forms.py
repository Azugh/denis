from django import forms
from .models import pictures, comments, Feedback, articles

# Форма для создания и редактирования статей
class ArticleForm(forms.ModelForm):
    class Meta:
        # Модель, на основе которой создается форма
        model = articles
        # Поля, которые будут включены в форму
        fields = ['title', 'description', 'text']
        # Виджеты для полей, чтобы задать HTML-атрибуты
        widgets = {
            # Виджет для поля "title" с классом "form-control"
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # Виджет для поля "description" с классом "form-control"
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            # Виджет для поля "text" с классом "form-control" и 5 строками
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

# Форма для создания и редактирования рисунков
class PictureForm(forms.ModelForm):
    class Meta:
        # Модель, на основе которой создается форма
        model = pictures
        # Поля, которые будут включены в форму
        fields = ('title', 'image')
        # Метки для полей формы
        labels = {
            'title': 'Заголовок',  # Метка для поля "title"
            'image': 'Путь к картинке',  # Метка для поля "image"
        }

# Форма для создания и редактирования комментариев
class CommentForm(forms.ModelForm):
    class Meta:
        # Модель, на основе которой создается форма
        model = comments
        # Поля, которые будут включены в форму
        fields = ('text',)
        # Метки для полей формы
        labels = {
            'text': 'Текст комментария',  # Метка для поля "text"
        }

# Форма для создания и редактирования обратной связи
class ReviewForm(forms.ModelForm):
    class Meta:
        # Модель, на основе которой создается форма
        model = Feedback
        # Поля, которые будут включены в форму
        fields = ['name', 'city', 'job', 'gender', 'internet', 'notice', 'email', 'message']
        # Метки для полей формы
        labels = {
            'name': 'Ваше имя',  # Метка для поля "name"
            'city': 'Ваш город',  # Метка для поля "city"
            'job': 'Ваш род деятельности',  # Метка для поля "job"
            'gender': 'Ваш пол',  # Метка для поля "gender"
            'internet': 'Вы пользуетесь интернетом',  # Метка для поля "internet"
            'notice': 'Получать новости сайта на e-mail?',  # Метка для поля "notice"
            'email': 'Ваш e-mail',  # Метка для поля "email"
            'message': 'Коротко о себе',  # Метка для поля "message"
        }
        # Виджеты для полей, чтобы задать выпадающие списки
        widgets = {
            # Виджет для поля "gender" с выбором из 'Мужской' или 'Женский'
            'gender': forms.Select(choices=[('1', 'Мужской'), ('2', 'Женский')]),
            # Виджет для поля "internet" с выбором из нескольких вариантов
            'internet': forms.Select(choices=[('1', 'Ежедневно'), ('2', 'Пару часов в день'), ('3', 'Пару часов в неделю'), ('4', 'Пару часов в месяц')]),
        }
