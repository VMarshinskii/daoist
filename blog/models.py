# -*- coding: utf-8 -*-
from django.db import models
from redactor.fields import RedactorField


class Post(models.Model):
    title = models.CharField("Название", max_length=200)
    description = models.CharField("Описание", max_length=200, blank=True)
    keyword = models.CharField("Ключевые слова", max_length=200, blank=True)
    text = RedactorField(verbose_name="Текст", redactor_options={'upload_to': 'static/uploads'})
    image = models.ImageField(verbose_name="Изображение", upload_to='static/uploads', blank=True)
    url = models.CharField("Url", max_length=200, unique=True)
    public = models.BooleanField("Опубликованно", default=False)
    date = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __unicode__(self):
        return self.title

    def get_link(self):
        return '<a target="_blank" href="/blog/' + self.url + '/">' + self.url + '</a>'
    get_link.allow_tags = True
    get_link.short_description = 'Ссылка'
