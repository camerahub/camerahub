from django.urls import path
from iommi import Form

# Import any models you need from your models.  Here I'm using Album
from schema.models import Manufacturer

urlpatterns = [
    # ...your urls...
    path('manufacturer/', Form.create(auto__model=Manufacturer).as_view()),
]
