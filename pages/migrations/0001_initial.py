# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('description', models.CharField(max_length=200, verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True)),
                ('keyword', models.CharField(max_length=200, verbose_name=b'\xd0\x9a\xd0\xbb\xd1\x8e\xd1\x87\xd0\xb5\xd0\xb2\xd1\x8b\xd0\xb5 \xd1\x81\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xb0', blank=True)),
                ('text', redactor.fields.RedactorField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82')),
                ('url', models.CharField(unique=True, max_length=200, verbose_name=b'Url')),
                ('public', models.BooleanField(default=False, verbose_name=b'\xd0\x9e\xd0\xbf\xd1\x83\xd0\xb1\xd0\xbb\xd0\xb8\xd0\xba\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xbd\xd0\xbe')),
                ('send', models.BooleanField(default=True, verbose_name=b'\xd0\xa0\xd0\xb0\xd0\xb7\xd0\xbe\xd1\x81\xd0\xbb\xd0\xb0\xd1\x82\xd1\x8c \xd0\xbf\xd0\xbe\xd0\xb4\xd0\xbf\xd0\xb8\xd1\x81\xd1\x87\xd0\xb8\xd0\xba\xd0\xb0\xd0\xbc')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f')),
            ],
            options={
                'verbose_name': '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430',
                'verbose_name_plural': '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u044b',
            },
        ),
    ]
