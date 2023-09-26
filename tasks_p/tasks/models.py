from django.db import models


class Task(models.Model):
    title = models.TextField('Заголовок', max_length=127)
    description = models.TextField('Описание', max_length=255)
    created = models.DateTimeField('Создана', auto_now=True)
    closed = models.DateTimeField('Закрыта', null=True, editable=False)
    changed = models.DateTimeField('Последнее изменение', auto_now=True, editable=False)
    deadline = models.DateTimeField('Рассмотреть до') #Добавить +неделю

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Служебка'
        verbose_name_plural = 'Служебки'
