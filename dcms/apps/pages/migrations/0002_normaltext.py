# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NormalText',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='date/time created')),
                ('modified_on', models.DateTimeField(auto_now=True, verbose_name='date/time modified')),
                ('title', models.CharField(max_length=255, verbose_name=b'Title')),
                ('content', models.CharField(max_length=255, verbose_name=b'Content')),
                ('created_by', models.ForeignKey(related_name='pages_normaltext_created_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='pages_normaltext_modified_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Content',
                'verbose_name_plural': 'Content',
            },
        ),
    ]
