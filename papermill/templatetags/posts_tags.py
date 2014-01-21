from django import template

from posts.models import Post

register = template.Library()


@register.inclusion_tag('papermill/templatetags/latest_posts_overview.html',
                        takes_context=True)
def latest_posts_overview(context):
    """
    Renders latest posts overview
    """

    posts = Post.latest.posts()

    return {
        'posts': posts,
    }
