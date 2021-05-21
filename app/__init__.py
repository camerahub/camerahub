from iommi import register_factory
from taggit.managers import TaggableManager
from django.contrib.contenttypes.fields import GenericRelation
from collectionfield.models import CollectionField

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
