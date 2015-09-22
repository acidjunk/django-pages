# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_page_ordering'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='slogan',
            field=models.CharField(default='This is my slogan', max_length=255, verbose_name=b'Slogan'),
            preserve_default=False,
        ),
    ]
