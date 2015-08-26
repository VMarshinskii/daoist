# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default='2015.08.18', verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='send',
            field=models.BooleanField(default=True, verbose_name=b'\xd0\xa0\xd0\xb0\xd0\xb7\xd0\xbe\xd1\x81\xd0\xbb\xd0\xb0\xd1\x82\xd1\x8c \xd0\xbf\xd0\xbe\xd0\xb4\xd0\xbf\xd0\xb8\xd1\x81\xd1\x87\xd0\xb8\xd0\xba\xd0\xb0\xd0\xbc'),
        ),
    ]
