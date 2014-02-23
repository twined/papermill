# -*- coding: utf-8 -*-

"""
// PAPERMILL
// model definitions for the papermill app
// http://github.com/twined/papermill
// (c) Twined/Univers 2009-2014. All rights reserved.
"""

from datetime import datetime

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify

import imgin.settings
from imgin.models import BaseImage

from taggit.managers import TaggableManager

from .managers import LatestPostsManager, PublishedPostsManager


class Post(models.Model):
    """
    Post model
    """
    PS_DRAFT = 0
    PS_WAITING = 1
    PS_PUBLISHED = 2
    PS_DELETED = 3

    POST_STATUS_TYPES = (
        (PS_DRAFT, 'Kladd'),
        (PS_WAITING, 'Venter'),
        (PS_PUBLISHED, 'Publisert'),
        (PS_DELETED, 'Slettet'),
    )

    language = models.CharField(max_length=10, blank=True)
    header = models.CharField(
        max_length=255, null=False, blank=False,
        verbose_name='Overskrift')
    slug = models.CharField(max_length=255, verbose_name="URL")
    lead = models.TextField(verbose_name='Ingress', blank=True)
    body = models.TextField(verbose_name="Brødtekst", blank=True)
    user = models.ForeignKey(User, verbose_name="Bruker")
    status = models.IntegerField(
        choices=POST_STATUS_TYPES, default=0, verbose_name='Status')
    featured = models.BooleanField(
        verbose_name="Vektlagt",
        help_text="Vektlagte poster vises alltid øverst",
        default=False)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Opprettet")
    updated = models.DateTimeField(auto_now=True, verbose_name="Endret")
    publish_at = models.DateTimeField(
        default=datetime.now, verbose_name='Publiseringstidspunkt')
    published = models.DateTimeField(
        null=True, blank=True, editable=False,
        verbose_name='Publisert')
    tweeted = models.BooleanField(
        null=False, blank=False, default=False, editable=False)
    meta_keywords = models.CharField(
        max_length=255,
        null=True,
        verbose_name="Nøkkelord til søkemotorer")
    meta_description = models.CharField(
        max_length=255,
        null=True,
        verbose_name="Beskrivelse til søkemotorer")

    objects = models.Manager()
    latest = LatestPostsManager()
    published = PublishedPostsManager()
    tags = TaggableManager(blank=True)

    @property
    def status_class(self):
        """
        Returns post's current status for use as css class
        """
        return self.POST_STATUS_TYPES[self.status][1]

    def get_absolute_url(self):
        kwargs_dict = {
            "slug": self.slug,
            "year": self.created.year,
            "month": self.created.month,
            "day": self.created.day,
        }
        return reverse('posts:detail', kwargs=kwargs_dict)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.header)
        super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.header

    class Meta:
        ordering = ('featured', '-created',)

# connect signals
from django.db.models.signals import post_save, post_delete
from .cache import invalidate_cache
post_save.connect(
    invalidate_cache, sender=Post,
    dispatch_uid="Post.post_save.invalidate"
)
post_delete.connect(
    invalidate_cache, sender=Post,
    dispatch_uid="Post.post_delete.invalidate"
)


class PostCategory(models.Model):
    """
    PostCategory model
    """
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User)
    created = models.DateTimeField(
        default=datetime.now, editable=False)
    modified = models.DateTimeField(
        default=datetime.now, editable=False)


class PostImage(BaseImage):
    """
    Models an image for upload and use through post object.
    Needs IMGIN
    """
    IMGIN_KEY = 'postimage'
    IMGIN_CFG = imgin.settings.IMGIN_CONFIG[IMGIN_KEY]

    @staticmethod
    def get_create_url(*args, **kwargs):
        return reverse(
            'admin:papermill:postimage-create'
        )

    def get_delete_url():
        return reverse(
            'admin:papermill:postimage-delete'
        )

    @staticmethod
    def get_upload_url(*args, **kwargs):
        return reverse(
            'admin:papermill:postimage-upload'
        )

    @staticmethod
    def get_list_url(*args, **kwargs):
        return reverse(
            'admin:papermill:postimage-list'
        )

    class Meta:
        verbose_name = 'Postbilde'
        verbose_name_plural = 'Postbilder'

# connect signals
from django.db.models.signals import post_save, post_delete
from .cache import invalidate_cache
post_save.connect(
    invalidate_cache, sender=PostImage,
    dispatch_uid="PostImage.post_save.invalidate"
)
post_delete.connect(
    invalidate_cache, sender=PostImage,
    dispatch_uid="PostImage.post_delete.invalidate"
)
