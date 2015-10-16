# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20151016_1131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pagefacebooklink',
            old_name='link',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='pagelink',
            old_name='link',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='pageyoutubelink',
            old_name='link',
            new_name='content',
        ),
    ]
