# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_page_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='url',
            field=models.SlugField(default='url', max_length=255, verbose_name=b'Url'),
            preserve_default=False,
        ),
    ]
