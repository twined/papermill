import os
import uuid
from django.db import models
from papermill.models import BasePost, BasePostImage


def handle_profile_upload(instance, filename):
    _, ext = os.path.splitext(filename)
    return os.path.join(
        'images', 'news_featured_image',
        '%s%s' % (uuid.uuid4(), ext.lower()))


class Post(BasePost):
    featured_image = models.ImageField(upload_to=handle_profile_upload,
                                       blank=True, null=True)

    class Meta:
        ordering = ('featured', '-created',)


class PostImage(BasePostImage):
    pass
