from django_filters import FilterSet
from django_currentuser.middleware import get_current_user

# Import all models that need admin pages
from schema.models import Accessory, Archive, Battery, BulkFilm, Camera, CameraModel, Developer, Enlarger, EnlargerModel, FilmStock
from schema.models import Flash, FlashModel, Lens, LensModel
from schema.models import Mount, MountAdapter, Order, PaperStock, Print
from schema.models import Negative, Film, Teleconverter, TeleconverterModel, Toner

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
        fields = ('format', 'filmstock', 'finished')

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
            'own',
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


class EnlargerModelFilter(FilterSet):
    class Meta:
        model = EnlargerModel
        fields = ('manufacturer', 'negative_size', 'type', 'light_source')

class EnlargerFilter(FilterSet):
    class Meta:
        model = Enlarger
        fields = ('enlargermodel', )

    @property
    def qs(self):
        parent = super().qs
        return parent.filter(owner=get_current_user())


class FilmStockFilter(FilterSet):

    class Meta:
        model = FilmStock
        fields = ('manufacturer', 'colour', 'panchromatic', 'process')


class FlashModelFilter(FilterSet):
    class Meta:
        model = FlashModel
        fields = ('manufacturer',
                  'pc_sync',
                  'hot_shoe',
                  'light_stand',
                  'manual_control',
                  'swivel_head',
                  'tilt_head',
                  'zoom',
                  'ttl',
                  )

class FlashFilter(FilterSet):
    class Meta:
        model = Flash
        fields = ('flashmodel',)

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
                  'own',
                  )

    @property
    def qs(self):
        parent = super().qs
        return parent.filter(owner=get_current_user())


class LensModelFilter(FilterSet):

    class Meta:
        model = LensModel
        fields = ('manufacturer', 'mount', 'zoom', 'autofocus', 'lens_type', 'purpose')


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


class NegativeFilter(FilterSet):
    class Meta:
        model = Negative
        fields = [
            'film',
            'film__camera',
            'lens',
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
            'status',
            'camera',
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
        fields = ('teleconvertermodel',)

    @property
    def qs(self):
        parent = super().qs
        return parent.filter(owner=get_current_user())

class TeleconverterModelFilter(FilterSet):
    class Meta:
        model = TeleconverterModel
        fields = ('manufacturer', 'mount',)


class TonerFilter(FilterSet):

    class Meta:
        model = Toner
        fields = ('manufacturer',)
