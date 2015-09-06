# -*- coding: utf-8 -*-
from django.db import models


class SiteSettings(models.Model):
    site_name = models.CharField('Название сайта', max_length=200)
    description = models.CharField('Description', max_length=200, blank=True)
    keywords = models.CharField('Keywords', max_length=200, blank=True)

    phone = models.CharField('Телефон', max_length=200, blank=True)
    email = models.CharField('E-mail', max_length=200)

    vk = models.CharField('Вк', max_length=200, blank=True)
    facebook = models.CharField('Facebook', max_length=200, blank=True)

    time_work = models.CharField('Время работы', max_length=200, blank=True)

    about = models.TextField("Обо мне (О центре)", default="")
    education = models.TextField("Образование", default="")
    cooperation = models.TextField("Сотрудничество", default="")

    class Meta:
        verbose_name = 'Настройки'
        verbose_name_plural = 'Настройки'
