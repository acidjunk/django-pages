from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^tag-cloud$', views.tag_cloud, name='tag-cloud'),
    url(r'^tag-it/(?P<model>\w+)/(?P<model_id>\d+)$', views.tag_it, name='tag-it'),
    url(r'^tag/del/(?P<id>\d+)$', views.tag_del, name='tag-del'),
    url(r'^go-back$', views.go_back, name='go-back'),
)
