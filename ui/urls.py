from django.urls import path
from iommi import Form, Table
from schema import models

urlpatterns = [
    path('battery/create/', Form.create(auto__model=models.Battery).as_view()),
    path('battery/', Table(auto__model=models.Battery).as_view()),

    #path('manufacturer/create/', Form.create(auto__model=models.Manufacturer).as_view()),
    #path('manufacturer/', Table(auto__model=models.Manufacturer).as_view()),
]
