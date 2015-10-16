# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20151016_1141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pagefacebooklink',
            old_name='content',
            new_name='link',
        ),
        migrations.RenameField(
            model_name='pagelink',
            old_name='content',
            new_name='link',
        ),
        migrations.RenameField(
            model_name='pageyoutubelink',
            old_name='content',
            new_name='link',
        ),
    ]
