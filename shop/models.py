from django.db import models
from django.contrib import admin
from datetime import datetime
from django.contrib.auth.models import User

# Модель для хранения категорий товаров
class categories(models.Model):
    # Название категории (строка до 100 символов)
    name = models.CharField(max_length=100, verbose_name="Название категории")

    # Метод для возврата строкового представления объекта (название категории)
    def __str__(self):
        return self.name

    class Meta:
        # Настройки для отображения имени модели в админке
        verbose_name_plural = "категории"
        verbose_name = "категория"

# Модель для хранения товаров магазина
class shopitems(models.Model):
    # Название товара (строка до 50 символов)
    name = models.CharField(max_length=50, verbose_name="Название")
    # Путь к изображению товара (по умолчанию 'temp.jpg')
    image = models.FileField(default='temp.jpg', verbose_name="Путь к картинке")
    # Описание товара (строка до 200 символов)
    description = models.CharField(max_length=200, verbose_name="Описание")
    # Цена товара (десятичное число с двумя знаками после запятой)
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Цена")
    # Ссылка на категорию товара (внешний ключ на модель `categories`)
    category = models.ForeignKey(categories, on_delete=models.CASCADE, verbose_name="Категория")

    # Метод для возврата строкового представления объекта (название товара)
    def __str__(self):
        return self.name

    class Meta:
        # Настройки для отображения имени модели в админке
        verbose_name_plural = "товары"
        verbose_name = "товар"

# Модель для хранения товаров в корзине пользователя
class cartitems(models.Model):
    # Покупатель (внешний ключ на модель `User`)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Покупатель")
    # Товар (внешний ключ на модель `shopitems`)
    shopitem = models.ForeignKey(shopitems, on_delete=models.CASCADE, verbose_name="Товар")
    # Количество товара (целое число, по умолчанию 1)
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")

    # Метод для возврата строкового представления объекта (количество x название товара)
    def __str__(self):
        return f"{self.quantity} x {self.shopitem.name}"

    class Meta:
        # Настройки для отображения имени модели в админке
        verbose_name_plural = "товары корзины"
        verbose_name = "товар корзины"

# Модель для хранения статусов заказов
class statuses(models.Model):
    # Название статуса (строка до 50 символов)
    name = models.CharField(max_length=50, verbose_name="Название статуса")

    # Метод для возврата строкового представления объекта (название статуса)
    def __str__(self):
        return self.name

    class Meta:
        # Настройки для отображения имени модели в админке
        verbose_name_plural = "cтатусы заказов"
        verbose_name = "статус заказа"

# Модель для хранения заказов
class orders(models.Model):
    # Покупатель (внешний ключ на модель `User`)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Покупатель")
    # Дата заказа (дата и время, по умолчанию текущая дата и время)
    order_date = models.DateTimeField(default=datetime.now(), verbose_name="Дата заказа")
    # Общая стоимость заказа (десятичное число с двумя знаками после запятой, по умолчанию 0)
    total_price = models.DecimalField(max_digits=7, decimal_places=2, default=0, verbose_name="Общая стоимость")
    # Статус заказа (внешний ключ на модель `statuses`)
    status = models.ForeignKey(statuses, on_delete=models.CASCADE, verbose_name="Статус заказа")

    # Метод для возврата строкового представления объекта (номер заказа и дата заказа)
    def __str__(self):
        return f"Заказ №{self.id} от {self.order_date}"

    class Meta:
        # Настройки для отображения имени модели в админке
        verbose_name_plural = "заказы"
        verbose_name = "заказ"

# Модель для хранения товаров в заказе
class orderitems(models.Model):
    # Заказ (внешний ключ на модель `orders`)
    order = models.ForeignKey(orders, on_delete=models.CASCADE, verbose_name="Заказ")
    # Товар (внешний ключ на модель `shopitems`)
    shopitem = models.ForeignKey(shopitems, on_delete=models.CASCADE, verbose_name="Товар")
    # Количество товара (целое число)
    quantity = models.PositiveIntegerField(verbose_name="Количество")
    # Цена на момент заказа (десятичное число с двумя знаками после запятой)
    fixed_price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Цена на момент заказа")

    # Метод для возврата строкового представления объекта (количество x название товара в заказе)
    def __str__(self):
        return f"{self.quantity} x {self.shopitem.name} в заказе №{self.order.id}"

    class Meta:
        # Настройки для отображения имени модели в админке
        verbose_name_plural = "товары заказа"
        verbose_name = "товар заказа"

admin.site.register(categories)
admin.site.register(shopitems)
admin.site.register(cartitems)
admin.site.register(statuses)
admin.site.register(orders)
admin.site.register(orderitems)