# -*- coding: utf-8 -*-

from crispy_forms.layout import (Div, Field)
from papermill.forms import BasePostForm

from .models import Post


class PostForm(BasePostForm):
    '''
    Extends base post form with a `featured_image` ImageField
    '''

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.helper.layout[1][0].extend([
            Div(
                Field(
                    'featured_image',
                ),
                css_class="col-md-12",
            ),
        ])

    class Meta:
        model = Post
        exclude = ('user',)
