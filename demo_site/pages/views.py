from django.conf import settings
from django.shortcuts import render
from .models import Page, Row, Column, PageArticle, PagePhoto, PageFile, PageFAQ, PageLink, PageYoutubeLink,\
    PageFacebookLink, GridObject
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
        self.object.ordering = max_order + 1
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








class PageGrid(ListView):
    model = GridObject
    fields = ['horizontalPosition','horizontalSize','verticalPosition','verticalSize']
    paginate_by = 10
    template_name = 'pages/semantic-ui/page-grid.html'


class PageGridCreate(CreateView):
    model = GridObject
    fields = ['horizontalPosition','horizontalSize','verticalPosition','verticalSize']
    success_url = reverse_lazy('pages:grid')
    template_name = 'pages/semantic-ui/page-grid-form.html'


class PageGridUpdate(UpdateView):
    model = GridObject
    fields = ['slug', 'horizontalSize', 'name', 'content']
    success_url = reverse_lazy('pages:grid')
    template_name = 'pages/semantic-ui/page-grid-form.html'


class PageGridDelete(DeleteView):
    model = GridObject
    fields = ['slug', 'horizontalSize', 'name', 'content']
    success_url = reverse_lazy('pages:grid')
    template_name = 'pages/semantic-ui/page-grid-delete.html'