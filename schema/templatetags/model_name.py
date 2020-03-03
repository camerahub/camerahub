from django import template
register = template.Library()

@register.filter
def verbose_name(obj):
    return obj._meta.verbose_name

@register.filter
def verbose_name_plural(obj):
    return obj._meta.verbose_name_plural

@register.filter
def model_name(obj):
    return obj._meta.model_name

@register.filter
def model_list(obj):
    return obj._meta.model_name + '-list'

@register.filter
def model_add(obj):
    return obj._meta.model_name + '-create'