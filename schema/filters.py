from django_filters import FilterSet
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)

# Import all models that need admin pages
from schema.models import Accessory, Archive, Battery, BulkFilm, Camera, CameraModel, Developer, Enlarger, FilmStock, Filter
from schema.models import Flash, FlashProtocol, Format, Lens, LensModel, Manufacturer
from schema.models import Mount, MountAdapter, NegativeSize, Order, PaperStock, Person, Print, Toning
from schema.models import Process, Repair, Scan, Negative, Film, Series, ShutterSpeed, Teleconverter, Toner


class AccessoryFilter(FilterSet):
    class Meta:
        model = Accessory
        fields = ('type',)

    @property
    def qs(self):
        parent = super().qs
        return parent.filter(owner=get_current_user())


class ArchiveFilter(FilterSet):
    class Meta:
        model = Archive
        fields = ('type', 'location', 'storage', 'sealed')

    @property
    def qs(self):
        parent = super().qs
        return parent.filter(owner=get_current_user())


class BatteryFilter(FilterSet):
    class Meta:
        model = Battery
        fields = ('chemistry',)


class BulkFilmFilter(FilterSet):
    class Meta:
        model = BulkFilm
        fields = ('format', 'filmstock',)

    @property
    def qs(self):
        parent = super().qs
        return parent.filter(owner=get_current_user())


class CameraFilter(FilterSet):
    class Meta:
        model = Camera
        fields = [
            'cameramodel__manufacturer',
            'cameramodel__mount',
            'cameramodel__format',
            'cameramodel__negative_size',
            'cameramodel__body_type',
        ]

    @property
    def qs(self):
        parent = super().qs
        return parent.filter(owner=get_current_user())


class CameraModelFilter(FilterSet):
    class Meta:
        model = CameraModel
        fields = [
            'manufacturer',
            'mount',
            'format',
            'negative_size',
            'body_type',
        ]


class DeveloperFilter(FilterSet):
    class Meta:
        model = Developer
        fields = ('manufacturer', 'for_paper', 'for_film')


class EnlargerFilter(FilterSet):
    class Meta:
        model = Enlarger
        fields = ('manufacturer', 'negative_size', 'type', 'light_source')

    @property
    def qs(self):
        parent = super().qs
        return parent.filter(owner=get_current_user())


class FilmStockFilter(FilterSet):
    class Meta:
        model = FilmStock
        fields = ('manufacturer', 'colour', 'panchromatic', 'process')


class FlashFilter(FilterSet):
    class Meta:
        model = Flash
        fields = ('manufacturer',
                  'pc_sync',
                  'hot_shoe',
                  'light_stand',
                  'manual_control',
                  'swivel_head',
                  'tilt_head',
                  'zoom',
                  'ttl',
                  'flash_protocol',)

    @property
    def qs(self):
        parent = super().qs
        return parent.filter(owner=get_current_user())


class LensFilter(FilterSet):
    class Meta:
        model = Lens
        fields = ('lensmodel__manufacturer',
                  'lensmodel__mount',
                  'lensmodel__zoom',
                  'lensmodel__autofocus',
                  'lensmodel__fixed_mount'
                  )

    @property
    def qs(self):
        parent = super().qs
        return parent.filter(owner=get_current_user())


class LensModelFilter(FilterSet):
    class Meta:
        model = LensModel
        fields = ('manufacturer', 'mount', 'zoom', 'autofocus', 'fixed_mount')


class MountFilter(FilterSet):
    class Meta:
        model = Mount
        fields = ('shutter_in_lens', 'type', 'purpose')


class MountAdapterFilter(FilterSet):
    class Meta:
        model = MountAdapter
        fields = ('camera_mount', 'lens_mount',
                  'has_optics', 'infinity_focus',)

    @property
    def qs(self):
        parent = super().qs
        return parent.filter(owner=get_current_user())


class OrderFilter(FilterSet):
    class Meta:
        model = Order
        fields = ('printed',)

    @property
    def qs(self):
        parent = super().qs
        return parent.filter(owner=get_current_user())


class PaperStockFilter(FilterSet):
    class Meta:
        model = PaperStock
        fields = ('manufacturer', 'resin_coated', 'colour', 'finish')


class PrintFilter(FilterSet):
    class Meta:
        model = Print
        fields = [
            'paper_stock',
            'developer',
            'fine',
            'archive',
        ]

    @property
    def qs(self):
        parent = super().qs
        return parent.filter(owner=get_current_user())


class RepairFilter(FilterSet):
    class Meta:
        model = Repair
        fields = ('camera', 'lens',)

    @property
    def qs(self):
        parent = super().qs
        return parent.filter(owner=get_current_user())


class NegativeFilter(FilterSet):
    class Meta:
        model = Negative
        fields = [
            'film',
            'lens',
            'filter',
            'metering_mode',
            'exposure_program',
        ]

    @property
    def qs(self):
        parent = super().qs
        return parent.filter(owner=get_current_user())


class FilmFilter(FilterSet):
    class Meta:
        model = Film
        fields = [
            'filmstock',
            'format',
            'camera',
            'developer',
            'bulk_film',
            'archive',
        ]

    @property
    def qs(self):
        parent = super().qs
        return parent.filter(owner=get_current_user())


class TeleconverterFilter(FilterSet):
    class Meta:
        model = Teleconverter
        fields = ('manufacturer', 'mount',)

    @property
    def qs(self):
        parent = super().qs
        return parent.filter(owner=get_current_user())


class TonerFilter(FilterSet):
    class Meta:
        model = Toner
        fields = ('manufacturer',)
