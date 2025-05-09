# Generated by Django 5.0.6 on 2024-12-15 19:30

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='shopitems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('image', models.FileField(default='temp.jpg', upload_to='', verbose_name='Путь к картинке')),
                ('description', models.CharField(max_length=200, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Цена')),
                ('count', models.PositiveIntegerField(verbose_name='Количество')),
                ('onePerUser', models.BooleanField(default=False, verbose_name='Одноразовый')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
            },
        ),
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(default=datetime.datetime(2024, 12, 15, 22, 30, 15, 348174), verbose_name='Дата заказа')),
                ('status', models.CharField(max_length=50, verbose_name='Статус')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Покупатель')),
                ('items', models.ManyToManyField(to='shop.shopitems', verbose_name='Товары')),
            ],
            options={
                'verbose_name': 'заказ',
                'verbose_name_plural': 'заказы',
                'ordering': ['-data'],
            },
        ),
    ]
