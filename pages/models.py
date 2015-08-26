# -*- coding: utf-8 -*-
from django.db import models
from redactor.fields import RedactorField


class Page(models.Model):
    title = models.CharField("Название", max_length=200)
    description = models.CharField("Описание", max_length=200, blank=True)
    keyword = models.CharField("Ключевые слова", max_length=200, blank=True)
    text = RedactorField(verbose_name="Текст", redactor_options={'upload_to': 'static/uploads'})
    url = models.CharField("Url", max_length=200, unique=True)
    public = models.BooleanField("Опубликованно", default=False)
    send = models.BooleanField(verbose_name="Разослать подписчикам", default=True)
    date = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

    def __unicode__(self):
        return self.title
