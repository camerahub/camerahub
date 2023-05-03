from datetime import date
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(is_safe=True)
def aperture(obj):
    if obj:
        newstr = mark_safe(obj.replace('f/', '<em>f</em>/'))
        return newstr


@register.filter(is_safe=True)
def shutter(obj):
    if obj:
        mystr = str(obj)
        newstr = mark_safe(mystr.replace('1/', '&sup1;/'))
        return newstr

@register.filter(is_safe=True)
def sign(obj):
    if type(obj) == int or type(obj) == float:
        if obj > 0:
            mystr = '+' + str(obj)
        elif obj == 0:
            mystr = '&plusmn;' + str(obj)
        else:
            mystr = str(obj)
    else:
        mystr = obj
    return mark_safe(mystr)

@register.filter(is_safe=True)
def yearssince(obj):
    currentyear = date.today().year
    diff = int(currentyear) - int(obj)
    return f"{diff} years ago"
