from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse_lazy
from .models import Post


class PostsListSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return [reverse_lazy('posts:list')]

    def location(self, obj):
        return obj

    def lastmod(self, obj):
        post = Post.published.all().order_by('-updated')[:1]
        if post:
            return post[0].updated


class PostDetailSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.updated
