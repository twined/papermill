# posts.py

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import redirect
from django.views.generic import (
    CreateView, ListView, UpdateView, DeleteView, DetailView
)

from cerebrum.views import LoginRequiredMixin
from cerebrum.utils import json_response
from imgin.views import (
    BaseImageCreateView, AJAXBaseImageHandleUploadView,
    AJAXBaseImageDeleteView, BaseImageListView, BaseCKEDITORBrowserView
)

from ..models import Post, PostImage
from ..forms import PostForm


@login_required
def get_keywords(request, *args, **kwargs):
    keywords = request.GET['text']
    return json_response({
        'keywords': keywords,
    })


@login_required
def tweet(request, pk):
    #post_to_twitter(request, Post.objects.get(pk=pk))
    #return redirect(reverse('admin:papermill:list'))
    pass


@login_required
def checkslug(request, pk=None, *args, **kwargs):
    if not 'slug' in request.GET:
        # slug wasn't passed.
        return json_response({
            'status': 400,
            'error_msg': 'No slug passed to posts::checkslug'
        })

    slug = request.GET['slug'].lower()

    if pk:
        # it's an edit. it's ok if it's the same as before
        post = Post.objects.get(pk=pk)
        if post.slug == slug:
            return json_response({
                'status': 200,
            })

    if Post.objects.all().filter(slug=slug):
        return json_response({
            'status': 300,
            'error_msg': 'Overskriften eksisterer allerede'
        })

    return json_response({
        'status': 200,
    })


class ListPostView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = "posts"
    template_name = "papermill/admin/list.html"

    def get_queryset(self):
        return Post.objects.order_by('status', '-pk')


class ViewPostView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "papermill/admin/detail.html"


class CreatePostView(LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = "papermill/admin/form.html"
    success_url = reverse_lazy('admin:papermill:list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user

        messages.success(self.request, "Innlegget er lagret", extra_tags='msg')
        return super(CreatePostView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Rett feilene under")
        return super(CreatePostView, self).form_invalid(form)


class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "papermill/admin/form.html"
    success_url = reverse_lazy('admin:papermill:list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        messages.success(self.request, "Endringen var vellykket.",
                         extra_tags='msg')
        return super(UpdatePostView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Rett feilene under")
        return super(UpdatePostView, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(UpdatePostView, self).get_context_data(**kwargs)
        context['body'] = self.object.body
        return context


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "papermill/admin/post_confirm_delete.html"
    success_url = reverse_lazy('admin:papermill:list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())

# -image----------------------------------------------------------------


class CKEDITORBrowserView(BaseCKEDITORBrowserView):
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
