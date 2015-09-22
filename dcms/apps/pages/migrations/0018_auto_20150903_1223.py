# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smartfields.fields
import smartfields.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_page_sidebar_right'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', smartfields.fields.TextField(verbose_name=b'Thank you message')),
            ],
            options={
                'verbose_name': 'Form',
                'verbose_name_plural': 'Forms',
            },
            bases=(smartfields.models.SmartfieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='FormElements',
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
        migrations.AlterModelOptions(
            name='content',
            options={'verbose_name': 'Text', 'verbose_name_plural': 'Text'},
        ),
    ]
