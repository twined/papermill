from django.conf.urls import patterns, url

from .views import PostDetailView, ListPostsView, ListTaggedPostsView
from .feeds import LatestUpdatesFeed

urlpatterns = patterns(
    '',
    url(r'^$', ListPostsView.as_view(), name='list'),
    url(r'^tagged/(?P<slug>[-\w]+)/$',
        ListTaggedPostsView.as_view(), name='tag'),
    url(r'^(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d+)/(?P<slug>[-\w]+)/$',
        PostDetailView.as_view(), name='detail'),
    (r'^rss/$', LatestUpdatesFeed()),
)
