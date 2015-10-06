# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0024_auto_20150903_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='column',
            name='modified_by',
            field=models.ForeignKey(related_name='pages_column_modified_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='modified_by',
            field=models.ForeignKey(related_name='pages_content_modified_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='file',
            name='modified_by',
            field=models.ForeignKey(related_name='pages_file_modified_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='form',
            name='modified_by',
            field=models.ForeignKey(related_name='pages_form_modified_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='modified_by',
            field=models.ForeignKey(related_name='pages_formelement_modified_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='modified_by',
            field=models.ForeignKey(related_name='pages_page_modified_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='modified_by',
            field=models.ForeignKey(related_name='pages_photo_modified_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='row',
            name='modified_by',
            field=models.ForeignKey(related_name='pages_row_modified_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='column',
            name='created_by',
            field=models.ForeignKey(related_name='pages_column_created_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='column',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date/time created'),
        ),
        migrations.AlterField(
            model_name='column',
            name='modified_on',
            field=models.DateTimeField(auto_now=True, verbose_name='date/time modified'),
        ),
        migrations.AlterField(
            model_name='content',
            name='created_by',
            field=models.ForeignKey(related_name='pages_content_created_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date/time created'),
        ),
        migrations.AlterField(
            model_name='content',
            name='modified_on',
            field=models.DateTimeField(auto_now=True, verbose_name='date/time modified'),
        ),
        migrations.AlterField(
            model_name='file',
            name='created_by',
            field=models.ForeignKey(related_name='pages_file_created_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date/time created'),
        ),
        migrations.AlterField(
            model_name='file',
            name='modified_on',
            field=models.DateTimeField(auto_now=True, verbose_name='date/time modified'),
        ),
        migrations.AlterField(
            model_name='form',
            name='created_by',
            field=models.ForeignKey(related_name='pages_form_created_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date/time created'),
        ),
        migrations.AlterField(
            model_name='form',
            name='modified_on',
            field=models.DateTimeField(auto_now=True, verbose_name='date/time modified'),
        ),
        migrations.AlterField(
            model_name='formelement',
            name='created_by',
            field=models.ForeignKey(related_name='pages_formelement_created_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='formelement',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date/time created'),
        ),
        migrations.AlterField(
            model_name='formelement',
            name='modified_on',
            field=models.DateTimeField(auto_now=True, verbose_name='date/time modified'),
        ),
        migrations.AlterField(
            model_name='page',
            name='created_by',
            field=models.ForeignKey(related_name='pages_page_created_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date/time created'),
        ),
        migrations.AlterField(
            model_name='page',
            name='modified_on',
            field=models.DateTimeField(auto_now=True, verbose_name='date/time modified'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='created_by',
            field=models.ForeignKey(related_name='pages_photo_created_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date/time created'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='modified_on',
            field=models.DateTimeField(auto_now=True, verbose_name='date/time modified'),
        ),
        migrations.AlterField(
            model_name='row',
            name='created_by',
            field=models.ForeignKey(related_name='pages_row_created_by', default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='row',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date/time created'),
        ),
        migrations.AlterField(
            model_name='row',
            name='modified_on',
            field=models.DateTimeField(auto_now=True, verbose_name='date/time modified'),
        ),
    ]
