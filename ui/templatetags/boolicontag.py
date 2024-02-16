from django import template
from schema.funcs import boolicon

register = template.Library()

@register.filter(is_safe=True)
def boolicontag(obj):
    return boolicon(obj)
