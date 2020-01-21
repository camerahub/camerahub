from django import template
import camerahub
register = template.Library()

@register.simple_tag
def camerahub_version():
    return camerahub.__version__
