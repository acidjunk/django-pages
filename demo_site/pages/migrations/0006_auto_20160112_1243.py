# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smartfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20160112_0952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='column',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='column',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='column',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='column',
            name='row',
        ),
        migrations.RemoveField(
            model_name='row',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='row',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='row',
            name='page',
        ),
        migrations.AlterField(
            model_name='gridcell',
            name='horizontalPosition',
            field=models.IntegerField(default=1, verbose_name='HorizontalPosition', choices=[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'), (6, 'six'), (7, 'seven'), (8, 'eight'), (9, 'nine'), (10, 'ten'), (11, 'eleven'), (12, 'twelve'), (13, 'thirteen'), (14, 'fourteen'), (15, 'fifteen'), (16, 'sixteen')]),
        ),
        migrations.AlterField(
            model_name='gridcell',
            name='horizontalSize',
            field=models.IntegerField(default=1, verbose_name='HorizontalSize', choices=[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'), (6, 'six'), (7, 'seven'), (8, 'eight'), (9, 'nine'), (10, 'ten'), (11, 'eleven'), (12, 'twelve'), (13, 'thirteen'), (14, 'fourteen'), (15, 'fifteen'), (16, 'sixteen')]),
        ),
        migrations.AlterField(
            model_name='gridcell',
            name='verticalPosition',
            field=models.IntegerField(default=0, verbose_name='VerticalPosition'),
        ),
        migrations.AlterField(
            model_name='gridcell',
            name='verticalSize',
            field=models.IntegerField(default=1, verbose_name='VerticalSize'),
        ),
        migrations.AlterField(
            model_name='page',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='page',
            name='ordering',
            field=models.PositiveSmallIntegerField(verbose_name='Ordering'),
        ),
        migrations.AlterField(
            model_name='page',
            name='parent',
            field=models.ForeignKey(to='pages.Page', null=True, verbose_name='Parent', blank=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='sidebar_right',
            field=models.BooleanField(default=True, verbose_name='Sidebar right?'),
        ),
        migrations.AlterField(
            model_name='page',
            name='slogan',
            field=models.CharField(max_length=255, default='', blank=True, verbose_name='Slogan'),
        ),
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(max_length=255, verbose_name='Url', unique=True),
        ),
        migrations.AlterField(
            model_name='pagearticle',
            name='content',
            field=models.TextField(verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='pagearticle',
            name='name',
            field=models.TextField(verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='pagearticle',
            name='slug',
            field=models.SlugField(max_length=255, verbose_name='Url', unique=True),
        ),
        migrations.AlterField(
            model_name='pagefacebooklink',
            name='link',
            field=models.TextField(verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='pagefacebooklink',
            name='name',
            field=models.TextField(verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='pagefacebooklink',
            name='slug',
            field=models.SlugField(max_length=255, verbose_name='Url', unique=True),
        ),
        migrations.AlterField(
            model_name='pagefaq',
            name='answer',
            field=models.TextField(verbose_name='Answer'),
        ),
        migrations.AlterField(
            model_name='pagefaq',
            name='question',
            field=models.TextField(verbose_name='Question'),
        ),
        migrations.AlterField(
            model_name='pagefaq',
            name='slug',
            field=models.SlugField(max_length=255, verbose_name='Url', unique=True),
        ),
        migrations.AlterField(
            model_name='pagefile',
            name='file',
            field=smartfields.fields.FileField(verbose_name='File', upload_to='files/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='pagefile',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='pagefile',
            name='slug',
            field=models.SlugField(max_length=255, verbose_name='Url', unique=True),
        ),
        migrations.AlterField(
            model_name='pageform',
            name='message',
            field=smartfields.fields.TextField(verbose_name='Thank you message'),
        ),
        migrations.AlterField(
            model_name='pageform',
            name='slug',
            field=models.SlugField(max_length=255, verbose_name='Url', unique=True),
        ),
        migrations.AlterField(
            model_name='pageformelement',
            name='form',
            field=models.ForeignKey(to='pages.PageForm', verbose_name='Form'),
        ),
        migrations.AlterField(
            model_name='pageformelement',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Element name'),
        ),
        migrations.AlterField(
            model_name='pageformelement',
            name='required',
            field=models.BooleanField(verbose_name='Required?'),
        ),
        migrations.AlterField(
            model_name='pagelink',
            name='link',
            field=models.TextField(verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='pagelink',
            name='name',
            field=models.TextField(verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='pagelink',
            name='slug',
            field=models.SlugField(max_length=255, verbose_name='Url', unique=True),
        ),
        migrations.AlterField(
            model_name='pagephoto',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='pagephoto',
            name='photo',
            field=smartfields.fields.ImageField(verbose_name='Photo', upload_to='photos/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='pagephoto',
            name='slug',
            field=models.SlugField(max_length=255, verbose_name='Url', unique=True),
        ),
        migrations.AlterField(
            model_name='pageyoutubelink',
            name='link',
            field=models.TextField(verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='pageyoutubelink',
            name='name',
            field=models.TextField(verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='pageyoutubelink',
            name='slug',
            field=models.SlugField(max_length=255, verbose_name='Url', unique=True),
        ),
        migrations.DeleteModel(
            name='Column',
        ),
        migrations.DeleteModel(
            name='Row',
        ),
    ]
