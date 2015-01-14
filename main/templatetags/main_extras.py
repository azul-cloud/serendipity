from django import template

register = template.Library()

@register.simple_tag
def active_page(request, view_name):
    '''
    determine if the page is the active page. Used for adding active to class attribute.
    '''
    from django.core.urlresolvers import resolve, Resolver404
    if not request:
        return "not request"
    try:
        if resolve(request.path_info).url_name == view_name:
            return "active" 
        else :
            return ""
    except Resolver404:
        return "not active"