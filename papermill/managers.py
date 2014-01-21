# -*- coding: utf-8 -*-

from datetime import datetime
from django.db import models


class LatestPostsManager(models.Manager):
    """
    Returns latests posts querysets
    """
    def posts(self, count=3):
        return self.model.objects.all().filter(
            status=self.model.PS_PUBLISHED).order_by('-publish_at')[:count]


class PublishedPostsManager(models.Manager):
    """
    Returns latest published posts
    """
    def get_query_set(self):
        qs = super(PublishedPostsManager, self).get_query_set()
        return qs.filter(status__exact=self.model.PS_PUBLISHED,
                         publish_at__lte=datetime.now())
