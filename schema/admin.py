from django.contrib import admin

# The text to put at the top of each admin page, as an <h1> (a string). By default, this is “Django administration”.
admin.site.site_header = 'PhotoDB'

# The text to put at the end of each admin page’s <title> (a string). By default, this is “Django site admin”.
admin.site.site_title = 'PhotoDB'

# The text to put at the top of the admin index page (a string). By default, this is “Site administration”.
admin.site.index_title = 'PhotoDB'

# The URL for the “View site” link at the top of each admin page. By default, site_url is /. Set it to None to remove the link.
admin.site.site_url = None

# Register your models here.

from .models import Accessory
class AccessoryAdmin(admin.ModelAdmin):
  filter_horizontal = ('camera_model_compatibility', 'lens_model_compatibility')
admin.site.register(Accessory, AccessoryAdmin)

from .models import Archive
admin.site.register(Archive)

from .models import Battery
admin.site.register(Battery)

from .models import BulkFilm
admin.site.register(BulkFilm)

from .models import Camera
class CameraInline(admin.TabularInline):
  model = Camera
  extra = 0
admin.site.register(Camera)

from .models import CameraModel
class CameraModelInline(admin.TabularInline):
  model = CameraModel
  extra = 0
class CameraModelAdmin(admin.ModelAdmin):
  fieldsets = (
    (None, {
      'fields': ('manufacturer', 'model', 'mount', 'format', 'body_type', 'weight', ('introduced', 'discontinued'), 'negative_size', 'cable_release', 'viewfinder_coverage', ('power_drive', 'continuous_fps'), 'video', 'digital', 'fixed_mount', 'lensmodel', ('battery_qty', 'battery_type'), 'notes', 'tripod', 'series'),
      'description': 'Enter information about this camera model',
    }),
    ('Metering', {
      'fields': ('metering', 'metering_type', 'coupled_metering', ('min_iso', 'max_iso'), ('meter_min_ev', 'meter_max_ev'), 'metering_modes', 'exposure_programs')
    }),
    ('Flash', {
      'fields': ('int_flash', 'int_flash_gn', 'ext_flash', 'flash_metering', 'pc_sync', 'hotshoe', 'coldshoe')
    }),
    ('Focus', {
      'fields': ('focus_type', 'af_points', 'dof_preview')
    }),
    ('Shutter', {
      'fields': ('shutter_type', 'shutter_model', 'shutter_speeds', 'bulb', 'time'),
    }),
  )
  inlines = [
    CameraInline,
  ]
  filter_horizontal = ('metering_modes', 'exposure_programs', 'series', 'shutter_speeds')
  search_fields = ['manufacturer__name', 'model', 'notes']
  list_display = ('__str__', 'mount', 'format', 'body_type', 'introduced')
  list_filter = ('manufacturer__name', 'mount', 'format', 'body_type', 'series')
admin.site.register(CameraModel, CameraModelAdmin)

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

from .models import Format
admin.site.register(Format)

from .models import Lens
class LensInline(admin.TabularInline):
  model = Lens
  extra = 0
admin.site.register(Lens)

from .models import LensModel
class LensModelAdmin(admin.ModelAdmin):
  fieldsets = (
    (None, {
      'fields': ('manufacturer', 'model', 'fixed_mount', 'mount'),
      'description': 'Enter information about this camera model',
    }),
    ('Optics', {
      'fields': ('zoom', ('min_focal_length', 'max_focal_length'), 'closest_focus', ('max_aperture', 'min_aperture'), ('elements', 'groups'), ('nominal_min_angle_diag', 'nominal_max_angle_diag'), 'magnification'),
    }),
    ('Physical', {
      'fields': ('length', 'diameter', 'weight'),
    }),
    ('Other', {
      'fields': ('aperture_blades', 'autofocus', 'filter_thread', 'url', 'introduced', 'discontinued', 'negative_size', 'notes', 'coating', 'hood', 'exif_lenstype', 'rectilinear', 'image_circle', 'formula', 'shutter_model', 'series'),
    })
  )
  inlines = [
    LensInline,
  ]
  filter_horizontal = ('series',)
  search_fields = ['manufacturer__name', 'model', 'notes']
  list_display = ('__str__', 'mount', 'min_focal_length', 'max_aperture', 'introduced')
  list_filter = ('manufacturer__name', 'mount')
admin.site.register(LensModel, LensModelAdmin)

from .models import LightMeter
admin.site.register(LightMeter)

from .models import Manufacturer
admin.site.register(Manufacturer)


from .models import MeteringType
admin.site.register(MeteringType)

from .models import Mount
admin.site.register(Mount)

from .models import MountAdapter
admin.site.register(MountAdapter)

from .models import Movie
admin.site.register(Movie)

from .models import NegativeSize
class NegativeSizeAdmin(admin.ModelAdmin):
  readonly_fields = ('area', 'crop_factor', 'aspect_ratio')
admin.site.register(NegativeSize, NegativeSizeAdmin)

from .models import Order
admin.site.register(Order)

from .models import PaperStock
admin.site.register(PaperStock)

from .models import Person
admin.site.register(Person)

from .models import Print
from .models import Toning
class ToningInline(admin.TabularInline):
  model = Print.toner.through
  verbose_name = "toner"
  verbose_name_plural = "toners"
  extra = 0

class PrintInline(admin.TabularInline):
  model = Print
  extra = 0
class PrintAdmin(admin.ModelAdmin):
  fieldsets = (
    (None, {
      'fields': ('negative', 'date', 'notes', 'own', 'location', 'sold_price', 'fine', 'archive', 'printer', ),
    }),
    ('Paper', {
      'fields': ('paper_stock', 'height', 'width', ),
    }),
    ('Exposure', {
      'fields': ('aperture', 'exposure_time', 'filtration_grade', 'enlarger', 'lens',),
    }),
    ('Development', {
      'fields': ('developer', 'development_time',),
    }),
  )
  inlines = [
    ToningInline,
  ]
  search_fields = ['negative__caption', 'notes']
  list_display = ('__str__', 'date', 'negative')
  list_filter = ('paper_stock', 'developer', 'fine')
admin.site.register(Print, PrintAdmin)

from .models import Process
admin.site.register(Process)

from .models import Projector
admin.site.register(Projector)

from .models import Repair
admin.site.register(Repair)

from .models import Scan
class ScanInline(admin.TabularInline):
  model = Scan
  extra = 0
admin.site.register(Scan)

from .models import Negative
class NegativeInline(admin.TabularInline):
  model = Negative
  extra = 0
class NegativeAdmin(admin.ModelAdmin):
  fieldsets = (
    (None, {
      'fields': (('film', 'frame'), 'caption', 'date', 'notes', 'photographer'),
      'description': 'Enter information about this camera model',
    }),
    ('Exposure', {
      'fields': ('lens', 'mount_adapter', 'shutter_speed', 'aperture', 'filter', 'teleconverter', 'focal_length', 'flash', 'metering_mode', 'exposure_program', 'copy_of'),
    }),
    ('Location', {
      'fields': (('latitude', 'longitude'),),
    }),
  )
  search_fields = ['caption', 'notes']
  list_display = ('__str__', 'caption', 'date',)
  list_filter = ('film', 'photographer')
  inlines = [
    ScanInline,
    PrintInline,
  ]
admin.site.register(Negative, NegativeAdmin)

from .models import Film
class FilmAdmin(admin.ModelAdmin):
  fieldsets = (
    (None, {
      'fields': ('format', 'title', 'filmstock', 'film_batch', 'expiry_date', 'purchase_date', 'price', 'frames'),
    }),
    ('Bulk film', {
      'fields': ('bulk_film', 'bulk_film_loaded'),
    }),
    ('Exposure', {
      'fields': ('exposed_at', 'camera', 'date_loaded'),
    }),
    ('Development', {
      'fields': ('developer', 'dev_uses', 'dev_time', 'dev_temp', 'dev_n', 'development_notes', 'processed_by', 'date_processed'),
    }),
    ('Archive', {
      'fields': ('directory', 'archive'),
    })
  )
  inlines = [
    NegativeInline,
  ]
admin.site.register(Film, FilmAdmin)

from .models import Series
admin.site.register(Series)

from .models import ShutterSpeed
class ShutterSpeedAdmin(admin.ModelAdmin):
  readonly_fields = ('duration',)
admin.site.register(ShutterSpeed, ShutterSpeedAdmin)

from .models import Teleconverter
admin.site.register(Teleconverter)

from .models import Toner
admin.site.register(Toner)