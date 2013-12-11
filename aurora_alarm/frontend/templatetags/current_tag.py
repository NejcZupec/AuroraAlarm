from django import template
from django.core.urlresolvers import reverse


register = template.Library()

@register.simple_tag
def current(request, name, by_path=False):
    """ Return the string 'current' current request.path is same as name

    This tag is used for top menu in the header.

    Keyword aruguments:
    request  -- Django request object
    name     -- name of the url or the actual path
    by_path  -- True if name contains a url instead of url name
    """

    if by_path:
        path = name
    else:
        path = reverse(name)

    if request.path == path:
        return 'current'

    # Here is a hack for the gallery.
    if request.path[:21] == path:
        return 'current'

    return ''
