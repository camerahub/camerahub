from django.contrib import admin

# Register your models here.

from .models import Accessory
admin.site.register(Accessory)

from .models import AccessoryType
admin.site.register(AccessoryType)

from .models import Archive
admin.site.register(Archive)

from .models import ArchiveType
admin.site.register(ArchiveType)

from .models import Battery
admin.site.register(Battery)

from .models import BodyType
admin.site.register(BodyType)

from .models import BulkFilm
admin.site.register(BulkFilm)

from .models import Camera
class CameraInline(admin.TabularInline):
  model = Camera
admin.site.register(Camera)

from .models import CameraModel
class CameraModelInline(admin.TabularInline):
  model = CameraModel
class CameraModelAdmin(admin.ModelAdmin):
  inlines = [
    CameraInline,
  ]
admin.site.register(CameraModel, CameraModelAdmin)

from .models import Condition
admin.site.register(Condition)

from .models import Developer
admin.site.register(Developer)

from .models import Enlarger
admin.site.register(Enlarger)

from .models import FilmStock
admin.site.register(FilmStock)

from .models import Filter
admin.site.register(Filter)

from .models import FilterAdapter
admin.site.register(FilterAdapter)

from .models import Flash
admin.site.register(Flash)

from .models import FlashProtocol
admin.site.register(FlashProtocol)

from .models import FocusType
admin.site.register(FocusType)

from .models import Format
admin.site.register(Format)

from .models import Lens
class LensInline(admin.TabularInline):
  model = Lens
admin.site.register(Lens)

from .models import LensModel
class LensModelAdmin(admin.ModelAdmin):
  inlines = [
    LensInline,
  ]
admin.site.register(LensModel)

from .models import LightMeter
admin.site.register(LightMeter)

from .models import Manufacturer
admin.site.register(Manufacturer)


from .models import MeteringType
admin.site.register(MeteringType)

from .models import Mount
admin.site.register(Mount)

from .models import Movie
admin.site.register(Movie)

from .models import NegativeSize
admin.site.register(NegativeSize)

from .models import Order
admin.site.register(Order)

from .models import PaperStock
admin.site.register(PaperStock)

from .models import Person
admin.site.register(Person)

from .models import Print
class PrintInline(admin.TabularInline):
  model = Print
admin.site.register(Print)

from .models import Process
admin.site.register(Process)

from .models import Projector
admin.site.register(Projector)

from .models import Repair
admin.site.register(Repair)

from .models import Scan
class ScanInline(admin.TabularInline):
  model = Scan
admin.site.register(Scan)

from .models import Negative
class NegativeInline(admin.TabularInline):
  model = Negative
class NegativeAdmin(admin.ModelAdmin):
  inlines = [
    ScanInline,
    PrintInline,
  ]
admin.site.register(Negative, NegativeAdmin)

from .models import Film
class FilmAdmin(admin.ModelAdmin):
  inlines = [
    NegativeInline,
  ]
admin.site.register(Film, FilmAdmin)

from .models import Series
admin.site.register(Series)

from .models import ShutterSpeed
admin.site.register(ShutterSpeed)

from .models import ShutterType
admin.site.register(ShutterType)

from .models import Teleconverter
admin.site.register(Teleconverter)

from .models import Toner
admin.site.register(Toner)