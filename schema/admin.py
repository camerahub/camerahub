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
admin.site.register(Camera)

from .models import CameraModel
admin.site.register(CameraModel)

from .models import Condition
admin.site.register(Condition)

from .models import Developer
admin.site.register(Developer)

from .models import Enlarger
admin.site.register(Enlarger)

from .models import Film
admin.site.register(Film)

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
admin.site.register(Lens)

from .models import LensModel
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

from .models import Negative
admin.site.register(Negative)

from .models import NegativeSize
admin.site.register(NegativeSize)

from .models import Order
admin.site.register(Order)

from .models import PaperStock
admin.site.register(PaperStock)

from .models import Person
admin.site.register(Person)

from .models import Print
admin.site.register(Print)

from .models import Process
admin.site.register(Process)

from .models import Projector
admin.site.register(Projector)

from .models import Repair
admin.site.register(Repair)

from .models import Scan
admin.site.register(Scan)

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