from django.urls import path
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

from iommi import Form
from iommi import register_factory
from iommi.path import register_path_decoding

from taggit.managers import TaggableManager

# Import any models you need from your models.  Here I'm using Album
from schema.models import Manufacturer

from ui.pages import IndexPage
from ui.tables import ManufacturerListPage
from ui.detail import ManufacturerPage

# Workaround for https://github.com/iommirocks/iommi/issues/339
register_factory(GenericRelation, factory=None)
register_factory(GenericForeignKey, factory=None)
register_factory(TaggableManager, shortcut_name='many_to_many')

register_path_decoding(
    manufacturer=Manufacturer.slug,
)

urlpatterns = [
    # ...your urls...
    path('manufacturer/', ManufacturerListPage().as_view()),
    path('manufacturer/create/', Form.create(auto__model=Manufacturer).as_view()),
    path('manufacturer/edit/', Form.edit(auto__model=Manufacturer).as_view()),
    path('manufacturer/<manufacturer>/', ManufacturerPage().as_view()),





    path('', IndexPage().as_view()),
]
