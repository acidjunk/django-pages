# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smartfields.fields
import smartfields.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='date/time created')),
                ('modified_on', models.DateTimeField(auto_now=True, verbose_name='date/time modified')),
                ('width', models.PositiveSmallIntegerField()),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('ordering', models.PositiveSmallIntegerField(verbose_name=b'Ordering')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', null=True)),
                ('created_by', models.ForeignKey(related_name='pages_column_created_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='pages_column_modified_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Column',
                'verbose_name_plural': 'Columns',
            },
        ),
        migrations.CreateModel(
            name='GridObject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='date/time created')),
                ('modified_on', models.DateTimeField(auto_now=True, verbose_name='date/time modified')),
                ('slug', models.SlugField(unique=True, max_length=255, verbose_name=b'Url')),
                ('horizontalSize', models.CharField(default=1, max_length=2, verbose_name=b'HorizontalSize', choices=[(1, b'one'), (2, b'two'), (3, b'three'), (4, b'four'), (5, b'five'), (6, b'six'), (7, b'seven'), (8, b'eight'), (9, b'nine'), (10, b'ten'), (11, b'eleven'), (12, b'twelve'), (13, b'thirteen'), (14, b'fourteen'), (15, b'fifteen'), (16, b'sixteen')])),
                ('horizontalPosition', models.IntegerField(default=0, verbose_name=b'HorizontalPosition')),
                ('verticalSize', models.CharField(default=1, max_length=2, verbose_name=b'VerticalSize')),
                ('verticalPosition', models.IntegerField(default=0, verbose_name=b'VerticalPosition')),
                ('Title', models.TextField(verbose_name=b'Title')),
                ('Content', models.TextField(verbose_name=b'Content')),
                ('created_by', models.ForeignKey(related_name='pages_gridobject_created_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='pages_gridobject_modified_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Content',
                'verbose_name_plural': 'Content',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='date/time created')),
                ('modified_on', models.DateTimeField(auto_now=True, verbose_name='date/time modified')),
                ('slug', models.SlugField(unique=True, max_length=255, verbose_name=b'Url')),
                ('name', models.CharField(max_length=255, verbose_name=b'Name')),
                ('slogan', models.CharField(max_length=255, verbose_name=b'Slogan')),
                ('url', models.SlugField(unique=True, max_length=255, verbose_name=b'Url')),
                ('ordering', models.PositiveSmallIntegerField(verbose_name=b'Ordering')),
                ('sidebar_right', models.BooleanField(default=True, verbose_name=b'Sidebar right?')),
                ('created_by', models.ForeignKey(related_name='pages_page_created_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='pages_page_modified_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('parent', models.ForeignKey(verbose_name=b'Parent', blank=True, to='pages.Page', null=True)),
            ],
            options={
                'verbose_name': 'Page',
                'verbose_name_plural': 'Pages',
            },
        ),
        migrations.CreateModel(
            name='PageArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='date/time created')),
                ('modified_on', models.DateTimeField(auto_now=True, verbose_name='date/time modified')),
                ('slug', models.SlugField(unique=True, max_length=255, verbose_name=b'Url')),
                ('title', models.TextField(verbose_name=b'Title')),
                ('content', models.TextField(verbose_name=b'Content')),
                ('created_by', models.ForeignKey(related_name='pages_pagearticle_created_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='pages_pagearticle_modified_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Content',
                'verbose_name_plural': 'Content',
            },
        ),
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
            name='PageFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='date/time created')),
                ('modified_on', models.DateTimeField(auto_now=True, verbose_name='date/time modified')),
                ('slug', models.SlugField(unique=True, max_length=255, verbose_name=b'Url')),
                ('name', models.CharField(max_length=255, verbose_name=b'Name')),
                ('file', smartfields.fields.FileField(upload_to=b'files/%Y/%m/%d', verbose_name=b'File')),
                ('created_by', models.ForeignKey(related_name='pages_pagefile_created_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='pages_pagefile_modified_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'File',
                'verbose_name_plural': 'Files',
            },
            bases=(smartfields.models.SmartfieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PageForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='date/time created')),
                ('modified_on', models.DateTimeField(auto_now=True, verbose_name='date/time modified')),
                ('slug', models.SlugField(unique=True, max_length=255, verbose_name=b'Url')),
                ('message', smartfields.fields.TextField(verbose_name=b'Thank you message')),
                ('created_by', models.ForeignKey(related_name='pages_pageform_created_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='pages_pageform_modified_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Form',
                'verbose_name_plural': 'Forms',
            },
            bases=(smartfields.models.SmartfieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PageFormElement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='date/time created')),
                ('modified_on', models.DateTimeField(auto_now=True, verbose_name='date/time modified')),
                ('name', models.CharField(max_length=255, verbose_name=b'Element name')),
                ('required', models.BooleanField(verbose_name=b'Required?')),
                ('created_by', models.ForeignKey(related_name='pages_pageformelement_created_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('form', models.ForeignKey(verbose_name=b'Form', to='pages.PageForm')),
                ('modified_by', models.ForeignKey(related_name='pages_pageformelement_modified_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Form element',
                'verbose_name_plural': 'Form elements',
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
            name='PagePhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='date/time created')),
                ('modified_on', models.DateTimeField(auto_now=True, verbose_name='date/time modified')),
                ('slug', models.SlugField(unique=True, max_length=255, verbose_name=b'Url')),
                ('name', models.CharField(max_length=255, verbose_name=b'Name')),
                ('photo', smartfields.fields.ImageField(upload_to=b'photos/%Y/%m/%d', verbose_name=b'Photo')),
                ('created_by', models.ForeignKey(related_name='pages_pagephoto_created_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='pages_pagephoto_modified_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Photo',
                'verbose_name_plural': "Photo's",
            },
            bases=(smartfields.models.SmartfieldsModelMixin, models.Model),
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
        migrations.CreateModel(
            name='Row',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='date/time created')),
                ('modified_on', models.DateTimeField(auto_now=True, verbose_name='date/time modified')),
                ('ordering', models.PositiveSmallIntegerField(verbose_name=b'Ordering')),
                ('created_by', models.ForeignKey(related_name='pages_row_created_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='pages_row_modified_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('page', models.ForeignKey(verbose_name=b'Page', to='pages.Page')),
            ],
            options={
                'verbose_name': 'Row',
                'verbose_name_plural': 'Rows',
            },
        ),
        migrations.AddField(
            model_name='column',
            name='row',
            field=models.ForeignKey(verbose_name=b'Row', to='pages.Row'),
        ),
    ]
