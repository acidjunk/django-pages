# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20150902_0827'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(upload_to=b'', verbose_name=b'Photo')),
            ],
            options={
                'verbose_name': 'Photo item',
                'verbose_name_plural': 'Photo items',
            },
        ),
        migrations.AlterModelOptions(
            name='content',
            options={'verbose_name': 'Text item', 'verbose_name_plural': 'Text items'},
        ),
    ]
