from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin



urlpatterns = patterns(
    '',
    url(r'', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^pages/', include('demo_site.pages.urls', namespace='pages')),
    # optionally add possibility to load short url pages.
    # Todo: import pages an get working short URL
    # url(r'^(?P<slug>[-\w\d]+)$', views.PageView, name='page'),

)

