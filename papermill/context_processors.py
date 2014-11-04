# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------
# Context processors for the Papermill app
# Provides {{ admin }} dictionary in all templates.
# (c) Twined/Univers 2009-2014. All rights reserved.
# ----------------------------------------------------------------------

from .settings import PAPERMILL_SETTINGS


def config(request):
    cfg = PAPERMILL_SETTINGS
    return {'papermill_settings': cfg}
