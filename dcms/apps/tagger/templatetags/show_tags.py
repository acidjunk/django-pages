from django import template
from ..models import Tag, TaggedItem
from django.contrib.contenttypes.models import ContentType
from ..forms import TagItForm

register = template.Library()

def show_tags(model, pk):
    object_type = ContentType.objects.get(model=model)
    tagged_items=TaggedItem.objects.filter(content_type=object_type.id, object_id=pk)
  #  print tagged_items
    return {'tagged_items': tagged_items, 'model': model, 'pk': pk}

register.inclusion_tag('tagger/templatetags/show_tags.html')(show_tags)


@register.inclusion_tag('tag_it_ajax.html', takes_context=True)
def tag_this(context, model, model_id):
    request = context['request']
    user = request.user
    content_type = ContentType.objects.get(model=model)

    if request.method == 'POST':
        tag_new = request.POST.get('tag_new', None)
        tag = request.POST.get('tag', None)
        if tag_new:
            tag = Tag(tag=tag_new, created_by=user)
            tag.save()
            tagged_item = TaggedItem(content_type=content_type, object_id=model_id)
            tagged_item.created_by = user
            tagged_item.tag = tag
            tagged_item.save()
        elif tag:
            tag = Tag.objects.get(id=tag)
            tagged_item = TaggedItem(content_type=content_type, object_id=model_id)
            tagged_item.created_by = user
            tagged_item.tag = tag
            tagged_item.save()

    form = TagItForm()
    tags = TaggedItem.objects.filter(content_type=content_type, object_id=model_id).all()
    form.fields["tag"].queryset = Tag.objects.exclude(tag__in=[o.tag for o in tags])

    context_dict = {'request': request, 'form': form, 'tags': tags}
    return context_dict
