# -*- coding: utf-8 -*-
from django.db import models
from redactor.fields import RedactorField


class Consultation(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    description = models.CharField("Описание", max_length=200, blank=True)
    keyword = models.CharField("Ключевые слова", max_length=200, blank=True)
    text = RedactorField(verbose_name="Ответ", redactor_options={'upload_to': 'static/uploads'}, blank=True)
    image = models.ImageField(verbose_name="Изображение", upload_to='static/uploads', null=True)
    url = models.CharField("Url", max_length=200, unique=True, default="")
    public = models.BooleanField("Опубликованно", default=False)
    date_time = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = 'Консультация'
        verbose_name_plural = 'Консультации'

    def __unicode__(self):
        return self.title


class ConsultationAsk(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=200)
    profession = models.CharField(verbose_name="Профессия", max_length=200, blank=True)
    age = models.CharField(verbose_name="Возраст", max_length=200, blank=True)
    email = models.EmailField(verbose_name="Email для ответа")
    text = models.TextField(verbose_name="Вопрос")
    date_time = models.DateTimeField(verbose_name="Дата и время", auto_now_add=True)
    viewed = models.BooleanField(verbose_name="Просмотрено", default=False)

    class Meta:
        verbose_name_plural = "Вопросы"
        verbose_name = "Вопрос"

    def __unicode__(self):
        return self.name + ", " + self.profession + ", " + self.age

    def get_date_time(self):
        return str(self.date_time.date()) + " " + str(self.date_time.time().hour) + ":" + str(self.date_time.time().minute)

