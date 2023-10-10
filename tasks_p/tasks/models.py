from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models import OneToOneField, ManyToManyField


class Company(models.Model):
    pass


class Rank(models.Model):
    pass


class Profile(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE, null=True)
    phone_number = models.CharField(max_length=12, null=True)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    rank = models.ForeignKey(Rank, on_delete=models.DO_NOTHING)
    boss = models.ForeignKey("self", on_delete=models.DO_NOTHING)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="img/profile")


class Task(models.Model):
    title = models.TextField('Заголовок', max_length=127)
    description = models.TextField('Описание', max_length=255)
    created = models.DateTimeField('Создана', auto_now=True)
    closed = models.DateTimeField('Закрыта', null=True, editable=False)
    changed = models.DateTimeField('Последнее изменение', auto_now=True, editable=False)
    deadline = models.DateTimeField('Рассмотреть до')
    author = models.ForeignKey('Инициатор', Profile, on_delete=models.DO_NOTHING)
    deciders = ManyToManyField('Рассматривающие', Profile, on_delete=models.DO_NOTHING)
    viewers = ManyToManyField('Наблюдатели', Group, on_delete=models.DO_NOTHING)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Служебка'
        verbose_name_plural = 'Служебки'


class Comment(models.Model):
    text = models.TextField()
    published = models.DateTimeField()
    author = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    task = models.ForeignKey(Task, on_delete=models.DO_NOTHING)

