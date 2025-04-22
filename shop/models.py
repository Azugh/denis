from django.db import models
from django.contrib import admin
from datetime import datetime
from django.contrib.auth.models import User

class categories(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "категории"
        verbose_name = "категория" 

class shopitems(models.Model):
    name = models.CharField(max_length = 50, verbose_name = "Название")
    image = models.FileField(default = 'temp.jpg', verbose_name = "Путь к картинке")
    description = models.CharField(max_length = 200, verbose_name = "Описание")
    price = models.DecimalField(max_digits = 5, decimal_places = 2, verbose_name = "Цена")
    category = models.ForeignKey(categories, on_delete = models.CASCADE, verbose_name = "Категория")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "товары"
        verbose_name = "товар"

class cartitems(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Покупатель")
    shopitem = models.ForeignKey(shopitems, on_delete = models.CASCADE, verbose_name = "Товар")
    quantity = models.PositiveIntegerField(default = 1, verbose_name = "Количество")

    def __str__(self):
        return f"{self.quantity} x {self.shopitem.name}"

    class Meta:
        verbose_name_plural = "товары корзины"
        verbose_name = "товар корзины"

class statuses(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название статуса")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "cтатусы заказов"
        verbose_name = "статус заказа"

class orders(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Покупатель")
    order_date = models.DateTimeField(default = datetime.now(), verbose_name = "Дата заказа")
    total_price = models.DecimalField(max_digits = 7, decimal_places = 2, default = 0, verbose_name = "Общая стоимость")
    status = models.ForeignKey(statuses, on_delete = models.CASCADE, verbose_name = "Статус заказа")

    def __str__(self):
        return f"Заказ №{self.id} от {self.order_date}"

    class Meta:
        verbose_name_plural = "заказы"
        verbose_name = "заказ"

class orderitems(models.Model):
    order = models.ForeignKey(orders, on_delete = models.CASCADE, verbose_name = "Заказ")
    shopitem = models.ForeignKey(shopitems, on_delete = models.CASCADE, verbose_name = "Товар")
    quantity = models.PositiveIntegerField(verbose_name = "Количество")
    fixed_price = models.DecimalField(max_digits = 5, decimal_places = 2, verbose_name = "Цена на момент заказа")

    def __str__(self):
        return f"{self.quantity} x {self.shopitem.name} в заказе №{self.order.id}"

    class Meta:
        verbose_name_plural = "товары заказа"
        verbose_name = "товар заказа"

admin.site.register(categories)
admin.site.register(shopitems)
admin.site.register(cartitems)
admin.site.register(statuses)
admin.site.register(orders)
admin.site.register(orderitems)