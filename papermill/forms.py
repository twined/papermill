# -*- coding: utf-8 -*-

import datetime

from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (Layout, Submit,
                                 Div, HTML, Field)

from taggit.forms import TagField
from cerebrum.fields import SlugField
from cerebrum.fields import StatusField

from .models import BasePost
from .settings import PAPERMILL_SETTINGS


class BasePostForm(forms.ModelForm):
    tags = TagField(
        label="Tags",
        required=False,
    )
    slug = forms.CharField(
        label="URL",
        required=True,
    )
    status = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect(), choices=BasePost.POST_STATUS_TYPES,
        initial='0'
    )
    language = forms.ChoiceField(
        label="Språk",
        required=True,
        choices=PAPERMILL_SETTINGS['languages'],
        initial=PAPERMILL_SETTINGS['default_language'],
    )
    meta_keywords = forms.CharField(
        label='META nøkkelord til søkemotorer',
        required=False,
        widget=forms.Textarea(attrs={'rows': 3})
    )
    meta_description = forms.CharField(
        label='META beskrivelse til søkemotorer',
        required=False,
        widget=forms.Textarea(attrs={'rows': 3})
    )
    publish_at = forms.DateTimeField(
        label='Publiseringstidspunkt',
        input_formats=['%d/%m/%Y %H:%M'],
        initial=datetime.datetime.now,
        widget=forms.DateTimeInput(format='%d/%m/%Y %H:%M')
    )

    def __init__(self, *args, **kwargs):
        #  Field.template = 'bootstrap/custom_field.html'
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                # 2
                Div(  # span7
                    Field('language'),
                    Field('header'),
                    SlugField('slug'),
                    Field(
                        'lead',
                        style="height: 100px;"
                    ),
                    Div(  # row
                        Div(  # md-12
                            Field(
                                'body',
                            ),
                            css_class="col-md-12",
                        ),
                        css_class="row",
                    ),
                    Div(  # row
                        Div(  # span7
                            Field(
                                'tags',
                            ),
                            css_class='col-md-10',
                        ),
                        Div(  # span2
                            Field(
                                'publish_at'
                            ),
                            css_class='col-md-2',
                        ),
                        css_class='row'
                    ),
                    css_class='col-md-10'
                ),
                # Right column
                Div(
                    StatusField('status'),
                    Field('featured'),
                    css_class='col-md-2 well',
                ),
                css_class="row",
            ),

        )
        self.helper.add_input(
            Submit('submit', 'Lagre', css_class="btn btn-primary"))

        super(BasePostForm, self).__init__(*args, **kwargs)

    class Meta:
        model = BasePost
        exclude = ('user',)
