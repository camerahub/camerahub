from django.urls import path
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

from iommi import Table
from iommi import register_factory

from taggit.managers import TaggableManager

# Import any models you need from your models.  Here I'm using Album
from schema.models import Manufacturer

from .pages import IndexPage

# Workaround for https://github.com/iommirocks/iommi/issues/339
register_factory(GenericRelation, factory=None)
register_factory(GenericForeignKey, factory=None)
register_factory(TaggableManager, shortcut_name='many_to_many')

urlpatterns = [
    # ...your urls...
    path('manufacturer/', Table(auto__model=Manufacturer).as_view()),
    path('', IndexPage().as_view()),
]
