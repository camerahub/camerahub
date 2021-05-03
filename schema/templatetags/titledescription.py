from django import template
from etc.templatetags.model_field import FieldAttrNode

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
