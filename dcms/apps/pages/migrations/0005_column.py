# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_row'),
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('width', models.PositiveSmallIntegerField(max_length=2)),
                ('row', models.ForeignKey(verbose_name=b'Row', to='pages.Row')),
            ],
            options={
                'verbose_name': 'Column',
                'verbose_name_plural': 'Columns',
            },
        ),
    ]
