# -*- coding: utf-8 -*-
from papermill.views import (
    BasePostDetailView, BaseListPostsView, BaseListTaggedPostsView
)

from .models import Post


class PostDetailView(BasePostDetailView):
    model = Post


class ListPostsView(BaseListPostsView):
    model = Post


class ListTaggedPostsView(BaseListTaggedPostsView):
    model = Post
