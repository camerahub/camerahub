from math import degrees
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
