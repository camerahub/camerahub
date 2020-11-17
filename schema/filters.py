from django_filters import FilterSet, CharFilter
from django_currentuser.middleware import get_current_user
from taggit.forms import TagField

# Import all models that need admin pages
from schema.models import Accessory, Archive, Battery, BulkFilm, Camera, CameraModel, Developer, Enlarger, FilmStock
from schema.models import Flash, Lens, LensModel
from schema.models import Mount, MountAdapter, Order, PaperStock, Print
from schema.models import Negative, Film, Teleconverter, Toner

# Define a custom tag filter


class TagFilter(CharFilter):
    field_class = TagField

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('lookup_expr', 'in')
        super().__init__(*args, **kwargs)


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
            'own',
        ]

    @property
    def qs(self):
        parent = super().qs
        return parent.filter(owner=get_current_user())


class CameraModelFilter(FilterSet):
    tags = TagFilter(field_name='tags__name', label='Tags')

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
    tags = TagFilter(field_name='tags__name', label='Tags')

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
    tags = TagFilter(field_name='tags__name', label='Tags')

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
                  )

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
    tags = TagFilter(field_name='tags__name', label='Tags')

    class Meta:
        model = LensModel
        fields = ('manufacturer', 'mount', 'zoom', 'autofocus', 'lens_type')


class MountFilter(FilterSet):
    tags = TagFilter(field_name='tags__name', label='Tags')

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
    tags = TagFilter(field_name='tags__name', label='Tags')

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
        fields = ('manufacturer', 'mount',)

    @property
    def qs(self):
        parent = super().qs
        return parent.filter(owner=get_current_user())


class TonerFilter(FilterSet):
    tags = TagFilter(field_name='tags__name', label='Tags')

    class Meta:
        model = Toner
        fields = ('manufacturer',)
