from django import template

register = template.Library()


@register.inclusion_tag('papermill/templatetags/latest_posts_overview.html',
                        takes_context=True)
def latest_posts_overview(context, posts, show_lead=True, count=50):
    """
    Renders latest posts overview
    """

    posts = posts.model.latest.posts(count=count)

    return {
        'posts': posts,
        'show_lead': show_lead,
    }
