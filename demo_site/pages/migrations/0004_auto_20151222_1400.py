# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0003_auto_20151222_1352'),
    ]

    operations = [
        migrations.CreateModel(
            name='GridCell',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='date/time created')),
                ('modified_on', models.DateTimeField(auto_now=True, verbose_name='date/time modified')),
                ('horizontalSize', models.IntegerField(default=1, verbose_name=b'HorizontalSize', choices=[(1, b'one'), (2, b'two'), (3, b'three'), (4, b'four'), (5, b'five'), (6, b'six'), (7, b'seven'), (8, b'eight'), (9, b'nine'), (10, b'ten'), (11, b'eleven'), (12, b'twelve'), (13, b'thirteen'), (14, b'fourteen'), (15, b'fifteen'), (16, b'sixteen')])),
                ('horizontalPosition', models.IntegerField(default=1, verbose_name=b'HorizontalPosition', choices=[(1, b'one'), (2, b'two'), (3, b'three'), (4, b'four'), (5, b'five'), (6, b'six'), (7, b'seven'), (8, b'eight'), (9, b'nine'), (10, b'ten'), (11, b'eleven'), (12, b'twelve'), (13, b'thirteen'), (14, b'fourteen'), (15, b'fifteen'), (16, b'sixteen')])),
                ('verticalSize', models.IntegerField(default=1, verbose_name=b'VerticalSize')),
                ('verticalPosition', models.IntegerField(default=0, verbose_name=b'VerticalPosition')),
                ('created_by', models.ForeignKey(related_name='pages_gridcell_created_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='pages_gridcell_modified_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('page', models.ForeignKey(related_name='grid_cells', to='pages.Page')),
            ],
            options={
                'verbose_name': 'Grid',
                'verbose_name_plural': 'Grids',
            },
        ),
        migrations.RemoveField(
            model_name='gridobject',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='gridobject',
            name='modified_by',
        ),
        migrations.DeleteModel(
            name='GridObject',
        ),
    ]
