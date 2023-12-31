# Generated by Django 4.2.5 on 2023-09-26 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=127, verbose_name='Заголовок')),
                ('description', models.TextField(max_length=255, verbose_name='Описание')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Создана')),
                ('closed', models.DateTimeField(blank=True, verbose_name='Закрыта')),
                ('changed', models.DateTimeField(blank=True, verbose_name='Последнее изменение')),
                ('deadline', models.DateTimeField(default=models.DateTimeField(auto_now=True, verbose_name='Создана'), verbose_name='Рассмотреть до')),
            ],
        ),
    ]
