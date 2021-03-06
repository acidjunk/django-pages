from django.utils.functional import cached_property
from django.shortcuts import render, get_object_or_404
from .models import Page, PageArticle, PageFAQ, PageLink, PageYoutubeLink,\
    PageFacebookLink, GridCell

from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Max


def IndexView(request):
    return render(request, 'index.html')


def parent_pages(pk):
    page = Page.objects.get(pk=pk)
    tree = []
    tree.append({'title': page.name, 'url': page.url})
    if page.parent:
        tree = parent_pages(page.parent_id) + tree
    return tree


class PageArticleList(ListView):
    model = PageArticle
    fields = ['name', 'content']
    paginate_by = 10
    template_name = 'pages/semantic-ui/page-article-list.html'  # % = settings.DJANGO_PAGES_THEME


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
        self.object = form.save(commit=False)
        # get highest current order number
        max_order = Page.objects.all().aggregate(Max('ordering'))['ordering__max']
        self.object.ordering = (max_order or 0) + 1
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
    template_name = 'pages/semantic-ui/page-detail.html'

    @cached_property
    def page(self):
        return get_object_or_404(Page, slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(PageDetail, self).get_context_data(**kwargs)

        context['grid_items'] = GridCell.objects.filter(page=self.page)

        object_instances = []
        object_instances1 = []
        object_instances2 = []
        object_instances3 = []
        for instance in GridCell.objects.filter(page=self.page):
            if instance.content_type.name == 'Youtube link':
                object_instances.append(PageYoutubeLink.objects.filter(id=instance.object_pk))
            else:
                if instance.content_type.name == "FAQ":
                    object_instances1.append(PageFAQ.objects.filter(id=instance.object_pk))
                else:
                    if instance.content_type.name == "Link":
                        object_instances2.append(PageLink.objects.filter(id=instance.object_pk))
                    else:
                        if instance.content_type.name == "Content":
                            object_instances3.append(PageArticle.objects.filter(id=instance.object_pk))

        context['item_instances'] = object_instances
        context['item_instances1'] = object_instances1
        context['item_instances2'] = object_instances2
        context['item_instances3'] = object_instances3

        return context


class PageGridList(ListView):
    model = GridCell
    fields = ['page', 'horizontalPosition', 'horizontalSize', 'verticalPosition', 'verticalSize']
    paginate_by = 10
    template_name = 'pages/semantic-ui/page-grid.html'

    @cached_property
    def page(self):
        return get_object_or_404(Page, slug=self.kwargs['slug'])

    def get_queryset(self):
        return GridCell.objects.filter(page=self.page)

    def get_context_data(self, **kwargs):
        context = super(PageGridList, self).get_context_data(**kwargs)
        context['page'] = self.page
        context['preview_page'] = self.page.slug
        return context


class PageGridCreate(CreateView):
    model = GridCell
    fields = ['content_type', 'object_pk', 'horizontalPosition', 'horizontalSize', 'verticalPosition', 'verticalSize']
    success_url = reverse_lazy('pages:article-list')
    template_name = 'pages/semantic-ui/page-grid-form.html'

    @cached_property
    def page(self):
        return get_object_or_404(Page, slug=self.kwargs['slug'])

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.page = self.page
        self.object.save()
        return super(PageGridCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PageGridCreate, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    def get_success_url(self):
        return reverse('pages:grid-list', kwargs={'slug': self.page.slug})


class PageGridUpdate(UpdateView):
    model = GridCell
    fields = ['content_type', 'object_pk', 'horizontalPosition', 'horizontalSize', 'verticalPosition', 'verticalSize']
    # success_url = reverse_lazy('pages:article-list')

    template_name = 'pages/semantic-ui/page-grid-form.html'

    # @cached_property
    # def page(self):
    #     return get_object_or_404(Page, slug=self.kwargs['slug'])

    def get_success_url(self):
        return reverse('pages:grid-list', kwargs={'slug': self.object.page.slug})


class PageGridDelete(DeleteView):
    model = GridCell
    fields = ['slug', 'horizontalSize', 'name', 'content']
    # success_url = reverse_lazy("pages:article-list")
    template_name = 'pages/semantic-ui/page-grid-delete.html'

    def page(self):
        return get_object_or_404(Page, slug=self.kwargs['slug'])

    def get_success_url(self):
        return reverse('pages:grid-list', kwargs={'slug': self.object.page.slug})


class PageGridUpdate2(UpdateView):
    model = GridCell
    fields = ['content_type', 'object_pk', 'horizontalPosition', 'horizontalSize', 'verticalPosition', 'verticalSize']
    # success_url = reverse_lazy('pages:article-list')

    template_name = 'pages/semantic-ui/page-grid-form.html'

    # @cached_property
    # def page(self):
    #     return get_object_or_404(Page, slug=self.kwargs['slug'])

    def get_success_url(self):
        # <a href="{% url "page-detail" preview_page %}" class="purple ui button">Preview</a>
        return reverse('page-detail', kwargs={'slug': self.object.page.slug})


class PageGridDelete2(DeleteView):
    model = GridCell
    fields = ['slug', 'horizontalSize', 'name', 'content']
    # success_url = reverse_lazy("pages:article-list")
    template_name = 'pages/semantic-ui/page-grid-delete.html'

    def page(self):
        return get_object_or_404(Page, slug=self.kwargs['slug'])

    def get_success_url(self):
        return reverse('grid-list', kwargs={'slug': self.object.page.slug})
