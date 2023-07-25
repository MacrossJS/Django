from datetime import datetime

from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=50, default='')
    anons = models.CharField('Анонс', max_length=50, default='')
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации', default=datetime.now)
    date_edited = models.DateTimeField('Отредактировано', null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
