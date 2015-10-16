# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20151006_1457'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pagearticle',
            options={'verbose_name': 'Content', 'verbose_name_plural': 'Content'},
        ),
        migrations.AddField(
            model_name='pagearticle',
            name='title',
            field=models.TextField(default=datetime.datetime(2015, 10, 16, 11, 31, 56, 630311, tzinfo=utc), verbose_name=b'Title'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pagearticle',
            name='content',
            field=models.TextField(verbose_name=b'Content'),
        ),
    ]
