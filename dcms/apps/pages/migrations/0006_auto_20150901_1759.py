# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_column'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='width',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
