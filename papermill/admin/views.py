# posts.py

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect

from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView

from cerebrum.mixins import LoginRequiredMixin, DispatchProtectionMixin
from cerebrum.utils import json_response


from ..models import BasePost
from ..models import BasePostImage

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


class BaseListPostView(LoginRequiredMixin, ListView):
    model = BasePost
    context_object_name = "posts"
    template_name = "papermill/admin/list.html"

    def get_queryset(self):
        return self.model.objects.order_by('status', '-pk')


class BaseViewPostView(LoginRequiredMixin, DetailView):
    model = BasePost
    template_name = "papermill/admin/detail.html"


class BaseCreatePostView(DispatchProtectionMixin,
                         LoginRequiredMixin, CreateView):
    '''
    Base view for creating new posts. Make sure to add CSRF for the
    image upload portion.
    '''
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


class BaseUpdatePostView(DispatchProtectionMixin,
                         LoginRequiredMixin, UpdateView):
    '''
    Base view for updating posts. Make sure to add CSRF for the
    image upload portion.
    '''
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
