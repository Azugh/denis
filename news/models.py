from django.db import models
from django.contrib import admin
from datetime import datetime
from django.contrib.auth.models import User

# Модель для хранения статей
class articles(models.Model):
    # Заголовок статьи (строка до 50 символов)
    title = models.CharField('Заголовок', max_length=50)
    # Описание статьи (строка до 200 символов)
    description = models.CharField('Описание', max_length=200)
    # Текст статьи (длинный текст)
    text = models.TextField('Текст')
    # Дата публикации (дата и время, по умолчанию текущая дата и время)
    data = models.DateTimeField('Дата публикации', default=datetime.now())
    # Автор статьи (внешний ключ на модель `User`, может быть пустым)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Автор')

    # Метод для возврата строкового представления объекта (заголовок статьи)
    def __str__(self):
        return self.title

    class Meta:
        # Сортировка по дате публикации в обратном порядке (новые статьи первыми)
        ordering = ["-data"]
        # Настройки для отображения имени модели в админке
        verbose_name_plural = 'новости'
        verbose_name = 'новость'

# Модель для хранения рисунков
class pictures(models.Model):
    # Заголовок рисунка (строка до 50 символов)
    title = models.CharField('Заголовок', max_length=50)
    # Путь к изображению (по умолчанию 'temp.jpg')
    image = models.FileField(default='temp.jpg', verbose_name='Путь к картинке')
    # Дата публикации (дата и время, по умолчанию текущая дата и время)
    data = models.DateTimeField('Дата публикации', default=datetime.now())
    # Автор рисунка (внешний ключ на модель `User`)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    # Метод для возврата строкового представления объекта (заголовок рисунка)
    def __str__(self):
        return self.title

    class Meta:
        # Сортировка по дате публикации в обратном порядке (новые рисунки первыми)
        ordering = ["-data"]
        # Настройки для отображения имени модели в админке
        verbose_name_plural = 'рисунки'
        verbose_name = 'рисунок'

# Модель для хранения комментариев к рисункам
class comments(models.Model):
    # Текст комментария (длинный текст)
    text = models.TextField('Текст комментария')
    # Дата комментария (дата и время, по умолчанию текущая дата и время)
    data = models.DateTimeField('Дата комментария', default=datetime.now())
    # Автор комментария (внешний ключ на модель `User`)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    # Запись, к которой относится комментарий (внешний ключ на модель `pictures`)
    post = models.ForeignKey(pictures, on_delete=models.CASCADE, verbose_name='Запись')

    # Метод для возврата строкового представления объекта (запись // автор (ID))
    def __str__(self):
        return '%s // %s (%d)' % (self.post, self.author, self.id)

    class Meta:
        # Сортировка по дате комментария в обратном порядке (новые комментарии первыми)
        ordering = ["-data"]
        # Настройки для отображения имени модели в админке
        verbose_name_plural = 'комментарии'
        verbose_name = 'комментарий'

# Модель для хранения обратной связи
class Feedback(models.Model):
    # Имя (строка до 100 символов)
    name = models.CharField(max_length=100, verbose_name="Имя")
    # Город (строка до 100 символов)
    city = models.CharField(max_length=100, verbose_name="Город")
    # Род деятельности (строка до 100 символов)
    job = models.CharField(max_length=100, verbose_name="Род деятельности")
    # Пол (выбор из 'Мужчина' или 'Женщина')
    gender = models.CharField(max_length=10, choices=[('1', 'Мужчина'), ('2', 'Женщина')], verbose_name="Пол")
    # Использование интернета (выбор из нескольких вариантов)
    internet = models.CharField(max_length=20, choices=[('1', 'Ежедневно'), ('2', 'Пару часов в день'), ('3', 'Пару часов в неделю'), ('4', 'Пару часов в месяц')], verbose_name="Использование интернета")
    # Получать новости на e-mail (булево значение, по умолчанию False)
    notice = models.BooleanField(default=False, verbose_name="Получать новости на e-mail")
    # E-mail (строка)
    email = models.EmailField(verbose_name="E-mail")
    # Сообщение (длинный текст)
    message = models.TextField(verbose_name="Сообщение")

    # Метод для возврата строкового представления объекта (имя отправителя)
    def __str__(self):
        return f"Feedback from {self.name}"

    class Meta:
        # Настройки для отображения имени модели в админке
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"
    
admin.site.register(articles)
admin.site.register(pictures)
admin.site.register(comments)
admin.site.register(Feedback)