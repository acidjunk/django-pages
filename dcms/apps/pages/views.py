from django.shortcuts import render
from .models import Page, Row, Column, Content, Photo, File
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.conf import settings
import forms


def IndexView(request):
    return render(request, 'index.html')


def parent_pages(pk):
    page = Page.objects.get(pk=pk)
    tree = []
    tree.append({'title': page.name, 'url': page.url})
    if page.parent:
        tree = parent_pages(page.parent_id) + tree
    return tree


def PageView(request, slug):
    page = Page.objects.get(url=slug)

    rows_ = []
    rows = Row.objects.filter(page=page).order_by('ordering').all()
    for row in rows:
        columns = Column.objects.filter(row=row).order_by('ordering').all()
        rows_.append({'id': row.id, 'columns': columns})

    breadcrumbs = parent_pages(page.id)

    if request.user.is_staff:
        if request.method == 'POST':
            content_id = request.POST.get('content_id', None)
            file = request.FILES.get('file', None)
            if content_id and file:
                photo = Photo.objects.get(pk=content_id)
                photo.photo = file
                photo.created_by = request.user
                photo.name = file.name
                photo.save()

    if page.sidebar_right:
        subpages = Page.objects.filter(parent=page.pk).order_by('ordering').all()
        sidebar_right = {'subpages': subpages}
    else:
        sidebar_right = None

    context = {'breadcrumbs': breadcrumbs, 'page': page, 'rows': rows_, 'sidebar_right': sidebar_right}

    return render(request, 'page.html', context=context)


@staff_member_required
def ItemAddView(request, page_url, colomn_id, content_type):
    if content_type == 'text':
        item = Content.objects.create(created_by=request.user)
        item.content = 'Test tekst'
        item.save()
    if content_type == 'photo':
        item = Photo.objects.create(created_by=request.user)
        item.photo = None
        item.save()

    column = Column.objects.get(pk=colomn_id)
    column.content_object = item
    column.save()

    return redirect('page', page_url)


@staff_member_required
def ItemRemoveView(request, page_url, colomn_id, content_type, object_id):

    column = Column.objects.get(pk=colomn_id)
    column.content_object = None
    column.save()

    if content_type == 'content':
        item = Content.objects.get(pk=object_id)
    if content_type == 'photo':
        item = Photo.objects.get(pk=object_id)

    item.delete()

    return redirect('page', page_url)


@staff_member_required
def ContentSaveView(request):
    if request.method == 'POST':
        content = request.POST.get('content', None)
        content_id = request.POST.get('content_id', None)

        con = Content.objects.get(pk=content_id)
        if con:
            con.content = content
            con.save()
            return render(request, 'response_200.html')
        else:
            return render(request, 'response_404.html')
    else:
        return render(request, 'response_404.html')


@staff_member_required
def RowAddView(request, page_url):
    page = Page.objects.get(url=page_url)
    orders = Row.objects.filter(page=page).count()
    row = Row.objects.create(page=page, ordering=orders+1, created_by=request.user)
    row.save()
    return redirect('page', page_url)


@staff_member_required
def RowDeleteView(request, page_url, row_id):
    row = Row.objects.get(pk=row_id)
    columns = Column.objects.filter(row=row).all()
    for x in columns:
        if x.content_type:
            x.content_object.delete()
        x.delete()
    row.delete()
    return redirect('page', page_url)


@staff_member_required
def ColumnAddView(request, page_url, row_id):
    columns = Column.objects.filter(row_id=row_id).all()
    count = Column.objects.filter(row_id=row_id).count()
    if count > 0:
        for x in columns:
            x.width = 12/(count+1)
            x.save()
        width = 12/(count+1)
    else:
        width = 12

    column = Column.objects.create(row_id=row_id, width=width, ordering=count+1, created_by=request.user)
    column.save()
    return redirect('page', page_url)


@staff_member_required
def ColumnDeleteView(request, page_url, row_id, column_id):
    columns = Column.objects.filter(row_id=row_id).all()
    count = Column.objects.filter(row_id=row_id).count()
    column = Column.objects.get(pk=column_id)
    for x in columns:
        if x != column:
            x.width = 12/(count-1)
            x.save()

    if column.content_object:
        column.content_object.delete()
    column.delete()
    return redirect('page', page_url)


@staff_member_required
def ColumnSortableView(request):
    col = request.POST.get('col_id', None)
    row = request.POST.get('row', None)
    ordering = 0
    for key in request.POST.getlist('col[]'):
        column = Column.objects.get(pk=key)
        column.ordering = ordering
        column.save()
        ordering += 1

    return render(request, 'response_200.html')


@staff_member_required
def RowSortableView(request):
    ordering = 0
    for key in request.POST.getlist('row[]'):
        row = Row.objects.get(pk=key)
        row.ordering = ordering
        row.save()
        ordering += 1

    return render(request, 'response_200.html')


@staff_member_required
def PagesView(request, parent=None):
    pages = Page.objects.filter(parent=parent).order_by('ordering').all()
    tree = []
    for x in pages:
        tree.append({'page': x, 'childs': Page.objects.filter(parent=x.pk).count()})
    context = {'tree': tree, 'parent': parent}
    return render(request, 'cms/pages.html', context=context)


@staff_member_required
def CMSIndexView(request):
    context = {}
    return render(request, 'cms/index.html', context=context)


@staff_member_required
def PageAddView(request):
    if request.method == "POST":
        form = forms.PageForm(request.POST)
        if form.is_valid():
            last_item = Page.objects.order_by('-ordering').first()
            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            model_instance = form.save(commit=False)
            model_instance.ordering = last_item.ordering+1
            model_instance.created_by = request.user
            model_instance.save()
            return redirect('pages')
    else:
        form = forms.PageForm()
    context = {'form': form}
    return render(request, 'cms/page-add.html', context=context)


@staff_member_required
def PageEditView(request, page_url):
    page = Page.objects.get(url=page_url)
    if request.method == "POST":
        form = forms.PageForm(request.POST, instance=page)
        if form.is_valid():
            # last_item = Page.objects.order_by('-ordering').first()
            # # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            model_instance = form.save(commit=False)
            # model_instance.ordering = last_item.ordering+1
            model_instance.save()
            return redirect('page', page_url)
    else:
        form = forms.PageForm(instance=page)
    context = {'form': form, 'page': page}
    return render(request, 'cms/page-edit.html', context=context)


@staff_member_required
def PageSortableView(request):
    parent = request.POST.get('parent', None)
    ordering = 0
    for key in request.POST.getlist('page[]'):
        page = Page.objects.get(pk=key)
        page.ordering = ordering
        page.save()
        ordering += 1

    return render(request, 'response_200.html')


@staff_member_required
def PhotosView(request):
    photos = Photo.objects.all()
    context = {'photos': photos}
    return render(request, 'cms/photos.html', context=context)


@staff_member_required
def FilesView(request):
    files = File.objects.all()
    context = {'files': files}
    return render(request, 'cms/files.html', context=context)


@staff_member_required
def FormsView(request):
    return render(request, 'cms/forms.html')


@staff_member_required
def FileAddView(request):
    if request.method == "POST":
        form = forms.FileForm(request.POST, request.FILES)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.created_by = request.user
            model_instance.save()

            return redirect('files')
    else:
        form = forms.FileForm()
    context = {'form': form}
    return render(request, 'cms/file-add.html', context=context)


@staff_member_required
def PhotoAddView(request):
    if request.method == "POST":
        form = forms.PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.created_by = request.user
            model_instance.save()
            return redirect('photos')
    else:
        form = forms.PhotoForm()
    context = {'form': form}
    return render(request, 'cms/photo-add.html', context=context)


@staff_member_required
def PhotoBrowserView(request):
    photos = Photo.objects.all()
    context = {'photos': photos}
    return render(request, 'cms/photo-browser.html', context=context)


@staff_member_required
def FileBrowserView(request):
    files = File.objects.all()
    context = {'files': files}
    return render(request, 'cms/file-browser.html', context=context)


@csrf_exempt
@staff_member_required
def PhotoUploadView(request):
    if request.FILES['upload']:
        request.FILES['photo'] = request.FILES['upload']
        request.POST['name'] = 'name'
    form = forms.PhotoForm(request.POST, request.FILES)
    if form.is_valid():
        model_instance = form.save(commit=False)
        model_instance.name = request.FILES['upload'].name.split('.')[0]
        model_instance.created_by = request.user
        model_instance.save()
        return HttpResponse("""
        <script type='text/javascript'>
            window.parent.CKEDITOR.tools.callFunction({0}, '{1}');
        </script>""".format(request.GET['CKEditorFuncNum'], model_instance.photo.url))


@csrf_exempt
@staff_member_required
def FileUploadView(request):
    if request.FILES['upload']:
        request.FILES['file'] = request.FILES['upload']
        request.POST['name'] = 'name'
    form = forms.FileForm(request.POST, request.FILES)
    if form.is_valid():
        model_instance = form.save(commit=False)
        model_instance.name = request.FILES['upload'].name.split('.')[0]
        model_instance.created_by = request.user
        model_instance.save()
        return HttpResponse("""
        <script type='text/javascript'>
            window.parent.CKEDITOR.tools.callFunction({0}, '{1}');
        </script>""".format(request.GET['CKEditorFuncNum'], model_instance.file.url))
