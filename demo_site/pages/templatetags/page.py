from django import template

register = template.Library()

# from django.utils.safestring import mark_safe
from ..models import Page


@register.inclusion_tag('page_navigation.html', takes_context=True)
def page_navigation(context):
    tree = []
    pages = Page.objects.filter(parent=None).order_by('ordering').all()
    for page in pages:
        childs = Page.objects.filter(parent=page.pk).count()
        childs_tree = []
        if childs > 0:
            ch = Page.objects.filter(parent=page.pk).order_by('ordering').all()
            for child in ch:
                chil = Page.objects.filter(parent=child.pk).count()
                chil_tree = []
                if chil > 0:
                    chi = Page.objects.filter(parent=child.pk).order_by('ordering').all()
                    for ch in chi:
                        chil_tree.append({'title': ch.name, 'url': ch.url})
                childs_tree.append({'title': child.name, 'url': child.url, 'childs': chil_tree})
        tree.append({'title': page.name, 'url': page.url, 'childs': childs_tree})
    return {'tree': tree, 'request': context['request']}


@register.inclusion_tag('page_content_load.html', takes_context=True)
def content_load(context, content_object):
    is_staff = context['request'].user.is_staff
    return {'is_staff': is_staff, 'content_object': content_object}
