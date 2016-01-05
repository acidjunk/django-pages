from django.conf.urls import url
from django.contrib.auth import views as auth_views
from demo_site.pages import views

urlpatterns = [
    # Test stuff
    url(r'^grid/(?P<slug>[-\w\d]+)$', views.PageGridList.as_view(), name='grid-list'),
    url(r'^grid/(?P<slug>[-\w\d]+)/new$', views.PageGridCreate.as_view(), name='grid-new'),
    url(r'^grid/edit/(?P<pk>\d+)$', views.PageGridUpdate.as_view(), name='grid-edit'),
    url(r'^grid/delete/(?P<pk>\d+)$', views.PageGridDelete.as_view(), name='grid-delete'),

    # Real stuff
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout_then_login, name='logout'),
    url(r'^page$', views.PageList.as_view(), name='page-list'),
    url(r'^page/new/', views.PageListCreate.as_view(), name='page-new'),
    url(r'^page/edit/(?P<pk>\d+)$', views.PageUpdate.as_view(), name='page-edit'),
    url(r'^page/delete/(?P<pk>\d+)$', views.PageDelete.as_view(),name='page-delete'),


    url(r'^article$', views.PageArticleList.as_view(), name='article-list'),
    url(r'^article/(?P<pk>\d+)$', views.PageArticleDetail.as_view(), name='article-detail'),
    url(r'^article/new$', views.PageArticleCreate.as_view(), name='article-new'),
    url(r'^article/edit/(?P<pk>\d+)$', views.PageArticleUpdate.as_view(), name='article-edit'),
    url(r'^article/delete/(?P<pk>\d+)$', views.PageArticleDelete.as_view(), name='article-delete'),
    url(r'^faq$', views.PageFAQList.as_view(), name='faq-list'),
    url(r'^faq/(?P<pk>\d+)$', views.PageFAQDetail.as_view(), name='faq-detail'),
    url(r'^faq/new$', views.PageFAQCreate.as_view(), name='faq-new'),
    url(r'^faq/edit/(?P<pk>\d+)$', views.PageFAQUpdate.as_view(), name='faq-edit'),
    url(r'^faq/delete/(?P<pk>\d+)$', views.PageFAQDelete.as_view(), name='faq-delete'),
    url(r'^link$', views.PageLinkList.as_view(), name='link-list'),
    url(r'^link/(?P<pk>\d+)$', views.PageLinkDetail.as_view(), name='link-detail'),
    url(r'^link/new$', views.PageLinkCreate.as_view(), name='link-new'),
    url(r'^link/edit/(?P<pk>\d+)$', views.PageLinkUpdate.as_view(), name='link-edit'),
    url(r'^link/delete/(?P<pk>\d+)$', views.PageLinkDelete.as_view(), name='link-delete'),
    url(r'^youtubelink$', views.PageYoutubeLinkList.as_view(), name='youtubelink-list'),
    url(r'^youtubelink/(?P<pk>\d+)$', views.PageYoutubeLinkDetail.as_view(), name='youtubelink-detail'),
    url(r'^youtubelink/new$', views.PageYoutubeLinkCreate.as_view(), name='youtubelink-new'),
    url(r'^youtubelink/edit/(?P<pk>\d+)$', views.PageYoutubeLinkUpdate.as_view(), name='youtubelink-edit'),
    url(r'^youtubelink/delete/(?P<pk>\d+)$', views.PageYoutubeLinkDelete.as_view(),
        name='youtubelink-delete'),
    url(r'^facebooklink$', views.PageFacebookLinkList.as_view(), name='facebooklink-list'),
    url(r'^facebooklink/(?P<pk>\d+)$', views.PageFacebookLinkDetail.as_view(), name='facebooklink-detail'),
    url(r'^facebooklink/new$', views.PageFacebookLinkCreate.as_view(), name='facebooklink-new'),
    url(r'^facebooklink/edit/(?P<pk>\d+)$', views.PageFacebookLinkUpdate.as_view(), name='facebooklink-edit'),
    url(r'^facebooklink/delete/(?P<pk>\d+)$', views.PageFacebookLinkDelete.as_view(),
        name='facebooklink-delete'),
    # url(r'^(?P<slug>[-\w\d]+)$', views.PageView, name='page'),
    #url(r'^', views.IndexView, name='default'),
]
