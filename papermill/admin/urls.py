from django.conf.urls import patterns, url

from papermill.admin.views import (
    CreatePostView, ListPostView, UpdatePostView, DeletePostView,
    AddPostImageView, UploadPostImageView, ListPostImageView,
    AJAXDeletePostImageView, CKEDITORBrowserView, ViewPostView
)

urlpatterns = patterns(
    'papermill.admin.views',
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
        r'^endre/(?P<pk>\d+)/$',
        UpdatePostView.as_view(),
        name="update"),
    url(
        r'^slett/(?P<pk>\d+)/$',
        DeletePostView.as_view(),
        name="delete"),
    url(
        r'^ny/check-slug/$',
        'checkslug',
        name="create-checkslug"),

    url(
        r'^(ny|endre)/get-keywords/$',
        'get_keywords',
        name="get-keywords"),
    url(
        r'^(ny|endre)/(.*)/get-keywords/$',
        'get_keywords',
        name="get-keywords"),

    # postimages
    url(
        r'^imgs/browser/$',
        CKEDITORBrowserView.as_view(),
        name="browser"),
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
