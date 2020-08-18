from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(is_safe=True)
def aperture(obj):
    newstr = mark_safe(obj.replace('f/', '<em>f</em>/'))
    return newstr


@register.filter(is_safe=True)
def shutter(obj):
    mystr = str(obj)
    newstr = mark_safe(mystr.replace('1/', '&sup1;/'))
    return newstr
