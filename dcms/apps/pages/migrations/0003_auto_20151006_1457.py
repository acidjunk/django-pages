# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0002_normaltext'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageFacebookLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='date/time created')),
                ('modified_on', models.DateTimeField(auto_now=True, verbose_name='date/time modified')),
                ('slug', models.SlugField(unique=True, max_length=255, verbose_name=b'Url')),
                ('title', models.TextField(verbose_name=b'Title')),
                ('link', models.TextField(verbose_name=b'Link')),
                ('created_by', models.ForeignKey(related_name='pages_pagefacebooklink_created_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='pages_pagefacebooklink_modified_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Content',
                'verbose_name_plural': 'Content',
            },
        ),
        migrations.CreateModel(
            name='PageFAQ',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='date/time created')),
                ('modified_on', models.DateTimeField(auto_now=True, verbose_name='date/time modified')),
                ('slug', models.SlugField(unique=True, max_length=255, verbose_name=b'Url')),
                ('question', models.TextField(verbose_name=b'Question')),
                ('answer', models.TextField(verbose_name=b'Answer')),
                ('created_by', models.ForeignKey(related_name='pages_pagefaq_created_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='pages_pagefaq_modified_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Content',
                'verbose_name_plural': 'Content',
            },
        ),
        migrations.CreateModel(
            name='PageLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='date/time created')),
                ('modified_on', models.DateTimeField(auto_now=True, verbose_name='date/time modified')),
                ('slug', models.SlugField(unique=True, max_length=255, verbose_name=b'Url')),
                ('title', models.TextField(verbose_name=b'Title')),
                ('link', models.TextField(verbose_name=b'Link')),
                ('created_by', models.ForeignKey(related_name='pages_pagelink_created_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='pages_pagelink_modified_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Content',
                'verbose_name_plural': 'Content',
            },
        ),
        migrations.CreateModel(
            name='PageYoutubeLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='date/time created')),
                ('modified_on', models.DateTimeField(auto_now=True, verbose_name='date/time modified')),
                ('slug', models.SlugField(unique=True, max_length=255, verbose_name=b'Url')),
                ('title', models.TextField(verbose_name=b'Title')),
                ('link', models.TextField(verbose_name=b'Link')),
                ('created_by', models.ForeignKey(related_name='pages_pageyoutubelink_created_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='pages_pageyoutubelink_modified_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Content',
                'verbose_name_plural': 'Content',
            },
        ),
        migrations.RemoveField(
            model_name='normaltext',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='normaltext',
            name='modified_by',
        ),
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(default=0, unique=True, max_length=255, verbose_name=b'Url'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pagearticle',
            name='slug',
            field=models.SlugField(default=0, unique=True, max_length=255, verbose_name=b'Url'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pagefile',
            name='slug',
            field=models.SlugField(default=0, unique=True, max_length=255, verbose_name=b'Url'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pageform',
            name='slug',
            field=models.SlugField(default=0, unique=True, max_length=255, verbose_name=b'Url'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pagephoto',
            name='slug',
            field=models.SlugField(default=0, unique=True, max_length=255, verbose_name=b'Url'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='NormalText',
        ),
    ]
