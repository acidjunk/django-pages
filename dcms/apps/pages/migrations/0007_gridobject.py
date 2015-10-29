# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20151016_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='GridObject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('horizontalSize', models.IntegerField(verbose_name=b'HorizontalPosition')),
                ('horizontalPosition', models.IntegerField(verbose_name=b'HorizontalPosition')),
                ('verticalSize', models.IntegerField(verbose_name=b'VerticalPosition')),
                ('verticalPosition', models.IntegerField(verbose_name=b'VerticalPosition')),
                ('Title', models.TextField(verbose_name=b'Title')),
                ('Content', models.TextField(verbose_name=b'Content')),
            ],
            options={
                'verbose_name': 'Content',
                'verbose_name_plural': 'Content',
            },
        ),
    ]
