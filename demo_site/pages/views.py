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
from django.db.models import Max
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


class PageArticleList(ListView):
    model = PageArticle
    fields = ['name', 'content']
    paginate_by = 10
    template_name = 'pages/semantic-ui/page-article-list.html' #% = settings.DJANGO_PAGES_THEME


class PageArticleCreate(CreateView):
    model = PageArticle
    fields = ['slug', 'name', 'content']
    success_url = reverse_lazy('pages:article-list')
    template_name = 'pages/semantic-ui/page-article-form.html'


class PageArticleUpdate(UpdateView):
    model = PageArticle
    fields = ['slug', 'name', 'content']
    success_url = reverse_lazy('pages:article-list')
    template_name = 'pages/semantic-ui/page-article-form.html'


class PageArticleDelete(DeleteView):
    model = PageArticle
    fields = ['name', 'content']
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
    fields = ['name', 'link']
    paginate_by = 10
    template_name = 'pages/semantic-ui/page-link.html'


class PageLinkCreate(CreateView):
    model = PageLink
    fields = ['slug', 'name', 'link']
    success_url = reverse_lazy('pages:link-list')
    template_name = 'pages/semantic-ui/page-link-form.html'


class PageLinkUpdate(UpdateView):
    model = PageLink
    fields = ['slug', 'name', 'link']
    success_url = reverse_lazy('pages:link-list')
    template_name = 'pages/semantic-ui/page-link-form.html'


class PageLinkDelete(DeleteView):
    model = PageLink
    fields = ['name', 'link']
    success_url = reverse_lazy('pages:link-list')
    template_name = 'pages/semantic-ui/page-link-delete.html'


class PageLinkDetail(DetailView):
    model = PageLink


class PageYoutubeLinkList(ListView):
    model = PageYoutubeLink
    fields = ['name', 'link']
    paginate_by = 10
    template_name = 'pages/semantic-ui/page-youtubelink.html'


class PageYoutubeLinkCreate(CreateView):
    model = PageYoutubeLink
    fields = ['slug', 'name', 'link']
    success_url = reverse_lazy('pages:youtubelink-list')
    template_name = 'pages/semantic-ui/page-youtubelink-form.html'


class PageYoutubeLinkUpdate(UpdateView):
    model = PageYoutubeLink
    fields = ['slug', 'name', 'link']
    success_url = reverse_lazy('pages:youtubelink-list')
    template_name = 'pages/semantic-ui/page-youtubelink-form.html'


class PageYoutubeLinkDelete(DeleteView):
    model = PageYoutubeLink
    fields = ['name', 'link']
    success_url = reverse_lazy('pages:youtubelink-list')
    template_name = 'pages/semantic-ui/page-youtubelink-delete.html'


class PageYoutubeLinkDetail(DetailView):
    model = PageYoutubeLink


class PageFacebookLinkList(ListView):
    model = PageFacebookLink
    fields = ['name', 'link']
    paginate_by = 10
    template_name = 'pages/semantic-ui/page-facebooklink.html'


class PageFacebookLinkCreate(CreateView):
    model = PageFacebookLink
    fields = ['slug', 'name', 'link']
    success_url = reverse_lazy('pages:facebooklink-list')
    template_name = 'pages/semantic-ui/page-facebooklink-form.html'


class PageFacebookLinkUpdate(UpdateView):
    model = PageFacebookLink
    fields = ['slug', 'name', 'link']
    success_url = reverse_lazy('pages:facebooklink-list')
    template_name = 'pages/semantic-ui/page-facebooklink-form.html'


class PageFacebookLinkDelete(DeleteView):
    model = PageFacebookLink
    fields = ['name', 'link']
    success_url = reverse_lazy('pages:facebooklink-list')
    template_name = 'pages/semantic-ui/page-facebooklink-delete.html'


class PageFacebookLinkDetail(DetailView):
    model = PageFacebookLink







class PageList(ListView):
    model = Page
    fields = ['name', 'slug', 'ordering']
    paginate_by = 10
    template_name = 'pages/semantic-ui/page-list.html'


class PageListCreate(CreateView):
    model = Page
    fields = ['name', 'slogan', 'slug']
    success_url = reverse_lazy('pages:page-list')
    template_name = 'pages/semantic-ui/page-form.html'

    def form_valid(self, form):
        self.object = form.save(commit = False)
        # get highest current order nummer
        max_order = Page.objects.all().aggregate(Max('ordering'))['ordering__max']

        #max_order = Page.objects.filter('ordering').max
        #Page.objects.values('ordering').annotate(count=Count('pk'))
        # store new highest order nummer to DB

        self.object.ordering = max_order + 1
        #self.ordering = max_order + 1
        self.object.save()
        return super(PageListCreate, self).form_valid(form)

class PageUpdate(UpdateView):
    model = Page
    fields = ['name', 'slogan', 'ordering', 'slug']
    success_url = reverse_lazy('pages:page-list')
    template_name = 'pages/semantic-ui/page-form.html'


class PageDelete(DeleteView):
    model = Page
    fields = ['name', 'slug']
    success_url = reverse_lazy('pages:page-list')
    template_name = 'pages/semantic-ui/page-delete.html'


class PageDetail(DetailView):
    model = Page







class PageGrid2(TemplateView):
    model = GridObject
    template_name = 'pages/semantic-ui/page-grid.html'


class PageGrid(ListView):
    model = GridObject
    fields = ['name', 'link']
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
