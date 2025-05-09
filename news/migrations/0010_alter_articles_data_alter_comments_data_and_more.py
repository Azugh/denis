# Generated by Django 5.0.6 on 2024-12-17 09:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_alter_articles_data_alter_comments_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 17, 12, 8, 33, 327185), verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 17, 12, 8, 33, 330246), verbose_name='Дата комментария'),
        ),
        migrations.AlterField(
            model_name='pictures',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 17, 12, 8, 33, 330246), verbose_name='Дата публикации'),
        ),
    ]
