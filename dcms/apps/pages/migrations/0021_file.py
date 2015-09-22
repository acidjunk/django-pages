# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smartfields.fields
import smartfields.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0020_auto_20150903_1227'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', smartfields.fields.FileField(upload_to=b'files/%Y/%m/%d', verbose_name=b'File')),
            ],
            options={
                'verbose_name': 'File',
                'verbose_name_plural': 'Files',
            },
            bases=(smartfields.models.SmartfieldsModelMixin, models.Model),
        ),
    ]
