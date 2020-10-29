from math import degrees
from itertools import chain
from django.utils.safestring import mark_safe
from numpy import arctan


def boolicon(obj):
    img = '<img src="/static/svg/{}.svg" width="30" height="30" alt="{}">'
    if obj is not None:
        if bool(obj):
            return_value = mark_safe(img.format('yes', 'Yes'))
        else:
            return_value = mark_safe(img.format('no', 'No'))
    else:
        return_value = None

    return return_value


def colouricon(obj):
    img = '<img src="/static/svg/{}.svg" width="30" height="30" alt="{}">'
    if obj is not None:
        if bool(obj):
            return_value = mark_safe(img.format('colour', 'Colour'))
        else:
            return_value = mark_safe(img.format('bw', 'Black & White'))
    else:
        return_value = None

    return return_value


def angle_of_view(diag, focal):
    # fov = 2 arctan (d / 2f)
    if diag is not None and focal is not None:
        angle = round(degrees(2 * arctan(float(diag) / (2*float(focal)))))
    else:
        angle = None
    return angle


def to_dict(instance):
    opts = instance._meta
    data = {}
    for field in chain(opts.concrete_fields, opts.private_fields):
        data[field.name] = field.value_from_object(instance)
    for field in opts.many_to_many:
        data[field.name] = [i.id for i in field.value_from_object(instance)]
    return data
