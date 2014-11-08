# -*- coding: utf-8 -*-
from papermill.views import (
    BasePostDetailView, BasePostsListView, BaseListTaggedPostsView
)

from .models import Post


class PostDetailView(BasePostDetailView):
    model = Post


class PostsListView(BasePostsListView):
    model = Post


class ListTaggedPostsView(BaseListTaggedPostsView):
    model = Post
