# -*- coding: utf-8 -*-

from django.utils import timezone
from django.db import models
from django.utils.translation import get_language
from .settings import PAPERMILL_SETTINGS


class LatestPostsManager(models.Manager):
    """
    Returns latest posts querysets
    """
    def posts(self, count=3):
        return self.model.objects.all().filter(
            status=self.model.STATUS_PUBLISHED).order_by('-publish_at')[:count]


class PublishedPostsManager(models.Manager):
    """
    Returns latest published posts
    """
    def get_queryset(self):
        qs = super(PublishedPostsManager, self).get_queryset()
        qs = qs.filter(status__exact=self.model.STATUS_PUBLISHED,
                       publish_at__lte=timezone.now())
        if PAPERMILL_SETTINGS['multilanguage']:
            qs = qs.filter(language=get_language())

        return qs
