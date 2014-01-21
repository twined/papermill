from django.conf import settings
from django.contrib.syndication.views import Feed
from .models import Post


class LatestUpdatesFeed(Feed):
    """
    Returns feed data for latest news and blog posts
    """
    title = "%s - news updates" % getattr(settings, 'FEED_TITLE', '')
    link = "/news/"

    description = "Latest news and updates."

    def items(self):
        return Post.objects.all().filter(status=2).order_by('-created')[:10]

    def item_title(self, item):
        return item.header

    def item_description(self, item):
        return item.body
