# posts.py

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import (
    CreateView, ListView, UpdateView, DeleteView, DetailView, View
)

from taggit.models import Tag
from cerebrum.views import LoginRequiredMixin
from cerebrum.utils import json_response
from imgin.views import (
    BaseImageCreateView, AJAXBaseImageHandleUploadView,
    AJAXBaseImageDeleteView, BaseImageListView
)

from ..models import (
    BasePost, BasePostImage
)
from ..forms import BasePostForm


@login_required
def get_keywords(request, *args, **kwargs):
    keywords = request.GET['text']
    return json_response({
        'keywords': keywords,
    })


@login_required
def tweet(request, pk):
    #  post_to_twitter(request, Post.objects.get(pk=pk))
    #  return redirect(reverse('admin:papermill:list'))
    pass


class BaseAJAXCheckSlugView(LoginRequiredMixin, View):
    """
    Checks given slug against the database
    """
    model = BasePost

    def get(self, request, *args, **kwargs):
        if 'slug' not in request.GET:
            # slug wasn't passed.
            return json_response({
                'status': 400,
                'error_msg': 'No slug passed to pages::checkslug'
            })

        slug = request.GET['slug'].lower()

        if 'pk' in self.kwargs:
            # it's an edit. it's ok if it's the same as before
            obj = self.model.objects.get(pk=self.kwargs['pk'])
            if obj.slug == slug:
                return json_response({
                    'status': 200,
                })

        if self.model.objects.all().filter(slug=slug):
            return json_response({
                'status': 300,
                'error_msg': 'Overskriften eksisterer allerede'
            })

        return json_response({
            'status': 200,
        })


class BaseListPostView(LoginRequiredMixin, ListView):
    model = BasePost
    context_object_name = "posts"
    template_name = "papermill/admin/list.html"

    def get_queryset(self):
        return self.model.objects.order_by('status', '-pk')


class BaseViewPostView(LoginRequiredMixin, DetailView):
    model = BasePost
    template_name = "papermill/admin/detail.html"


class BaseCreatePostView(LoginRequiredMixin, CreateView):
    form_class = BasePostForm
    template_name = "papermill/admin/form.html"
    success_url = reverse_lazy('admin:papermill:list')

    def form_valid(self, form):

        self.object = form.save(commit=False)
        self.object.user = self.request.user

        messages.success(self.request, "Innlegget er lagret", extra_tags='msg')
        return super(BaseCreatePostView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Rett feilene under")
        return super(BaseCreatePostView, self).form_invalid(form)


class BaseUpdatePostView(LoginRequiredMixin, UpdateView):
    model = BasePost
    form_class = BasePostForm
    template_name = "papermill/admin/form.html"
    success_url = reverse_lazy('admin:papermill:list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        messages.success(self.request, "Endringen var vellykket.",
                         extra_tags='msg')
        return super(BaseUpdatePostView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Rett feilene under")
        return super(BaseUpdatePostView, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(BaseUpdatePostView, self).get_context_data(**kwargs)
        context['body'] = self.object.body
        return context


class BaseDeletePostView(LoginRequiredMixin, DeleteView):
    model = BasePost
    template_name = "papermill/admin/post_confirm_delete.html"
    success_url = reverse_lazy('admin:papermill:list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())


class AJAXAutoCompleteTagsView(View):
    """
    AJAX: Returns tags
    """
    def get(self, request, *args, **kwargs):
        try:
            tags = Tag.objects.filter(
                name__istartswith=request.GET['query']
            ).values_list('name', flat=True)
        except MultiValueDictKeyError:
            tags = []

        return json_response({'suggestions': list(tags)})
