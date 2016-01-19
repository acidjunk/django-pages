from django.core import urlresolvers
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from smartfields import fields
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# from .grid_validator import GridValidator, GridCellValidator


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
    # language = models.CharField()
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    class Meta:
        abstract = True


class PageFAQ(TimestampAble, AbstractPage):
    question = models.TextField(verbose_name='Question')
    answer = models.TextField(verbose_name='Answer')

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return 'FAQ: {0}'.format(self.question)


class PageLink(TimestampAble, AbstractPage):
    name = models.TextField(verbose_name='Title') 
    link = models.TextField(verbose_name='Link')

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'

    # def content_type(self):
    #     return 'title','link'

    def __str__(self):
        return 'Internal Link: {0}'.format(self.name)


class PageYoutubeLink(TimestampAble, AbstractPage):
    name = models.TextField(verbose_name='Title') 
    link = models.TextField(verbose_name='Link')

    class Meta:
        verbose_name = 'Youtube link'
        verbose_name_plural = 'Youtube links'

    def __str__(self):
        return 'Youtube Link: {0}'.format(self.name)


class PageFacebookLink(TimestampAble, AbstractPage):
    name = models.TextField(verbose_name='Title') 
    link = models.TextField(verbose_name='Link')

    class Meta:
        verbose_name = 'Facebook link'
        verbose_name_plural = 'Facebook links'

    def __str__(self):
        return str(self.pk)


class Page(TimestampAble, AbstractPage):
    name = models.CharField(max_length=255, verbose_name='Name')
    slogan = models.CharField(max_length=255, verbose_name='Slogan', blank=True, default='')
    summary = models.TextField(blank=True)
    parent = models.ForeignKey('Page', blank=True, null=True, verbose_name='Parent', related_name="Child")
    ordering = models.PositiveSmallIntegerField(verbose_name='Ordering')
    sidebar_right = models.BooleanField(default=True, verbose_name='Sidebar right?')

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'

    def __str__(self):
        return self.name


class GridCell(TimestampAble):
    CHOICES = (
        (1, 'one'),
        (2, 'two'),
        (3, 'three'),
        (4, 'four'),
        (5, 'five'),
        (6, 'six'),
        (7, 'seven'),
        (8, 'eight'),
        (9, 'nine'),
        (10, 'ten'),
        (11, 'eleven'),
        (12, 'twelve'),
        (13, 'thirteen'),
        (14, 'fourteen'),
        (15, 'fifteen'),
        (16, 'sixteen'),
    )
    # Link Cell to a page
    page = models.ForeignKey(Page, related_name='grid_cells', editable=False)

    # Content object
    content_type = models.ForeignKey(ContentType,
                                     verbose_name=_('content type'),
                                     related_name="content_type_set_for_%(class)s")
    object_pk = models.TextField(_('object ID'))
    content_object = GenericForeignKey(ct_field="content_type", fk_field="object_pk")

    # Cell properties
    horizontalSize = models.IntegerField(verbose_name='HorizontalSize', choices=CHOICES, default=1)
    horizontalPosition = models.IntegerField(verbose_name='HorizontalPosition', choices=CHOICES, default=1)
    verticalSize = models.IntegerField(verbose_name='VerticalSize', default=1)

    verticalPosition = models.IntegerField(verbose_name='VerticalPosition', default=0)

    # def validate_unique(self, exclude=None):
    #     Grid.add_cell(self)

    class Meta:
        verbose_name = 'Grid'
        verbose_name_plural = 'Grids'

    def get_content_object_url(self):
        """
        Get a URL suitable for redirecting to the content object.
        """
        return urlresolvers.reverse(
            "comments-url-redirect",
            args=(self.content_type_id, self.object_pk)
        )

    def __str__(self):
        return 'Model:{0}, ID:{1}'.format(self.content_type, self.object_pk)


class PageArticle(TimestampAble, AbstractPage):
    name = models.TextField(verbose_name='Title') 
    content = models.TextField(verbose_name='Content')

    class Meta:
        verbose_name = 'Content'
        verbose_name_plural = 'Content'

    def __str__(self):
        return 'Article: {0}'.format(self.name)


class PageFile(TimestampAble, AbstractPage):
    name = models.CharField(max_length=255, verbose_name='Name')
    file = fields.FileField(upload_to='files/%Y/%m/%d', verbose_name='File')

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'

    def __str__(self):
        return self.name


class PagePhoto(TimestampAble, AbstractPage):
    name = models.CharField(max_length=255, verbose_name='Name')
    photo = fields.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Photo')

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photo\'s'

    def __str__(self):
        return self.name


class PageForm(TimestampAble, AbstractPage):
    message = fields.TextField(verbose_name='Thank you message')

    class Meta:
        verbose_name = 'Form'
        verbose_name_plural = 'Forms'

    def __str__(self):
        return str(self.pk)


class PageFormElement(TimestampAble):
    form = models.ForeignKey(PageForm, verbose_name='Form', related_name="FormElement")
    name = models.CharField(max_length=255, verbose_name='Element name')
    required = models.BooleanField(verbose_name='Required?')

    class Meta:
        verbose_name = 'Form element'
        verbose_name_plural = 'Form elements'

    def __str__(self):
        return self.name
