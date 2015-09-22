from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from smartfields import fields
from django.contrib.auth.models import User
from django.utils import timezone


class Page(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    slogan = models.CharField(max_length=255, verbose_name='Slogan')
    url = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    parent = models.ForeignKey('Page', blank=True, null=True, verbose_name='Parent')
    ordering = models.PositiveSmallIntegerField(verbose_name='Ordering')
    sidebar_right = models.BooleanField(default=True, verbose_name='Sidebar right?')

    created_by = models.ForeignKey(User, editable=False)
    created_on = models.DateTimeField(auto_now_add=timezone.now)
    modified_on = models.DateTimeField(auto_now=timezone.now)

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'

    def __str__(self):
        return self.name


class Row(models.Model):
    page = models.ForeignKey('Page', null=False, blank=False, verbose_name='Page')
    ordering = models.PositiveSmallIntegerField(verbose_name='Ordering')

    created_by = models.ForeignKey(User, editable=False)
    created_on = models.DateTimeField(auto_now_add=timezone.now)
    modified_on = models.DateTimeField(auto_now=timezone.now)

    class Meta:
        verbose_name = 'Row'
        verbose_name_plural = 'Rows'

    def __str__(self):
        return self.page.name + ' - ' + str(self.pk)


class Column(models.Model):
    row = models.ForeignKey(Row, verbose_name='Row')
    width = models.PositiveSmallIntegerField()
    content_type = models.ForeignKey(ContentType, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    ordering = models.PositiveSmallIntegerField(verbose_name='Ordering')

    created_by = models.ForeignKey(User, editable=False)
    created_on = models.DateTimeField(auto_now_add=timezone.now)
    modified_on = models.DateTimeField(auto_now=timezone.now)

    class Meta:
        verbose_name = 'Column'
        verbose_name_plural = 'Columns'

    def __str__(self):
        return str(self.row.pk) + ' - ' + str(self.pk) + ' - ' + str(self.width)


class Content(models.Model):
    content = models.TextField()

    created_by = models.ForeignKey(User, editable=False)
    created_on = models.DateTimeField(auto_now_add=timezone.now)
    modified_on = models.DateTimeField(auto_now=timezone.now)

    class Meta:
        verbose_name = 'Text'
        verbose_name_plural = 'Texts'

    def content_type(self):
        return 'content'

    def __str__(self):
        return str(self.pk)


class File(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    file = fields.FileField(upload_to='files/%Y/%m/%d', verbose_name='File')

    created_by = models.ForeignKey(User, editable=False)
    created_on = models.DateTimeField(auto_now_add=timezone.now)
    modified_on = models.DateTimeField(auto_now=timezone.now)

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'

    def content_type(self):
        return 'file'

    def __str__(self):
        return self.name


class Photo(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    photo = fields.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Photo')

    created_by = models.ForeignKey(User, editable=False)
    created_on = models.DateTimeField(auto_now_add=timezone.now)
    modified_on = models.DateTimeField(auto_now=timezone.now)

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photo\'s'

    def content_type(self):
        return 'photo'

    def __str__(self):
        return self.name


class Form(models.Model):
    message = fields.TextField(verbose_name='Thank you message')

    created_by = models.ForeignKey(User, editable=False)
    created_on = models.DateTimeField(auto_now_add=timezone.now)
    modified_on = models.DateTimeField(auto_now=timezone.now)

    class Meta:
        verbose_name = 'Form'
        verbose_name_plural = 'Forms'

    def content_type(self):
        return 'form'

    def __str__(self):
        return str(self.pk)


class FormElement(models.Model):
    form = models.ForeignKey(Form, verbose_name='Form')
    name = models.CharField(max_length=255, verbose_name='Element name')
    required = models.BooleanField(verbose_name='Required?')

    created_by = models.ForeignKey(User, editable=False)
    created_on = models.DateTimeField(auto_now_add=timezone.now)
    modified_on = models.DateTimeField(auto_now=timezone.now)

    class Meta:
        verbose_name = 'Form element'
        verbose_name_plural = 'Form elements'

    def __str__(self):
        return self.name
