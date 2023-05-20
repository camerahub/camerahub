from django.urls import path
from iommi import Table

# Import any models you need from your models.  Here I'm using Album
from schema.models import Manufacturer

urlpatterns = [
    # ...your urls...
    path('manufacturer/', Table(auto__model=Manufacturer).as_view()),
]
