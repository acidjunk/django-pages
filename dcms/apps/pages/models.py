from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from smartfields import fields
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

class TimestampAble(models.Model):
    created_on = models.DateTimeField(_("date/time created"), editable=False, auto_now_add=True)
    modified_on = models.DateTimeField(_("date/time modified"), editable=False, auto_now=True)

    # These fields will be populated automatically through dcim.apps.middleware.UserAuditMiddleware
    # We will accept Null to make sure we can also populate the fields through shell, tests or anonymous users
    created_by = models.ForeignKey(User, editable=False, related_name='%(app_label)s_%(class)s_created_by', null=True,
                                   default=None)
    modified_by = models.ForeignKey(User, editable=False, related_name='%(app_label)s_%(class)s_modified_by', null=True,
                                    default=None)


    class Meta:
        abstract = True


class Page(TimestampAble):
    name = models.CharField(max_length=255, verbose_name='Name')
    slogan = models.CharField(max_length=255, verbose_name='Slogan')
    url = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    parent = models.ForeignKey('Page', blank=True, null=True, verbose_name='Parent')
    ordering = models.PositiveSmallIntegerField(verbose_name='Ordering')
    sidebar_right = models.BooleanField(default=True, verbose_name='Sidebar right?')

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'

    def __str__(self):
        return self.name


# Todo: remove obsolete class in favor of Grid?
class Row(TimestampAble):
    page = models.ForeignKey('Page', null=False, blank=False, verbose_name='Page')
    ordering = models.PositiveSmallIntegerField(verbose_name='Ordering')

    class Meta:
        verbose_name = 'Row'
        verbose_name_plural = 'Rows'

    def __str__(self):
        return self.page.name + ' - ' + str(self.pk)


# Todo: remove obsolete class in favor of Grid?
class Column(TimestampAble):
    row = models.ForeignKey(Row, verbose_name='Row')
    width = models.PositiveSmallIntegerField()
    content_type = models.ForeignKey(ContentType, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    ordering = models.PositiveSmallIntegerField(verbose_name='Ordering')

    class Meta:
        verbose_name = 'Column'
        verbose_name_plural = 'Columns'

    def __str__(self):
        return str(self.row.pk) + ' - ' + str(self.pk) + ' - ' + str(self.width)


class Content(TimestampAble):
    content = models.TextField()

    class Meta:
        verbose_name = 'Text'
        verbose_name_plural = 'Texts'

    def content_type(self):
        return 'content'

    def __str__(self):
        return str(self.pk)


class File(TimestampAble):
    name = models.CharField(max_length=255, verbose_name='Name')
    file = fields.FileField(upload_to='files/%Y/%m/%d', verbose_name='File')

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'

    def content_type(self):
        return 'file'

    def __str__(self):
        return self.name


class Photo(TimestampAble):
    name = models.CharField(max_length=255, verbose_name='Name')
    photo = fields.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Photo')

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photo\'s'

    def content_type(self):
        return 'photo'

    def __str__(self):
        return self.name


class Form(TimestampAble):
    message = fields.TextField(verbose_name='Thank you message')

    class Meta:
        verbose_name = 'Form'
        verbose_name_plural = 'Forms'

    def content_type(self):
        return 'form'

    def __str__(self):
        return str(self.pk)


class FormElement(TimestampAble):
    form = models.ForeignKey(Form, verbose_name='Form')
    name = models.CharField(max_length=255, verbose_name='Element name')
    required = models.BooleanField(verbose_name='Required?')

    class Meta:
        verbose_name = 'Form element'
        verbose_name_plural = 'Form elements'

    def __str__(self):
        return self.name
