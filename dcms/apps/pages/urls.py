"""dcms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from dcms.apps.pages import views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout_then_login, name='logout'),

    url(r'^row/add/(?P<page_url>[-\w\d]+)/', views.RowAddView, name='row-add'),
    url(r'^row/delete/(?P<page_url>[-\w\d]+)/(?P<row_id>[\d]+)/', views.RowDeleteView, name='row-delete'),
    url(r'^row/sortable/', views.RowSortableView, name='row-sortable'),

    url(r'^column/add/(?P<page_url>[-\w\d]+)/(?P<row_id>[\d]+)/', views.ColumnAddView, name='column-add'),
    url(r'^column/delete/(?P<page_url>[-\w\d]+)/(?P<row_id>[\d]+)/(?P<column_id>[\d]+)/', views.ColumnDeleteView, name='column-delete'),
    url(r'^column/sortable/', views.ColumnSortableView, name='column-sortable'),

    url(r'^content/save/$', views.ContentSaveView, name='content-save'),

    url(r'^item/add/(?P<page_url>[-\w\d]+)/(?P<colomn_id>[\d]+)/(?P<content_type>[\w\d]+)/', views.ItemAddView, name='item-add'),
    url(r'^item/remove/(?P<page_url>[-\w\d]+)/(?P<colomn_id>[\d]+)/(?P<content_type>[\w\d]+)/(?P<object_id>[\d]+)/', views.ItemRemoveView, name='item-remove'),

    url(r'^cms/', views.CMSIndexView, name='cms'),

    url(r'^pages/sortable/', views.PageSortableView, name='pages-sortable'),
    url(r'^pages/(?P<parent>[\d]+)/', views.PagesView, name='pages-parent'),
    url(r'^pages/', views.PagesView, name='pages'),

    url(r'^forms/$', views.FormsView, name='forms'),

    url(r'^photos/$', views.PhotosView, name='photos'),
    url(r'^photo/add/$', views.PhotoAddView, name='photo-add'),
    url(r'^photo/browser/$', views.PhotoBrowserView, name='photo-browser'),
    url(r'^photo/uploader/$', views.PhotoUploadView, name='photo-uploader'),

    url(r'^files/$', views.FilesView, name='files'),
    url(r'^file/add/$', views.FileAddView, name='file-add'),
    url(r'^file/browser/$', views.FileBrowserView, name='file-browser'),
    url(r'^file/uploader/$', views.FileUploadView, name='file-uploader'),

    url(r'^page/add/', views.PageAddView, name='page-add'),
    url(r'^page/edit/(?P<page_url>[-\w\d]+)/', views.PageEditView, name='page-edit'),



    url(r'^page-article/$', views.PageArticleList.as_view(), name='page-article-list'),
    url(r'^page-article/(?P<pk>\d+)$', views.PageArticleDetail.as_view(), name='page-article-detail'),
    url(r'^page-article/new/$', views.PageArticleCreate.as_view(), name='page-article-new'),
    url(r'^page-article/edit/(?P<pk>\d+)$', views.PageArticleUpdate.as_view(), name='page-article-edit'),
    url(r'^page-article/delete/(?P<pk>\d+)$', views.PageArticleDelete.as_view(), name='page-article-delete'),

    url(r'^(?P<slug>[-\w\d]+)/$', views.PageView, name='page'),
    url(r'^', views.IndexView, name='default'),

]
