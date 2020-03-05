from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(is_safe=True)
def yesnoicon(obj):
    img = '<img src="/static/svg/{}.svg" width="30" height="30" alt="{}">'
    if obj == True:
        return mark_safe(img.format('yes', 'Yes'))
    elif obj == False:
        return mark_safe(img.format('no', 'No'))
    else:
        return None