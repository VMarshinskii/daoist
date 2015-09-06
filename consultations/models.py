# -*- coding: utf-8 -*-
from django.db import models
from redactor.fields import RedactorField


class Consultation(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    description = models.CharField("Описание", max_length=200, blank=True)
    keyword = models.CharField("Ключевые слова", max_length=200, blank=True)
    question = models.TextField(verbose_name="Вопрос")
    reply = RedactorField(verbose_name="Ответ", redactor_options={'upload_to': 'static/uploads'}, blank=True)
    public = models.BooleanField("Опубликованно", default=False)
    date_time = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = 'Консультация'
        verbose_name_plural = 'Консультации'

    def __unicode__(self):
        return self.title
