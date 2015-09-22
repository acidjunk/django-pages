from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone


@python_2_unicode_compatible
class Tag(models.Model):
    tag = models.SlugField(unique=True)

    created_by = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now_add=timezone.now)
    modified_on = models.DateTimeField(auto_now=timezone.now)

    class Meta:
        get_latest_by = 'created_on'
        ordering = ('tag',)
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    def __str__(self):
        return self.tag


@python_2_unicode_compatible
class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, related_name='tagged_items')
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    created_by = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now_add=timezone.now)
    modified_on = models.DateTimeField(auto_now=timezone.now)

    class Meta:
        get_latest_by = 'created_on'
        ordering = ('tag',)
        verbose_name = 'tagged item'
        verbose_name_plural = 'tagged items'

    def __str__(self):
        return 'Model:%s, ID:%s, Tagname:%s'% (self.content_type, self.object_id, self.tag.tag)
