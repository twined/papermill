# -*- coding: utf-8 -*-
from django.views.generic import DetailView, ListView

from hiver.views import CacheMixin

from .models import Post
from .settings import PAPERMILL_SETTINGS


class PostDetailView(CacheMixin, DetailView):
    model = Post
    context_object_name = "post"
    template_name = "papermill/detail.html"
    cache_path = "posts.view"

    def get_queryset(self):
        return Post.published.all().filter(
            slug__iexact=self.kwargs['slug'],
            post_type=self.kwargs['post_type'])

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['posts'] = Post.latest.posts(count=10)
        context['title_prefix'] = PAPERMILL_SETTINGS['title_prefix']

        try:
            context['prev'] = self.object.get_previous_by_publish_at(
                post_type__exact=self.object.post_type)
        except:
            pass
        return context


class ListPostsView(CacheMixin, ListView):
    model = Post
    context_object_name = "posts"
    cache_path = "posts.list"
    template_name = "papermill/list.html"
    paginate_by = PAPERMILL_SETTINGS['paginate_by']

    def get_queryset(self):
        return Post.published.all().order_by('-pk')  # [:10]

    def get_context_data(self, **kwargs):
        context = super(ListPostsView, self).get_context_data(**kwargs)
        context['title_prefix'] = PAPERMILL_SETTINGS['title_prefix']

        return context


class ListTaggedPostsView(CacheMixin, ListView):
    model = Post
    context_object_name = "posts"
    cache_path = "posts.tagged"
    template_name = "papermill/list.html"

    def get_queryset(self):
        return Post.published.all().filter(
            tags__slug__in=[self.kwargs['slug']])

    def get_context_data(self, **kwargs):
        context = super(ListTaggedPostsView, self).get_context_data(**kwargs)
        context['title_prefix'] = PAPERMILL_SETTINGS['title_prefix']

        return context
