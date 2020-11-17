from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from schema.models import Process, Scan, Negative, Film, ShutterSpeed, Teleconverter, Toner
from schema.models import Mount, MountAdapter, NegativeSize, Order, PaperStock, Person, Print
from schema.models import Flash, Format, Lens, LensModel, Manufacturer
from schema.models import Accessory, Archive, Battery, BulkFilm, Camera, CameraModel, Developer, Enlarger, FilmStock, Filter

# The text to put at the top of each admin page, as an <h1> (a string). By default, this is “Django administration”.
admin.site.site_header = 'CameraHub'

# The text to put at the end of each admin page’s <title> (a string). By default, this is “Django site admin”.
admin.site.site_title = 'CameraHub'

# The text to put at the top of the admin index page (a string). By default, this is “Site administration”.
admin.site.index_title = 'CameraHub'

# The URL for the “View site” link at the top of each admin page. By default, site_url is /. Set it to None to remove the link.
admin.site.site_url = None

# Import all models that need admin pages

# Define inlines that can be embedded into other admin pages


class CameraInline(admin.TabularInline):
    model = Camera
    extra = 0


class CameraModelInline(admin.TabularInline):
    model = CameraModel
    extra = 0


class LensInline(admin.TabularInline):
    model = Lens
    extra = 0


class NegativeInline(admin.TabularInline):
    model = Negative
    extra = 0


class PrintInline(admin.TabularInline):
    model = Print
    extra = 0


class ScanInline(admin.TabularInline):
    model = Scan
    extra = 0


class ToningInline(admin.TabularInline):
    model = Print.toner.through
    verbose_name = "toner"
    verbose_name_plural = "toners"
    extra = 0

# Now register the admin pages, customising where necessary


class AccessoryAdmin(admin.ModelAdmin):
    filter_horizontal = ('camera_model_compatibility',
                         'lens_model_compatibility')
    exclude = ('owner',)


admin.site.register(Accessory, AccessoryAdmin)


class ArchiveAdmin(admin.ModelAdmin):
    exclude = ('owner',)


admin.site.register(Archive, ArchiveAdmin)

admin.site.register(Battery, SimpleHistoryAdmin)


class BulkFilmAdmin(admin.ModelAdmin):
    exclude = ('owner',)


admin.site.register(BulkFilm, BulkFilmAdmin)


class CameraAdmin(admin.ModelAdmin):
    exclude = ('owner',)


admin.site.register(Camera, CameraAdmin)


class CameraModelAdmin(SimpleHistoryAdmin):
    fieldsets = (
        (None, {
            'fields': ('manufacturer', 'model', 'mount', 'format', 'body_type', 'weight', ('introduced', 'discontinued'), 'negative_size', 'cable_release', 'viewfinder_coverage', ('internal_power_drive', 'continuous_fps'), ('battery_qty', 'battery_type'), 'notes', 'tripod'),
            'description': 'Enter information about this camera model',
        }),
        ('Metering', {
            'fields': ('metering', 'metering_type', ('min_iso', 'max_iso'), ('meter_min_ev', 'meter_max_ev'), 'metering_modes', 'exposure_programs')
        }),
        ('Flash', {
            'fields': ('int_flash', 'int_flash_gn', 'ext_flash', 'pc_sync', 'shoe')
        }),
        ('Focus', {
            'fields': ('focus_type', 'af_points', 'dof_preview')
        }),
        ('Shutter', {
            'fields': ('shutter_type', 'shutter_model', 'fastest_shutter_speed', 'slowest_shutter_speed', 'bulb', 'time'),
        }),
    )
    inlines = [
        CameraInline,
    ]
    filter_horizontal = ('metering_modes', 'exposure_programs')
    search_fields = ['manufacturer__name', 'model', 'notes']
    list_display = ('__str__', 'mount', 'format', 'body_type', 'introduced')
    list_filter = ('manufacturer__name', 'mount', 'format', 'body_type')


admin.site.register(CameraModel, CameraModelAdmin)

admin.site.register(Developer, SimpleHistoryAdmin)


class EnlargerAdmin(admin.ModelAdmin):
    exclude = ('owner',)


admin.site.register(Enlarger, EnlargerAdmin)

admin.site.register(FilmStock, SimpleHistoryAdmin)


class FilterAdmin(admin.ModelAdmin):
    exclude = ('owner',)


admin.site.register(Filter, FilterAdmin)


class FlashAdmin(admin.ModelAdmin):
    exclude = ('owner',)


admin.site.register(Flash, FlashAdmin)

admin.site.register(Format, SimpleHistoryAdmin)


class LensAdmin(admin.ModelAdmin):
    exclude = ('owner',)


admin.site.register(Lens, LensAdmin)


class LensModelAdmin(SimpleHistoryAdmin):
    fieldsets = (
        (None, {
            'fields': ('manufacturer', 'model', 'mount'),
            'description': 'Enter information about this camera model',
        }),
        ('Optics', {
            'fields': ('zoom', ('min_focal_length', 'max_focal_length'), 'closest_focus', ('max_aperture', 'min_aperture'), ('elements', 'groups'), ('nominal_min_angle_diag', 'nominal_max_angle_diag'), 'magnification'),
        }),
        ('Physical', {
            'fields': ('length', 'diameter', 'weight'),
        }),
        ('Other', {
            'fields': ('aperture_blades', 'autofocus', 'filter_thread', 'linkurl', 'introduced', 'discontinued', 'negative_size', 'notes', 'coating', 'hood', 'image_circle', 'shutter_model'),
        })
    )
    inlines = [
        LensInline,
    ]
    search_fields = ['manufacturer__name', 'model', 'notes']
    list_display = ('__str__', 'mount', 'min_focal_length',
                    'max_aperture', 'introduced')
    list_filter = ('manufacturer__name', 'mount')


admin.site.register(LensModel, LensModelAdmin)

admin.site.register(Manufacturer, SimpleHistoryAdmin)

admin.site.register(Mount, SimpleHistoryAdmin)


class MountAdapterAdmin(admin.ModelAdmin):
    exclude = ('owner',)


admin.site.register(MountAdapter, MountAdapterAdmin)


class NegativeSizeAdmin(SimpleHistoryAdmin):
    readonly_fields = ('area', 'crop_factor', 'aspect_ratio')


admin.site.register(NegativeSize, NegativeSizeAdmin)


class OrderAdmin(admin.ModelAdmin):
    exclude = ('owner',)


admin.site.register(Order, OrderAdmin)

admin.site.register(PaperStock, SimpleHistoryAdmin)


class PersonAdmin(admin.ModelAdmin):
    exclude = ('owner',)


admin.site.register(Person, PersonAdmin)


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
    exclude = ('owner',)
    search_fields = ['negative__caption', 'notes']
    list_display = ('__str__', 'date', 'negative')
    list_filter = ('paper_stock', 'developer', 'fine')


admin.site.register(Print, PrintAdmin)

admin.site.register(Process)

class ScanAdmin(admin.ModelAdmin):
    exclude = ('owner',)


admin.site.register(Scan, ScanAdmin)


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
            'fields': ('location',),
        }),
    )
    search_fields = ['caption', 'notes']
    list_display = ('__str__', 'caption', 'date',)
    list_filter = ('film', 'photographer')
    inlines = [
        ScanInline,
        PrintInline,
    ]
    exclude = ('owner',)


admin.site.register(Negative, NegativeAdmin)


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
            'fields': ('developer', 'developer_previous_uses', 'development_time', 'development_temperature', 'development_compensation', 'development_notes', 'processed_by', 'date_processed'),
        }),
        ('Archive', {
            'fields': ('archive', ),
        })
    )
    inlines = [
        NegativeInline,
    ]
    exclude = ('owner',)


admin.site.register(Film, FilmAdmin)


class ShutterSpeedAdmin(admin.ModelAdmin):
    readonly_fields = ('duration',)


admin.site.register(ShutterSpeed, ShutterSpeedAdmin)


class TeleconverterAdmin(admin.ModelAdmin):
    exclude = ('owner',)


admin.site.register(Teleconverter, TeleconverterAdmin)

admin.site.register(Toner, SimpleHistoryAdmin)
