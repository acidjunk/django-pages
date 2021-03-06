# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='url',
        ),
        migrations.AddField(
            model_name='page',
            name='summary',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='slogan',
            field=models.CharField(default=b'', max_length=255, verbose_name=b'Slogan', blank=True),
        ),
    ]
