from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from .pages import views

urlpatterns = patterns(
    '',
    url(r'', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^pages/', include('demo_site.pages.urls', namespace='pages')),
    url(r'^(?P<slug>[-\w\d]+)$', views.PageDetail.as_view(), name='page-detail'),
    url(r'^.*$', RedirectView.as_view(url='pages/page', permanent=False), name='index')
)
