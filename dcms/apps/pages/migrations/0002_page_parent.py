# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='parent',
            field=models.ForeignKey(verbose_name=b'Parent', blank=True, to='pages.Page', null=True),
        ),
    ]
