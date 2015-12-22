from django.conf import settings
from django.shortcuts import render
from .models import Page, Row, Column, PageArticle, PagePhoto, PageFile, PageFAQ, PageLink, PageYoutubeLink,\
    PageFacebookLink, GridObject, GridRow
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#import forms


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
                photo = PagePhoto.objects.get(pk=content_id)
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
        item = PageArticle.objects.create(created_by=request.user)
        item.content = 'Test tekst'
        item.save()
    if content_type == 'photo':
        item = PagePhoto.objects.create(created_by=request.user)
        item.photo = None
        item.save()
    if content_type == 'form':
        item = None
        #item.save()


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
        item = PageArticle.objects.get(pk=object_id)
    if content_type == 'photo':
        item = PagePhoto.objects.get(pk=object_id)
    #TODO make the item become inactive instead of being deleted
    item.delete()

    return redirect('page', page_url)


@staff_member_required
def ContentSaveView(request):
    if request.method == 'POST':
        content = request.POST.get('content', None)
        content_id = request.POST.get('content_id', None)

        con = PageArticle.objects.get(pk=content_id)
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
            try:
                model_instance.ordering = last_item.ordering+1
            except:
                model_instance.ordering = 0
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
    photos = PagePhoto.objects.all()
    context = {'photos': photos}
    return render(request, 'cms/photos.html', context=context)


@staff_member_required
def FilesView(request):
    files = PageFile.objects.all()
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
    photos = PagePhoto.objects.all()
    context = {'photos': photos}
    return render(request, 'cms/photo-browser.html', context=context)


@staff_member_required
def FileBrowserView(request):
    files = PageFile.objects.all()
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


class PageArticleList(ListView):
    model = PageArticle
    fields = ['title', 'content']
    paginate_by = 10
    template_name = 'pages/semantic-ui/page-article-list.html' #% = settings.DJANGO_PAGES_THEME


class PageArticleCreate(CreateView):
    model = PageArticle
    fields = ['slug', 'title', 'content']
    success_url = reverse_lazy('pages:article-list')
    template_name = 'pages/semantic-ui/page-article-form.html'


class PageArticleUpdate(UpdateView):
    model = PageArticle
    fields = ['slug', 'title', 'content']
    success_url = reverse_lazy('pages:article-list')
    template_name = 'pages/semantic-ui/page-article-form.html'


class PageArticleDelete(DeleteView):
    model = PageArticle
    fields = ['title', 'content']
    success_url = reverse_lazy('pages:article-list')
    template_name = 'pages/semantic-ui/page-article-delete.html'


class PageArticleDetail(DetailView):
    model = PageArticle


class PageFAQList(ListView):
    model = PageFAQ
    fields = ['question', 'answer']
    paginate_by = 10
    template_name = 'pages/semantic-ui/page-faq.html'


class PageFAQCreate(CreateView):
    model = PageFAQ
    fields = ['slug', 'question', 'answer']
    success_url = reverse_lazy('pages:faq-list')
    template_name = 'pages/semantic-ui/page-faq-form.html'


class PageFAQUpdate(UpdateView):
    model = PageFAQ
    fields = ['slug', 'question', 'answer']
    success_url = reverse_lazy('pages:faq-list')
    template_name = 'pages/semantic-ui/page-faq-form.html'


class PageFAQDelete(DeleteView):
    model = PageFAQ
    fields = ['question', 'answer']
    success_url = reverse_lazy('pages:faq-list')
    template_name = 'pages/semantic-ui/page-faq-delete.html'


class PageFAQDetail(DetailView):
    model = PageFAQ


class PageLinkList(ListView):
    model = PageLink
    fields = ['title', 'link']
    paginate_by = 10
    template_name = 'pages/semantic-ui/page-link.html'


class PageLinkCreate(CreateView):
    model = PageLink
    fields = ['slug', 'title', 'link']
    success_url = reverse_lazy('pages:link-list')
    template_name = 'pages/semantic-ui/page-link-form.html'


class PageLinkUpdate(UpdateView):
    model = PageLink
    fields = ['slug', 'title', 'link']
    success_url = reverse_lazy('pages:link-list')
    template_name = 'pages/semantic-ui/page-link-form.html'


class PageLinkDelete(DeleteView):
    model = PageLink
    fields = ['title', 'link']
    success_url = reverse_lazy('pages:link-list')
    template_name = 'pages/semantic-ui/page-link-delete.html'


class PageLinkDetail(DetailView):
    model = PageLink


class PageYoutubeLinkList(ListView):
    model = PageYoutubeLink
    fields = ['title', 'link']
    paginate_by = 10
    template_name = 'pages/semantic-ui/page-youtubelink.html'


class PageYoutubeLinkCreate(CreateView):
    model = PageYoutubeLink
    fields = ['slug', 'title', 'link']
    success_url = reverse_lazy('pages:youtubelink-list')
    template_name = 'pages/semantic-ui/page-youtubelink-form.html'


class PageYoutubeLinkUpdate(UpdateView):
    model = PageYoutubeLink
    fields = ['slug', 'title', 'link']
    success_url = reverse_lazy('pages:youtubelink-list')
    template_name = 'pages/semantic-ui/page-youtubelink-form.html'


class PageYoutubeLinkDelete(DeleteView):
    model = PageYoutubeLink
    fields = ['title', 'link']
    success_url = reverse_lazy('pages:youtubelink-list')
    template_name = 'pages/semantic-ui/page-youtubelink-delete.html'


class PageYoutubeLinkDetail(DetailView):
    model = PageYoutubeLink


class PageFacebookLinkList(ListView):
    model = PageFacebookLink
    fields = ['title', 'link']
    paginate_by = 10
    template_name = 'pages/semantic-ui/page-facebooklink.html'


class PageFacebookLinkCreate(CreateView):
    model = PageFacebookLink
    fields = ['slug', 'title', 'link']
    success_url = reverse_lazy('pages:facebooklink-list')
    template_name = 'pages/semantic-ui/page-facebooklink-form.html'


class PageFacebookLinkUpdate(UpdateView):
    model = PageFacebookLink
    fields = ['slug', 'title', 'link']
    success_url = reverse_lazy('pages:facebooklink-list')
    template_name = 'pages/semantic-ui/page-facebooklink-form.html'


class PageFacebookLinkDelete(DeleteView):
    model = PageFacebookLink
    fields = ['title', 'link']
    success_url = reverse_lazy('pages:facebooklink-list')
    template_name = 'pages/semantic-ui/page-facebooklink-delete.html'


class PageFacebookLinkDetail(DetailView):
    model = PageFacebookLink


class PageGrid2(TemplateView):
    model = GridObject
    template_name = 'pages/semantic-ui/page-grid.html'


class PageGrid(ListView):
    model = GridObject
    fields = ['title', 'link']
    paginate_by = 10
    template_name = 'pages/semantic-ui/page-grid.html'


class PageGridCreate(CreateView):
    model = GridObject
    fields = ['slug', 'horizontalSize', 'Title', 'Content']
    success_url = reverse_lazy('pages:grid')
    template_name = 'pages/semantic-ui/page-grid-form.html'


class PageGridUpdate(UpdateView):
    model = GridObject
    fields = ['slug', 'horizontalSize', 'Title', 'Content']
    success_url = reverse_lazy('pages:grid')
    template_name = 'pages/semantic-ui/page-grid-form.html'


class PageGridDelete(DeleteView):
    model = GridObject
    fields = ['slug', 'horizontalSize', 'Title', 'Content']
    success_url = reverse_lazy('pages:grid')
    template_name = 'pages/semantic-ui/page-grid-delete.html'


class GridCell(object):
    def __init__(self, horizontal_position, vertical_position, horizontal_size, vertical_size):
        self.horizontal_size = horizontal_size
        self.vertical_size = vertical_size
        self.horizontal_position = horizontal_position
        self.vertical_position = vertical_position

        self.data = [[0 for _ in range(self.horizontal_size)] for _ in range(self.vertical_size)]

    def __str__(self):
        result = ''
        for row in self.data:
            for _ in row:
                result += 'x'
            result += '\n'

        return result


class Grid(object):
    height = 2
    width = 16

    def __init__(self):
        self._data = [[0 for _ in range(self.width)] for _ in range(self.height)]
        print(self._data)

    def __str__(self):
        result = ''
        for row in range(0, self.height):
            print('row', row)
            for col in range(0, self.width):
                print('col', self._data[row][col])
                if self._data[row][col] == 0:
                    result += '0'
                else:
                    result += '1'
            result += '\n'
        return result

    def is_place_able(self, cell):
        if (cell.horizontal_position + cell.horizontal_size) > self.width:
            return False
        else:
            return True

    def check_override(self, cell, save):
        objects_in_row = 0
        long_enough = False
        print('all', self._data)
        for row in self._data[cell.vertical_position]:
            print('row', row)
            for col in range(cell.horizontal_position, cell.horizontal_position+cell.horizontal_size):
                print('col', self._data[row][col])
                if self._data[row][col] == 0:
                    if objects_in_row == cell.horizontal_size:
                        long_enough = True
                        if save:
                            for colp in range(cell.horizontal_position, cell.horizontal_position+cell.horizontal_size):
                                self._data[row][colp] = 1
                    else:
                        objects_in_row += 1
                        # print(objects_in_row)
                else:
                    print("e1, 1", self._data[row][col])
                    pass
        return long_enough

    def remove_cell(self, cell, save):
        objects_in_row = 0
        long_enough = False
        for row in self._data[cell.vertical_position]:
            for col in range(cell.horizontal_position, cell.horizontal_position+cell.horizontal_size):
                print('col', self._data[row][col])
                if self._data[row][col] == 1:
                    if objects_in_row == cell.horizontal_size:
                        long_enough = True
                        if save:
                            for colp in range(cell.horizontal_position, cell.horizontal_position+cell.horizontal_size):
                                self._data[row][colp] = 0
                    else:
                        objects_in_row += 1
                        # print(objects_in_row)
                else:
                    print("e1, 1", self._data[row][col])
                    pass
        return long_enough

    def check_row_for_free_places(self, cell):
        free_places = 0
        for row in self._data[cell.vertical_position]:
            for col in range(cell.horizontal_position, cell.horizontal_position+cell.horizontal_size):
                print('col', self._data[row][col])
                if self._data[row][col] == 0:
                        free_places += 1
                        # print(free_places)
                else:
                    pass
        return free_places

    def check_for_free_space(self, cell):
        objects_in_row = 0
        free_spaces = []
        for row in self._data:
            for col in range(cell.horizontal_position, cell.horizontal_position+cell.horizontal_size):
                if row[col] == 0:
                    if objects_in_row == cell.horizontal_size:
                        free_spaces += row
                        objects_in_row = 0
                    else:
                        objects_in_row += 1

        return free_spaces

    def add_cell(self, cell):
        if self.is_place_able(cell):  # false = fits
            if self.check_override(cell, False):
                # TODO add specific location for cells? and not randomly assigned
                self.check_override(cell, True)
                pass
            else:
                print("cell overrides another")
        else:
            print("cell is too wide")

    def move_cell(self, cell):
        if self.check_override(cell, False):
            if self.remove_cell(cell, False):
                self.remove_cell(cell, True)
                # TODO make something to choose the new location
                self.add_cell(cell)
        else:
            print("cell does not fit somewhere else")
