from django.conf import settings

PAPERMILL_SETTINGS = {
    'multilanguage': False,
    'default_language': 'en',
    'languages': (('en', 'English'),),
    'editor_css': 'admin/css/papermill-editor.css',
    'title_prefix': 'News',
    'paginate_by': 50,
}

PAPERMILL_SETTINGS.update(getattr(settings, 'PAPERMILL_SETTINGS', {}))
