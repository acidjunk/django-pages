# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0023_photo_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='column',
            name='created_by',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='column',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now, auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='column',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 3, 16, 3, 35, 802797, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='content',
            name='created_by',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='content',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 3, 16, 3, 57, 142224, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='content',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 3, 16, 3, 59, 646337, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='created_by',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 3, 16, 4, 4, 158439, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 3, 16, 4, 6, 54489, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='form',
            name='created_by',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='form',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 3, 16, 4, 10, 110628, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='form',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 3, 16, 4, 12, 110698, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formelement',
            name='created_by',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formelement',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 3, 16, 4, 17, 486938, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formelement',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 3, 16, 4, 20, 135048, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='created_by',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 3, 16, 4, 26, 127280, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 3, 16, 4, 33, 287536, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='created_by',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 3, 16, 4, 43, 295860, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 3, 16, 4, 46, 320193, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='row',
            name='created_by',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='row',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 3, 16, 5, 40, 585853, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='row',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 3, 16, 5, 42, 265948, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
