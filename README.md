PAPERMILL
=========

**NOTE: This is tailored for the twined project structure,
it probably won't work too well without customization on other
project bootstraps.**

Installation:
-------------

    pip install -e git://github.com/twined/papermill.git#egg=papermill-dev


Usage:
------

Add `papermill` to `INSTALLED_APPS` and add this to your urlpatterns:

    # urls
    url(
        r'^posts/', include('papermill.urls', namespace="posts")
    ),

Then add this to your `settings.py`

    # default papermill settings

    PAPERMILL_SETTINGS = {
        'title_prefix': 'News',
        'paginate_by': 50,
    }

Remember to add a `postimage` key to the IMGIN_CONFIG in your `settings.py`:

    # example IMGIN config

    IMGIN_CONFIG = {
        # ...
        'postimage': {
            'allowed_exts': [".jpg", ".png", ".jpeg",
                             ".JPG", ".PNG", ".JPEG"],
            'upload_dir': os.path.join('images', 'posts'),
            'size_limit': 10240000,
            'size_map': {
                'l': {
                    'landscape': '700',
                    'portrait': '700',
                    'dir': 'l',
                    'class_name': 'large',
                    'crop': '',
                    'quality': 90,
                    'format': 'JPEG',
                },
                'm': {
                    'landscape': '310',
                    'portrait': '310',
                    'dir': 'm',
                    'class_name': 'medium',
                    'crop': '',
                    'quality': 90,
                    'format': 'JPEG',
                },
                's': {
                    'landscape': '200',
                    'portrait': '200',
                    'dir': 's',
                    'class_name': 'small',
                    'crop': '',
                    'quality': 90,
                    'format': 'JPEG',
                },
                't': {
                    'landscape': '140x140',
                    'portrait': '140x140',
                    'dir': 't',
                    'class_name': 'thumb',
                    'crop': 'center',
                    'quality': 90,
                    'format': 'JPEG',
                },
            },
        },
    }

Overridable templates:

    /papermill/list.html
    /papermill/detail.html
    /papermill/templatetags/latest_posts_overview.html

Object name is `posts` and `post`.

Template tags
-------------
`latest_posts_overview`
    {% load posts_tags %}
    {% latest_posts_overview show_lead=True %}
