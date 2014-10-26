from django.core.urlresolvers import reverse_lazy


APP_ADMIN_URLS = {
    'url_base': 'nyheter',
    'namespace': 'papermill',
}

APP_ADMIN_MENU = {
    # for the posts section
    'Nyheter': {
        'anchor': 'posts',
        'bgcolor': '#65BD77',
        'icon': 'fa fa-file-text icon',

        'menu': {
            'Oversikt': {
                'url': reverse_lazy(
                    'admin:%s:list' % APP_ADMIN_URLS['namespace']
                ),
                'icon': 'glyphicon glyphicon-th-list',
                'order': 0,
            },
            'Ny post': {
                'url': reverse_lazy(
                    'admin:%s:create' % APP_ADMIN_URLS['namespace']
                ),
                'icon': 'glyphicon glyphicon-plus-sign',
                'order': 1,
            },
            'Artikkelbilder': {
                'url': reverse_lazy(
                    'admin:%s:postimage-list' % APP_ADMIN_URLS['namespace']
                ),
                'icon': 'glyphicon glyphicon-th-list',
                'order': 2,
            },
            'Last opp artikkelbilder': {
                'url': reverse_lazy(
                    'admin:%s:postimage-create' % APP_ADMIN_URLS['namespace']
                ),
                'icon': 'glyphicon glyphicon-picture',
                'order': 3,
            },
        }
    }
}
