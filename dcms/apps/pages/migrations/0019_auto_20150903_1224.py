# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0018_auto_20150903_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormElement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Element name')),
                ('required', models.BooleanField(verbose_name=b'Required?')),
                ('form', models.ForeignKey(verbose_name=b'Form', to='pages.Form')),
            ],
            options={
                'verbose_name': 'Form element',
                'verbose_name_plural': 'Form elements',
            },
        ),
        migrations.RemoveField(
            model_name='formelements',
            name='form',
        ),
        migrations.DeleteModel(
            name='FormElements',
        ),
    ]
