# -*- coding: utf-8 -*-
from django.views.generic import DetailView, ListView

from .models import BasePost
from .settings import PAPERMILL_SETTINGS


class BasePostDetailView(DetailView):
    model = BasePost
    context_object_name = "post"
    template_name = "papermill/detail.html"

    def get_queryset(self):
        return self.model.published.all().filter(
            slug__iexact=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(BasePostDetailView, self).get_context_data(**kwargs)
        context['posts'] = self.model.latest.posts(count=10)
        context['title_prefix'] = PAPERMILL_SETTINGS['title_prefix']

        try:
            context['prev'] = self.object.get_previous_by_publish_at()
        except:
            pass
        return context


class BasePostsListView(ListView):
    model = BasePost
    context_object_name = "posts"
    template_name = "papermill/list.html"
    paginate_by = PAPERMILL_SETTINGS['paginate_by']

    def get_queryset(self):
        return self.model.published.all().order_by('-featured', '-pk')

    def get_context_data(self, **kwargs):
        context = super(BasePostsListView, self).get_context_data(**kwargs)
        context['title_prefix'] = PAPERMILL_SETTINGS['title_prefix']
        return context


class BaseListTaggedPostsView(ListView):
    model = BasePost
    context_object_name = "posts"
    template_name = "papermill/list.html"

    def get_queryset(self):
        return self.model.published.all().filter(
            tags__slug__in=[self.kwargs['slug']])

    def get_context_data(self, **kwargs):
        context = super(
            BaseListTaggedPostsView, self).get_context_data(**kwargs)
        context['title_prefix'] = PAPERMILL_SETTINGS['title_prefix']

        return context
