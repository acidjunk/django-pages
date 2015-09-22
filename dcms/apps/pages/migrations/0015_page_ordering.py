# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_row_ordering'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='ordering',
            field=models.PositiveSmallIntegerField(default=1, verbose_name=b'Ordering'),
            preserve_default=False,
        ),
    ]
