from django.conf.urls import patterns, url

from papermill.admin.views import AJAXAutoCompleteTagsView

from .views import (
    CreatePostView, ListPostView, UpdatePostView,
    DeletePostView, ViewPostView,
)
from .views import (
    AddPostImageView, UploadPostImageView, ListPostImageView,
    AJAXCheckSlugView,
    AJAXDeletePostImageView, AJAXFroalaBrowserView, AJAXFroalaUploadView
)


urlpatterns = patterns(
    'news.admin.views',
    url(
        r'^$',
        ListPostView.as_view(),
        name="list"),
    url(
        r'^vis/(?P<pk>\d+)/$',
        ViewPostView.as_view(),
        name="view"),
    url(
        r'^ny/$',
        CreatePostView.as_view(),
        name="create"),
    url(
        r'^ny/autocomplete-tags/$',
        AJAXAutoCompleteTagsView.as_view(),
        name="autocomplete-tags"),
    url(
        r'^endre/(?P<pk>\d+)/$',
        UpdatePostView.as_view(),
        name="update"),
    url(
        r'^endre/(?P<pk>\d+)/autocomplete-tags/$',
        AJAXAutoCompleteTagsView.as_view(),
        name="autocomplete-tags"),
    url(
        r'^slett/(?P<pk>\d+)/$',
        DeletePostView.as_view(),
        name="delete"),
    url(
        r'^ny/check-slug/$',
        AJAXCheckSlugView.as_view(),
        name="create-checkslug"),
    url(
        r'^endre/(?P<pk>\d+)/check-slug/$',
        AJAXCheckSlugView.as_view(),
        name="edit-checkslug"),

    url(
        r'^(ny|endre)/get-keywords/$',
        'get_keywords',
        name="get-keywords"),
    url(
        r'^(ny|endre)/(.*)/get-keywords/$',
        'get_keywords',
        name="get-keywords"),

    # postimages
    # ----------
    # returns a json object of images to the froala browser
    url(
        r'^imgs/browser/$',
        AJAXFroalaBrowserView.as_view(),
        name="browser"),
    # uploads image to froala, returns the image as json
    url(
        r'^imgs/froala-upload/$',
        AJAXFroalaUploadView.as_view(),
        name="postimage-froala-upload"),
    url(
        r'^imgs/ny/$',
        AddPostImageView.as_view(),
        name="postimage-create"),
    url(
        r'^imgs/ny/upload/$',
        UploadPostImageView.as_view(),
        name="postimage-upload"),
    url(
        r'^imgs/oversikt/$',
        ListPostImageView.as_view(),
        name="postimage-list"),
    url(
        r'^imgs/oversikt/slett/$',
        AJAXDeletePostImageView.as_view(),
        name="postimage-delete"),
)
