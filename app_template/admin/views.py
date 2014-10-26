# posts.py

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import (
    CreateView, ListView, UpdateView, DeleteView, DetailView, View
)

from cerebrum.utils import json_response
from cerebrum.views import LoginRequiredMixin

from imgin.views import (
    BaseImageCreateView, AJAXBaseImageHandleUploadView,
    AJAXBaseImageDeleteView, BaseImageListView,
    BaseAJAXFroalaBrowserView, BaseAJAXFroalaUploadView
)

from papermill.admin.views import (
    get_keywords, tweet
)

from papermill.admin.views import (
    BaseListPostView, BaseViewPostView, BaseCreatePostView,
    BaseUpdatePostView, BaseDeletePostView, BaseAJAXCheckSlugView
)

from ..models import (
    Post, PostImage
)
from ..forms import PostForm


class AJAXCheckSlugView(BaseAJAXCheckSlugView):
    model = Post


class ListPostView(BaseListPostView):
    model = Post


class ViewPostView(BaseViewPostView):
    model = Post


class CreatePostView(BaseCreatePostView):
    model = Post
    form_class = PostForm


class UpdatePostView(BaseUpdatePostView):
    model = Post
    form_class = PostForm


class DeletePostView(BaseDeletePostView):
    model = Post


# images

class AJAXFroalaBrowserView(BaseAJAXFroalaBrowserView):
    model = PostImage


class AJAXFroalaUploadView(BaseAJAXFroalaBrowserView):
    model = PostImage


class AddPostImageView(LoginRequiredMixin, BaseImageCreateView):
    model = PostImage


class ListPostImageView(LoginRequiredMixin, BaseImageListView):
    model = PostImage


class UploadPostImageView(LoginRequiredMixin,
                          AJAXBaseImageHandleUploadView):
    model = PostImage


class AJAXDeletePostImageView(LoginRequiredMixin,
                              AJAXBaseImageDeleteView):
    model = PostImage
