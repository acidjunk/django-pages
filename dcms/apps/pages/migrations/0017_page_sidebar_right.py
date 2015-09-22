# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_page_slogan'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='sidebar_right',
            field=models.BooleanField(default=True, verbose_name=b'Sidebar right?'),
        ),
    ]
