from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from smartfields import fields
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class TimestampAble(models.Model):
    created_on = models.DateTimeField(_("date/time created"), editable=False, auto_now_add=True)
    modified_on = models.DateTimeField(_("date/time modified"), editable=False, auto_now=True)
    created_by = models.ForeignKey(User, editable=False, related_name='%(app_label)s_%(class)s_created_by', null=True,
                                   default=None)
    modified_by = models.ForeignKey(User, editable=False, related_name='%(app_label)s_%(class)s_modified_by', null=True,
                                    default=None)

    class Meta:
        abstract = True


class AbstractPage(models.Model):
    #language = models.CharField()
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    class Meta:
        abstract = True


class GridObject(models.Model):
    horizontal = models.IntegerField(verbose_name='HorizontalPosition')
    vertical = models.IntegerField(verbose_name='VerticalPosition')

    class Meta:
        abstract = True


class PageFAQ(TimestampAble, AbstractPage):
    question = models.TextField(verbose_name='Question')
    answer = models.TextField(verbose_name='Answer')

    class Meta:
        verbose_name = 'Content'
        verbose_name_plural = 'Content'

    def content_type(self):
        return 'question','answer'

    def __str__(self):
        return str(self.pk)


class PageLink(TimestampAble, AbstractPage):
    title = models.TextField(verbose_name='Title')
    link = models.TextField(verbose_name='Link')

    class Meta:
        verbose_name = 'Content'
        verbose_name_plural = 'Content'

    def content_type(self):
        return 'title','link'

    def __str__(self):
        return str(self.pk)


class PageYoutubeLink(TimestampAble, AbstractPage):
    title = models.TextField(verbose_name='Title')
    link = models.TextField(verbose_name='Link')

    class Meta:
        verbose_name = 'Content'
        verbose_name_plural = 'Content'

    def content_type(self):
        return 'title','link'

    def __str__(self):
        return str(self.pk)


class PageFacebookLink(TimestampAble, AbstractPage):
    title = models.TextField(verbose_name='Title')
    link = models.TextField(verbose_name='Link')

    class Meta:
        verbose_name = 'Content'
        verbose_name_plural = 'Content'

    def content_type(self):
        return 'title','link'

    def __str__(self):
        return str(self.pk)


class Page(TimestampAble, AbstractPage):
    name = models.CharField(max_length=255, verbose_name='Name')
    slogan = models.CharField(max_length=255, verbose_name='Slogan')
    url = models.SlugField(max_length=255, verbose_name='Url', unique=True)  # todo remove in favor of abstract slug
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


class PageArticle(TimestampAble, AbstractPage):
    title = models.TextField(verbose_name='Title')
    content = models.TextField(verbose_name='Content')

    class Meta:
        verbose_name = 'Content'
        verbose_name_plural = 'Content'

    def content_type(self):
        return 'title','content'

    def __str__(self):
        return str(self.pk)


class PageFile(TimestampAble, AbstractPage):
    name = models.CharField(max_length=255, verbose_name='Name')
    file = fields.FileField(upload_to='files/%Y/%m/%d', verbose_name='File')

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'

    def content_type(self):
        return 'file'

    def __str__(self):
        return self.name


class PagePhoto(TimestampAble, AbstractPage):
    name = models.CharField(max_length=255, verbose_name='Name')
    photo = fields.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Photo')

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photo\'s'

    def content_type(self):
        return 'photo'

    def __str__(self):
        return self.name


class PageForm(TimestampAble, AbstractPage):
    message = fields.TextField(verbose_name='Thank you message')

    class Meta:
        verbose_name = 'Form'
        verbose_name_plural = 'Forms'

    def content_type(self):
        return 'form'

    def __str__(self):
        return str(self.pk)


class PageFormElement(TimestampAble):
    form = models.ForeignKey(PageForm, verbose_name='Form')
    name = models.CharField(max_length=255, verbose_name='Element name')
    required = models.BooleanField(verbose_name='Required?')

    class Meta:
        verbose_name = 'Form element'
        verbose_name_plural = 'Form elements'

    def __str__(self):
        return self.name
