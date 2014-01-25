# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------
# Context processors for the Papermill app
# Provides {{ admin }} dictionary in all templates.
# (c) Twined/Univers 2009-2014. All rights reserved.
# ----------------------------------------------------------------------

import datetime

from .settings import PAPERMILL_SETTINGS


def config(request):

    cfg = PAPERMILL_SETTINGS
    return {'papermill_settings': cfg}


def date_now(request):
    return {'date_now': datetime.datetime.now()}
