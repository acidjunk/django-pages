# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smartfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_auto_20150902_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=smartfields.fields.ImageField(upload_to=b'photos/%Y/%m/%d', verbose_name=b'Photo'),
        ),
    ]
