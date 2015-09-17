# -*- coding: utf-8 -*-
from django.db import models


class PhoneOrder(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=200, default="")
    phone = models.CharField(verbose_name="Телефон", max_length=200, default="")
    date_time = models.DateTimeField(verbose_name="Дата и время", auto_now_add=True)
    viewed = models.BooleanField(verbose_name="Просмотрено", default=False)

    class Meta:
        verbose_name_plural = "Обратные звонки"
        verbose_name = "Обратный звонок"

    def __unicode__(self):
        return self.name + " : " + self.phone

    def get_date_time(self):
        return str(self.date_time.date()) + " " + str(self.date_time.time().hour) + ":" + str(self.date_time.time().minute)
    get_date_time.verbose_name = "Дата"


class Subscriber(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=200)
    email = models.EmailField(verbose_name="E-mail", max_length=200, unique=True)
    date_time = models.DateTimeField(verbose_name="Дата и время", auto_now_add=True)

    class Meta:
        verbose_name_plural = "Подписчики"
        verbose_name = "Подписчик"

    def __unicode__(self):
        return self.name + " : " + self.email

    def get_date_time(self):
        return str(self.date_time.date()) + " " + str(self.date_time.time().hour) + ":" + str(self.date_time.time().minute)
    get_date_time.verbose_name = "Дата"


class Reviews(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=200)
    profession = models.CharField(verbose_name="Профессия", max_length=200, blank=True)
    age = models.CharField(verbose_name="Возраст", max_length=200, blank=True)
    text = models.TextField(verbose_name="Отзыв")
    date_time = models.DateTimeField(verbose_name="Дата и время", auto_now_add=True)
    public = models.BooleanField(verbose_name="Опубликован", default=False)

    class Meta:
        verbose_name_plural = "Отзывы"
        verbose_name = "Отзыв"

    def __unicode__(self):
        return self.name + ", " + self.profession + ", " + self.age

    def get_date_time(self):
        return str(self.date_time.date()) + " " + str(self.date_time.time().hour) + ":" + str(self.date_time.time().minute)
