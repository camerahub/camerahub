from iommi import register_factory, register_style, Style
from taggit.managers import TaggableManager
from django.contrib.contenttypes.fields import GenericRelation
from collectionfield.models import CollectionField
from iommi.style_bootstrap import bootstrap

register_factory(
    CollectionField,
    shortcut_name = None
)

register_factory(
    TaggableManager,
    shortcut_name = None
)

register_factory(
    GenericRelation,
    shortcut_name = None
)

# Define the CameraHub house style
camerahub = Style(
    bootstrap,
    base_template='base.html',
    #content_block='content'
)
register_style('camerahub', camerahub)
