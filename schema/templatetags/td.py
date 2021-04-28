from django import template
from etc.toolbox import get_model_class_from_string

register = template.Library()

@register.inclusion_tag('td2.html')
def td(obj):
    #field = obj.__class__.__name__
    #model = get_model_class_from_string('schema.'+field)
    #model = type(obj)
    
    #model = obj.__class__
    #print ('obj:' + obj.__name__)
    #print ('model:' + model)
    
    #model = obj.__class__.__name__
    #f = model._meta.get_field(obj)
    #field = f

    #f = model._meta.get_field(obj.__field__)
    #field = f.name

    #help_text = obj.help_text

    #field = obj.__class__.__name__
    #help = obj.__class__.help_text
    
    #title = getattr(obj, 'class')
    #title = obj

    # this works
    model = str(obj.__class__.__name__)
    #help_text = getattr(obj.__class__._meta, 'help_text', '')


    #var_field = template.Variable(self.field)
    obj2 = template.Variable(obj)
    var_model = obj2.lookups[0]
    field_name = obj2.lookups[1]


    return {
        'model': str(var_model),
        'field': str(var_field),
    #    'instance': instance,
    #    'obj': obj
    }
