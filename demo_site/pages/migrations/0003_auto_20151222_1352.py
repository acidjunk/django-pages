# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20151222_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gridobject',
            name='content',
        ),
        migrations.RemoveField(
            model_name='gridobject',
            name='name',
        ),
        migrations.RemoveField(
            model_name='gridobject',
            name='slug',
        ),
        migrations.AlterField(
            model_name='gridobject',
            name='horizontalPosition',
            field=models.IntegerField(default=1, verbose_name=b'HorizontalPosition', choices=[(1, b'one'), (2, b'two'), (3, b'three'), (4, b'four'), (5, b'five'), (6, b'six'), (7, b'seven'), (8, b'eight'), (9, b'nine'), (10, b'ten'), (11, b'eleven'), (12, b'twelve'), (13, b'thirteen'), (14, b'fourteen'), (15, b'fifteen'), (16, b'sixteen')]),
        ),
    ]
