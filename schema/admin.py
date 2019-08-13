from django.contrib import admin

# Register your models here.

from .models import Manufacturer
admin.site.register(Manufacturer)

from .models import CameraModel
admin.site.register(CameraModel)