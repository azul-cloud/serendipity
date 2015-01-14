from django import template
from django.core.urlresolvers import resolve, Resolver404

register = template.Library()

@register.simple_tag
def active_page(request, view_name):
    '''
    determine if the page is the active page. Used for adding active to class attribute.
    '''
    if not request:
        return ""
    try:
        if resolve(request.path_info).url_name == view_name:
            return "active" 
        else :
            return ""
    except Resolver404:
        return ""