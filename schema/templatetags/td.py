from django import template
register = template.Library()

@register.inclusion_tag('td.html')
def td(obj):
    #model = get_model_class_from_string(field)

    model = obj.__class__.__name__
    f = model._meta.get_field(obj)
    field = f.name

    return {
        'model': model,
        'field': field
    }
