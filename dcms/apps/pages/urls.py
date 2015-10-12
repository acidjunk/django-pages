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

    url(r'^page-faq/$', views.PageFAQList.as_view(), name='page-faq-list'),
    url(r'^page-faq/(?P<pk>\d+)$', views.PageFAQDetail.as_view(), name='page-faq-detail'),
    url(r'^page-faq/new/$', views.PageFAQCreate.as_view(), name='page-faq-new'),
    url(r'^page-faq/edit/(?P<pk>\d+)$', views.PageFAQUpdate.as_view(), name='page-faq-edit'),
    url(r'^page-faq/delete/(?P<pk>\d+)$', views.PageFAQDelete.as_view(), name='page-faq-delete'),

    url(r'^page-link/$', views.PageLinkList.as_view(), name='page-link-list'),
    url(r'^page-link/(?P<pk>\d+)$', views.PageLinkDetail.as_view(), name='page-link-detail'),
    url(r'^page-link/new/$', views.PageLinkCreate.as_view(), name='page-link-new'),
    url(r'^page-link/edit/(?P<pk>\d+)$', views.PageLinkUpdate.as_view(), name='page-link-edit'),
    url(r'^page-link/delete/(?P<pk>\d+)$', views.PageLinkDelete.as_view(), name='page-link-delete'),

    url(r'^page-youtubelink/$', views.PageYoutubeLinkList.as_view(), name='page-youtubelink-list'),
    url(r'^page-youtubelink/(?P<pk>\d+)$', views.PageYoutubeLinkDetail.as_view(), name='page-youtubelink-detail'),
    url(r'^page-youtubelink/new/$', views.PageYoutubeLinkCreate.as_view(), name='page-youtubelink-new'),
    url(r'^page-youtubelink/edit/(?P<pk>\d+)$', views.PageYoutubeLinkUpdate.as_view(), name='page-youtubelink-edit'),
    url(r'^page-youtubelink/delete/(?P<pk>\d+)$', views.PageYoutubeLinkDelete.as_view(), name='page-youtubelink-delete'),

    url(r'^page-facebooklink/$', views.PageFacebookLinkList.as_view(), name='page-facebooklink-list'),
    url(r'^page-facebooklink/(?P<pk>\d+)$', views.PageFacebookLinkDetail.as_view(), name='page-facebooklink-detail'),
    url(r'^page-facebooklink/new/$', views.PageFacebookLinkCreate.as_view(), name='page-facebooklink-new'),
    url(r'^page-facebooklink/edit/(?P<pk>\d+)$', views.PageFacebookLinkUpdate.as_view(), name='page-facebooklink-edit'),
    url(r'^page-facebooklink/delete/(?P<pk>\d+)$', views.PageFacebookLinkDelete.as_view(), name='page-facebooklink-delete'),

    url(r'^(?P<slug>[-\w\d]+)/$', views.PageView, name='page'),
    url(r'^', views.IndexView, name='default'),

]
