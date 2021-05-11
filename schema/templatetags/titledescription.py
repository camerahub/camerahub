from django import template
from etc.templatetags.model_field import FieldAttrNode, _get_model_field_attr

register = template.Library()

@register.tag
def titledescription(parser, token):
    tag_name = 'titledescription'

    tokens = token.split_contents()
    tokens_num = len(tokens)

    if tokens_num not in (3, 5):
        raise template.TemplateSyntaxError(
            '`%(tag_name)s` tag requires two or four arguments. '
            'E.g.: {%% %(tag_name)s from model.field %%} or {%% %(tag_name)s from model.field as myvar %%}.'
            % {'tag_name': tag_name}
        )

    field = tokens[2]
    as_var = None

    tokens = tokens[3:]
    if len(tokens) >= 2 and tokens[-2] == 'as':
        as_var = tokens[-1]

    # FieldAttrNode(field, attr_name, tag_name, as_var)
    verbose_name = FieldAttrNode(field, 'verbose_name', 'td') #, as_var)
    help_text = FieldAttrNode(field, 'help_text', 'td') #, as_var)

    return "{}<br><small class=\"text-muted\">{}</small>".format(verbose_name, help_text)



@register.tag
def mytag(parser, token):
    return FieldAttrNode(
        field=f'{token.split_contents()[1]}.elements',
        attr_name='help_text',
        tag_name='mytag'
    )



@register.inclusion_tag('td2.html')
def mytag2(parser, token):
    help_text = FieldAttrNode(
        field=f'{token.split_contents()[1]}.elements',
        attr_name='help_text',
        tag_name='mytag'
    )
    verbose_name = FieldAttrNode(
        field=f'{token.split_contents()[1]}.elements',
        attr_name='verbose_name',
        tag_name='mytag2'
    )
    return {
        'help_text': str(help_text),
        'verbose_name': str(verbose_name),
    }


@register.tag
def mytag3(parser, token):
    help_text = FieldAttrNode(
        field=f'{token.split_contents()[1]}.elements',
        attr_name='help_text',
        tag_name='mytag'
    )
    verbose_name = FieldAttrNode(
        field=f'{token.split_contents()[1]}.elements',
        attr_name='verbose_name',
        tag_name='mytag2'
    )
    return str("{}<br><small class=\"text-muted\">{}</small>".format(verbose_name, help_text))



@register.tag
def mytag4(parser, token):
    verbose_name = _get_model_field_attr('model_field_verbose_name', 'verbose_name', token)
    help_text = _get_model_field_attr('model_field_help_text', 'help_text', token)
    return "{}<br><small class=\"text-muted\">{}</small>".format(verbose_name, help_text)

@register.simple_tag
def mytag5(obj):
#    verbose_name = _get_model_field_attr('model_field_verbose_name', 'verbose_name', obj)
#    help_text = _get_model_field_attr('model_field_help_text', 'help_text', obj)
    verbose_name = getattr(obj.__class__._meta, 'verbose_name')
    help_text = getattr(obj.__class__._meta, 'help_text')
    return "{}<br><small class=\"text-muted\">{}</small>".format(verbose_name, help_text)
