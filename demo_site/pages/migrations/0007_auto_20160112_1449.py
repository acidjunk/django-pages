# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20160112_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gridcell',
            name='page',
            field=models.ForeignKey(related_name='grid_cells', editable=False, to='pages.Page'),
        ),
        migrations.AlterField(
            model_name='page',
            name='parent',
            field=models.ForeignKey(verbose_name='Parent', related_name='Child', null=True, blank=True, to='pages.Page'),
        ),
        migrations.AlterField(
            model_name='pageformelement',
            name='form',
            field=models.ForeignKey(verbose_name='Form', related_name='FormElement', to='pages.PageForm'),
        ),
    ]
