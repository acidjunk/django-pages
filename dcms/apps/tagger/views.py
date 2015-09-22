from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Tag, TaggedItem
from .forms import TagItForm
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect


def tag_cloud(request):
    tags = Tag.objects.all()
    tag_list = []
    for tag in tags:
        tag_list.append((tag.tag, len(tag.tagged_items.all())))
    context_dict = {'tag_list': tag_list}
    return render(request, 'tagger/tag_cloud.html', context_dict)

@login_required
def tag_it(request, model, model_id):
    #Set nice return URL
    return_url=request.session.get('tagger_return_url', None)
    if not return_url:
        request.session['tagger_return_url']=request.META.get('HTTP_REFERER')

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
    tags = TaggedItem.objects.filter(content_type=content_type, object_id=model_id)
    form.fields["tag"].queryset = Tag.objects.exclude(tag__in=[o.tag for o in tags])

    context_dict = {'form': form, 'tags': tags}
    return render(request, 'tagger/tag_it.html', context_dict)

@login_required
def go_back(request):
    return_url=request.session.get('tagger_return_url', None)
    if return_url:
        del request.session['tagger_return_url']
        return redirect(return_url)
    else:
        # No return URL? This shouldn't happen. Anyway let's return to home
        return redirect('/')

@login_required
def tag_del(request, id):
    tagged_item = TaggedItem.objects.get(id=id)
    find_all_tagged_items = TaggedItem.objects.filter(tag=tagged_item.tag)
    if find_all_tagged_items.count() == 1:
        tag = Tag.objects.get(id=tagged_item.tag_id)
        tag.delete()
    else:
        tagged_item.delete()
    return redirect(request.META.get('HTTP_REFERER'))
