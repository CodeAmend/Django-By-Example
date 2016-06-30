from django.conf.urls import url
from . import views
from .feeds import LatestPostsFeed

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<post_id>[0-9]+)/share/$', views.post_share, name='post_share'),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'),
    url(r'^feed/$', LatestPostsFeed(), name='post_feed'),
]
