from django.core.urlresolvers import reverse_lazy


APP_ADMIN_URLS = {
    'url_base': 'papermill',
    'namespace': 'papermill',
}

APP_ADMIN_MENU = {
    # for the posts section
    'Poster': {
        'anchor': 'posts',
        'bgcolor': '#65BD77',
        'icon': 'fa fa-file-text icon',

        'menu': {
            'Oversikt': {
                'url': reverse_lazy('admin:papermill:list'),
                'icon': 'glyphicon glyphicon-th-list',
                'order': 0,
            },
            'Ny post': {
                'url': reverse_lazy('admin:papermill:create'),
                'icon': 'glyphicon glyphicon-plus-sign',
                'order': 1,
            },
            'Artikkelbilder': {
                'url': reverse_lazy('admin:papermill:postimage-list'),
                'icon': 'glyphicon glyphicon-th-list',
                'order': 2,
            },
            'Last opp artikkelbilder': {
                'url': reverse_lazy('admin:papermill:postimage-create'),
                'icon': 'glyphicon glyphicon-picture',
                'order': 3,
            },
        }
    }
}
