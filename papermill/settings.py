from django.conf import settings

PAPERMILL_SETTINGS = {
    'multilanguage': False,
    'default_language': 'en',
    'languages': None,
    'title_prefix': 'News',
    'paginate_by': 50,
}

PAPERMILL_SETTINGS.update(getattr(settings, 'PAPERMILL_SETTINGS', {}))
