# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20150901_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='url',
            field=models.SlugField(unique=True, max_length=255, verbose_name=b'Url'),
        ),
    ]
