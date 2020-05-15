from django.utils.safestring import mark_safe


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
