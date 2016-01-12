# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('pages', '0004_auto_20151222_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='gridcell',
            name='content_type',
            field=models.ForeignKey(related_name='content_type_set_for_gridcell', default=1, verbose_name='content type', to='contenttypes.ContentType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gridcell',
            name='object_pk',
            field=models.TextField(default=1, verbose_name='object ID'),
            preserve_default=False,
        ),
    ]
