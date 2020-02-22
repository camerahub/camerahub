from django.forms import ModelForm
from django import forms
from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)
import sys

from schema.models import Accessory, Archive, Battery, BulkFilm, Camera, CameraModel, Developer, Enlarger, FilmStock, Filter
from schema.models import Flash, FlashProtocol, Format, Lens, LensModel, Manufacturer
from schema.models import Mount, MountAdapter, NegativeSize, Order, PaperStock, Person, Print, Toning
from schema.models import Process, Repair, Scan, Negative, Film, Series, ShutterSpeed, Teleconverter, Toner

class AccessoryForm(ModelForm):
    class Meta:
        model = Accessory
        fields = [
            'type',
            'manufacturer',
            'model',
            'acquired',
            'cost',
            'lost',
            'lost_price',
            'camera_model_compatibility',
            'lens_model_compatibility',
        ]
        if ('makemigrations' in sys.argv or 'migrate' in sys.argv or 'test' in sys.argv):
            fields.remove('manufacturer')
            fields.remove('camera_model_compatibility')
            fields.remove('lens_model_compatibility')

class ArchiveForm(ModelForm):
    class Meta:
        model = Archive
        fields = [
            'type',
            'name',
            'max_width',
            'max_height',
            'location',
            'storage',
            'sealed',
        ]

class BatteryForm(ModelForm):
    class Meta:
        model = Battery
        fields = [
            'name',
            'voltage',
            'chemistry',
            'other_names',
        ]

class BulkFilmForm(ModelForm):
    class Meta:
        model = BulkFilm
        fields = [
            'format',
            'filmstock',
            'purchase_date',
            'cost',
            'source',
            'batch',
            'expiry',
        ]
        if ('makemigrations' in sys.argv or 'migrate' in sys.argv or 'test' in sys.argv):
            fields.remove('filmstock')
            fields.remove('format')

class CameraForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CameraForm, self).__init__(*args, **kwargs)
        self.fields['lens'].queryset = Lens.objects.filter(owner = get_current_user())
        self.fields['display_lens'].queryset = Lens.objects.filter(owner = get_current_user())
    class Meta:
        model = Camera
        fields = [
            'cameramodel',
            'acquired',
            'cost',
            'serial',
            'datecode',
            'manufactured',
            'own',
            'lens',
            'notes',
            'lost',
            'lost_price',
            'source',
            'condition',
            'condition_notes',
            'display_lens',
        ]
        if ('makemigrations' in sys.argv or 'migrate' in sys.argv or 'test' in sys.argv):
            fields.remove('cameramodel')

class CameraModelForm(ModelForm):
    class Meta:
        model = CameraModel
        fields = [
            'manufacturer',
            'model',
            'disambiguation',
            'mount',
            'format',
            'focus_type',
            'metering',
            'coupled_metering',
            'metering_type',
            'introduced',
            'discontinued',
            'body_type',
            'weight',
            'introduced',
            'discontinued',
            'negative_size',
            'shutter_type',
            'shutter_model',
            'cable_release',
            'viewfinder_coverage',
            'power_drive',
            'continuous_fps',
            'fixed_mount',
            'lensmodel',
            'battery_qty',
            'battery_type',
            'notes',
            'bulb',
            'time',
            'min_iso',
            'max_iso',
            'af_points',
            'int_flash',
            'int_flash_gn',
            'ext_flash',
            'flash_metering',
            'pc_sync',
            'hotshoe',
            'coldshoe',
            'meter_min_ev',
            'meter_max_ev',
            'dof_preview',
            'tripod',
            'shutter_speeds',
            'metering_modes',
            'exposure_programs',
            'series',
        ]
        if ('makemigrations' in sys.argv or 'migrate' in sys.argv or 'test' in sys.argv):
            fields.remove('manufacturer')
            fields.remove('mount')
            fields.remove('format')
            fields.remove('battery_type')
            fields.remove('negative_size')
            fields.remove('lensmodel')
            fields.remove('flash_metering')

class DeveloperForm(ModelForm):
    class Meta:
        model = Developer
        fields = [
            'manufacturer',
            'name',
            'for_paper',
            'for_film',
            'chemistry',
        ]
        if ('makemigrations' in sys.argv or 'migrate' in sys.argv or 'test' in sys.argv):
            fields.remove('manufacturer')

class EnlargerForm(ModelForm):
    class Meta:
        model = Enlarger
        fields = [
            'manufacturer',
            'model',
            'negative_size',
            'type',
            'light_source',
            'acquired',
            'lost',
            'introduced',
            'discontinued',
            'cost',
            'lost_price',
        ]
        if ('makemigrations' in sys.argv or 'migrate' in sys.argv or 'test' in sys.argv):
            fields.remove('manufacturer')
            fields.remove('negative_size')

class FilmStockForm(ModelForm):
    class Meta:
        model = FilmStock
        fields = [
            'name',
            'manufacturer',
            'iso',
            'colour',
            'panchromatic',
            'process',
        ]
        if ('makemigrations' in sys.argv or 'migrate' in sys.argv or 'test' in sys.argv):
            fields.remove('manufacturer')
            fields.remove('process')

class FilterForm(ModelForm):
    class Meta:
        model = Filter
        fields = [
            'type',
            'thread',
            'attenuation',
            'qty',
            'manufacturer',
        ]
        if ('makemigrations' in sys.argv or 'migrate' in sys.argv or 'test' in sys.argv):
            fields.remove('manufacturer')

class FlashForm(ModelForm):
    class Meta:
        model = Flash
        fields = [
            'model',
            'manufacturer',
            'guide_number',
            'gn_info',
            'battery_powered',
            'pc_sync',
            'hot_shoe',
            'light_stand',
            'battery_type',
            'battery_qty',
            'manual_control',
            'swivel_head',
            'tilt_head',
            'zoom',
            'ttl',
            'flash_protocol',
            'trigger_voltage',
            'own',
            'acquired',
            'cost',
        ]
        if ('makemigrations' in sys.argv or 'migrate' in sys.argv or 'test' in sys.argv):
            fields.remove('manufacturer')
            fields.remove('flash_protocol')
            fields.remove('battery_type')

class FlashProtocolForm(ModelForm):
    class Meta:
        model = FlashProtocol
        fields = [
            'name',
            'manufacturer',
        ]
        if ('makemigrations' in sys.argv or 'migrate' in sys.argv or 'test' in sys.argv):
            fields.remove('manufacturer')

class FormatForm(ModelForm):
    class Meta:
        model = Format
        fields = [
            'format',
            'negative_size',
        ]
        if ('makemigrations' in sys.argv or 'migrate' in sys.argv or 'test' in sys.argv):
            fields.remove('negative_size')

class LensForm(ModelForm):
    class Meta:
        model = Lens
        fields = [
            'lensmodel',
            'serial',
            'date_code',
            'manufactured',
            'acquired',
            'cost',
            'notes',
            'own',
            'lost',
            'lost_price',
            'source',
            'condition',
            'condition_notes',
        ]
        if ('makemigrations' in sys.argv or 'migrate' in sys.argv or 'test' in sys.argv):
            fields.remove('lensmodel')

class LensModelForm(ModelForm):
    class Meta:
        model = LensModel
        fields = [
            'manufacturer',
            'model',
            'disambiguation',
            'mount',
            'zoom',
            'min_focal_length',
            'max_focal_length',
            'closest_focus',
            'max_aperture',
            'min_aperture',
            'elements',
            'groups',
            'weight',
            'nominal_min_angle_diag',
            'nominal_max_angle_diag',
            'aperture_blades',
            'autofocus',
            'filter_thread',
            'magnification',
            'url',
            'introduced',
            'discontinued',
            'negative_size',
            'fixed_mount',
            'notes',
            'coating',
            'hood',
            'exif_lenstype',
            'rectilinear',
            'length',
            'diameter',
            'image_circle',
            'formula',
            'shutter_model',
            'series',
        ]
        if ('makemigrations' in sys.argv or 'migrate' in sys.argv or 'test' in sys.argv):
            fields.remove('manufacturer')
            fields.remove('mount')
            fields.remove('negative_size')

class ManufacturerForm(ModelForm):
    class Meta:
        model = Manufacturer
        fields = [
            'name',
            'city',
            'country',
            'url',
            'founded',
            'dissolved',
        ]

class MountForm(ModelForm):
    class Meta:
        model = Mount
        fields = [
            'mount',
            'shutter_in_lens',
            'type',
            'purpose',
            'notes',
            'manufacturer',
        ]
        if ('makemigrations' in sys.argv or 'migrate' in sys.argv or 'test' in sys.argv):
            fields.remove('manufacturer')

class MountAdapterForm(ModelForm):
    class Meta:
        model = MountAdapter
        fields = [
            'camera_mount',
            'lens_mount',
            'has_optics',
            'infinity_focus',
            'notes',
        ]
        if ('makemigrations' in sys.argv or 'migrate' in sys.argv or 'test' in sys.argv):
            fields.remove('camera_mount')
            fields.remove('lens_mount')

class NegativeSizeForm(ModelForm):
    class Meta:
        model = NegativeSize
        fields = [
            'name',
            'width',
            'height',
            'crop_factor',
            'area',
            'aspect_ratio',
        ]

class OrderForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['negative'].queryset = Negative.objects.filter(owner = get_current_user())
        self.fields['print'].queryset = Print.objects.filter(owner = get_current_user())
        self.fields['recipient'].queryset = Person.objects.filter(owner = get_current_user())
    class Meta:
        model = Order
        fields = [
            'negative',
            'width',
            'height',
            'added',
            'printed',
            'print',
            'recipient',
        ]

class PaperStockForm(ModelForm):
    class Meta:
        model = PaperStock
        fields = [
            'name',
            'manufacturer',
            'resin_coated',
            'tonable',
            'colour',
            'finish',
        ]
        if ('makemigrations' in sys.argv or 'migrate' in sys.argv or 'test' in sys.argv):
            fields.remove('manufacturer')

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name']

class PrintForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PrintForm, self).__init__(*args, **kwargs)
        self.fields['negative'].queryset = Negative.objects.filter(owner = get_current_user())
        self.fields['enlarger'].queryset = Enlarger.objects.filter(owner = get_current_user())
        self.fields['lens'].queryset = Lens.objects.filter(owner = get_current_user())
        self.fields['archive'].queryset = Archive.objects.filter(owner = get_current_user())
        self.fields['printer'].queryset = Person.objects.filter(owner = get_current_user())
    class Meta:
        model = Print
        fields = [
            'negative',
            'date',
            'paper_stock',
            'height',
            'width',
            'aperture',
            'exposure_time',
            'filtration_grade',
            'development_time',
            'toner',
            'own',
            'location',
            'sold_price',
            'enlarger',
            'lens',
            'developer',
            'fine',
            'notes',
            'archive',
            'printer',
        ]
        if ('makemigrations' in sys.argv or 'migrate' in sys.argv or 'test' in sys.argv):
            fields.remove('paper_stock')
            fields.remove('developer')
            fields.remove('toner')

class ProcessForm(ModelForm):
    class Meta:
        model = Process
        fields = [
            'name',
            'colour',
            'positive',
        ]

class RepairForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RepairForm, self).__init__(*args, **kwargs)
        self.fields['camera'].queryset = Camera.objects.filter(owner = get_current_user())
        self.fields['lens'].queryset = Lens.objects.filter(owner = get_current_user())
    class Meta:
        model = Repair
        fields = [
            'camera',
            'lens',
            'date',
            'summary',
            'detail',
        ]

class ScanForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ScanForm, self).__init__(*args, **kwargs)
        self.fields['negative'].queryset = Negative.objects.filter(owner = get_current_user())
        self.fields['print'].queryset = Print.objects.filter(owner = get_current_user())
    class Meta:
        model = Scan
        fields = [
            'negative',
            'print',
            'filename',
            'date',
            'colour',
            'width',
            'height',
        ]

class NegativeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(NegativeForm, self).__init__(*args, **kwargs)
        self.fields['film'].queryset = Film.objects.filter(owner = get_current_user())
        self.fields['lens'].queryset = Lens.objects.filter(owner = get_current_user())
        self.fields['mount_adapter'].queryset = MountAdapter.objects.filter(owner = get_current_user())
        self.fields['film'].queryset = Film.objects.filter(owner = get_current_user())
        self.fields['photographer'].queryset = Person.objects.filter(owner = get_current_user())
        self.fields['copy_of'].queryset = Negative.objects.filter(owner = get_current_user())
    class Meta:
        model = Negative
        fields = [
            'film',
            'frame',
            'caption',
            'date',
            'lens',
            'shutter_speed',
            'aperture',
            'filter',
            'teleconverter',
            'notes',
            'mount_adapter',
            'focal_length',
            'latitude',
            'longitude',
            'flash',
            'metering_mode',
            'exposure_program',
            'photographer',
            'copy_of',
        ]

class FilmForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FilmForm, self).__init__(*args, **kwargs)
        self.fields['camera'].queryset = Camera.objects.filter(owner = get_current_user())
        self.fields['bulk_film'].queryset = BulkFilm.objects.filter(owner = get_current_user())
        self.fields['processed_by'].queryset = Person.objects.filter(owner = get_current_user())
        self.fields['archive'].queryset = Archive.objects.filter(owner = get_current_user())
    class Meta:
        model = Film
        fields = [
            'filmstock',
            'exposed_at',
            'format',
            'date_loaded',
            'date_processed',
            'camera',
            'title',
            'frames',
            'developer',
            'directory',
            'dev_uses',
            'dev_time',
            'dev_temp',
            'dev_n',
            'development_notes',
            'bulk_film',
            'bulk_film_loaded',
            'film_batch',
            'expiry_date',
            'purchase_date',
            'price',
            'processed_by',
            'archive',
        ]
        if ('makemigrations' in sys.argv or 'migrate' in sys.argv or 'test' in sys.argv):
            fields.remove('filmstock')
            fields.remove('developer')
            fields.remove('format')

class SeriesForm(ModelForm):
    class Meta:
        model = Series
        fields = ['name']

class TeleconverterForm(ModelForm):
    class Meta:
        model = Teleconverter
        fields = [
            'model',
            'manufacturer',
            'mount',
            'factor',
            'elements',
            'groups',
            'multicoated',
        ]
        if ('makemigrations' in sys.argv or 'migrate' in sys.argv or 'test' in sys.argv):
            fields.remove('manufacturer')
            fields.remove('mount')

class TonerForm(ModelForm):
    class Meta:
        model = Toner
        fields = [
            'name',
            'manufacturer',
            'formulation',
            'stock_dilution',
        ]
        if ('makemigrations' in sys.argv or 'migrate' in sys.argv or 'test' in sys.argv):
            fields.remove('manufacturer')
