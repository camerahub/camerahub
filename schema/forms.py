import sys
from django.forms import ModelForm
from django.db.models import Q
from django_currentuser.middleware import get_current_user
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Div, Hidden, HTML
from crispy_forms.bootstrap import FormActions, AppendedText, InlineCheckboxes, PrependedText, TabHolder, Tab

from schema.models import Accessory, Archive, Battery, BulkFilm, Camera, CameraModel, Developer, Enlarger, FilmStock, Filter
from schema.models import Flash, FlashProtocol, Format, Lens, LensModel, Manufacturer
from schema.models import Mount, MountAdapter, NegativeSize, Order, PaperStock, Person, Print
from schema.models import Process, Repair, Scan, Negative, Film, Teleconverter, Toner


class AccessoryForm(ModelForm):
    class Meta:
        model = Accessory
        fields = [
            'manufacturer',
            'model',
            'type',
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('Save', 'Save'))


class ArchiveForm(ModelForm):
    class Meta:
        model = Archive
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                'name',
                'type',
                AppendedText('max_width', '"'),
                AppendedText('max_height', '"'),
                'location',
                'storage',
                'sealed',
            ),
            FormActions(
                Submit('save', 'Save'),
            )
        )


class BatteryForm(ModelForm):
    class Meta:
        model = Battery
        fields = [
            'name',
            'voltage',
            'chemistry',
            'compatible_with',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('Save', 'Save'))


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('Save', 'Save'))


class CameraForm(ModelForm):
    class Meta:
        model = Camera
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                'cameramodel',
                'acquired',
                'cost',
                'source',
                'serial',
                'datecode',
                'manufactured',
                'own',
                'notes',
                'lost',
                'lost_price',
                'condition',
                'condition_notes',
            ),
            FormActions(
                Submit('save', 'Save')
            )
        )


class CameraModelForm(ModelForm):
    class Meta:
        model = CameraModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.helper.layout = Layout(
            Fieldset(
                'Basics',
                'manufacturer',
                'model',
                'other_names',
                'disambiguation',
                'introduced',
                'discontinued',
                'format',
                'negative_size',
            ),
            Div(
                TabHolder(
                    Tab('Interchangeable lens',
                        Fieldset(
                            'Lens mount',
                            'mount',
                        ),
                        ),
                    Tab('Fixed lens',
                        Fieldset(
                            'Lens',
                            'lens_manufacturer',
                            'lens_model_name',
                        ),
                        Fieldset(
                            'Optics',
                            'zoom',
                            AppendedText('min_focal_length', 'mm'),
                            AppendedText('max_focal_length', 'mm'),
                            PrependedText('max_aperture', 'f/'),
                            PrependedText('min_aperture', 'f/'),
                            AppendedText('closest_focus', 'm'),
                            'elements',
                            'groups',
                            AppendedText('nominal_min_angle_diag', '&deg;'),
                            AppendedText('nominal_max_angle_diag', '&deg;'),
                            'aperture_blades',
                            'coating',
                            AppendedText('magnification', '&times;'),
                        ),
                        Fieldset(
                            'Physical',
                            AppendedText('filter_thread', 'mm'),
                            'hood',
                        ),
                        ),
                ),
                css_class="border",
            ),
            Fieldset(
                'Physical',
                'body_type',
                AppendedText('weight', 'g'),
            ),
            Fieldset(
                'Focus',
                'focus_type',
                AppendedText('viewfinder_coverage', '%'),
                'af_points',
            ),
            Fieldset(
                'Metering',
                'metering',
                'metering_type',
                InlineCheckboxes('metering_modes'),
                InlineCheckboxes('exposure_programs'),
                'min_iso',
                'max_iso',
                'meter_min_ev',
                'meter_max_ev',
            ),
            Fieldset(
                'Shutter',
                'shutter_type',
                'shutter_model',
                'fastest_shutter_speed',
                'slowest_shutter_speed',
                'bulb',
                'time',
            ),
            Fieldset(
                'Flash',
                'int_flash',
                'int_flash_gn',
                'ext_flash',
                'flash_metering',
                'pc_sync',
                'shoe',
                'x_sync',
            ),
            Fieldset(
                'Battery',
                'battery_qty',
                'battery_type',
            ),
            Fieldset(
                'Features',
                'cable_release',
                'dof_preview',
                'mirror_lockup',
                'tripod',
                'self_timer',
                'date_imprint',
                'interchangeable_backs',
                'interchangeable_finders',
                'strap_lugs',
                'multiple_exposures',
                'internal_power_drive',
                AppendedText('continuous_fps', 'fps'),
                'external_power_drive',
            ),
            Fieldset(
                'Misc',
                'notes',
                'tags',
                'url',
                'image',
                'image_attribution',
                'image_attribution_url',
            ),
            FormActions(
                Submit('save', 'Save')
            )
        )


class DeveloperForm(ModelForm):
    class Meta:
        model = Developer
        fields = [
            'manufacturer',
            'name',
            'for_paper',
            'for_film',
            'chemistry',
            'tags',
        ]
        if ('makemigrations' in sys.argv or 'migrate' in sys.argv or 'test' in sys.argv):
            fields.remove('manufacturer')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('Save', 'Save'))


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('Save', 'Save'))


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
            'tags',
        ]
        if ('makemigrations' in sys.argv or 'migrate' in sys.argv or 'test' in sys.argv):
            fields.remove('manufacturer')
            fields.remove('process')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('Save', 'Save'))


class FilterForm(ModelForm):
    class Meta:
        model = Filter
        fields = [
            'type',
            'shortname',
            'attenuation',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('Save', 'Save'))


class FlashForm(ModelForm):
    class Meta:
        model = Flash
        fields = [
            'manufacturer',
            'model',
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('Save', 'Save'))


class FlashProtocolForm(ModelForm):
    class Meta:
        model = FlashProtocol
        fields = [
            'name',
            'manufacturer',
        ]
        if ('makemigrations' in sys.argv or 'migrate' in sys.argv or 'test' in sys.argv):
            fields.remove('manufacturer')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('Save', 'Save'))


class FormatForm(ModelForm):
    class Meta:
        model = Format
        fields = [
            'format',
            'negative_size',
        ]
        if ('makemigrations' in sys.argv or 'migrate' in sys.argv or 'test' in sys.argv):
            fields.remove('negative_size')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('Save', 'Save'))


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('Save', 'Save'))


class LensModelForm(ModelForm):
    class Meta:
        model = LensModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Fieldset(
                'Basics',
                'manufacturer',
                'model',
                'disambiguation',
                'mount',
                'introduced',
                'discontinued',
            ),
            Fieldset(
                'Optics',
                'zoom',
                AppendedText('min_focal_length', 'mm'),
                AppendedText('max_focal_length', 'mm'),
                PrependedText('max_aperture', 'f/'),
                PrependedText('min_aperture', 'f/'),
                AppendedText('closest_focus', 'm'),
                'elements',
                'groups',
                AppendedText('nominal_min_angle_diag', '&deg;'),
                AppendedText('nominal_max_angle_diag', '&deg;'),
                'lens_type',
                AppendedText('image_circle', 'mm'),
                'aperture_blades',
                'coating',
                'autofocus',
                'perspective_control',
                AppendedText('magnification', '&times;'),
                'negative_size',
            ),
            Fieldset(
                'Physical',
                AppendedText('weight', 'g'),
                AppendedText('length', 'mm'),
                AppendedText('diameter', 'mm'),
                AppendedText('filter_thread', 'mm'),
                'hood',
                'shutter_model',
            ),
            Fieldset(
                'Misc',
                'notes',
                'tags',
                'url',
                'image',
                'image_attribution',
                'image_attribution_url',
                'diagram',
                'diagram_attribution',
                'diagram_attribution_url',
            ),
            FormActions(
                Submit('save', 'Save')
            )
        )


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
            'tags',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('Save', 'Save'))


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
            'tags',
        ]
        if ('makemigrations' in sys.argv or 'migrate' in sys.argv or 'test' in sys.argv):
            fields.remove('manufacturer')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('Save', 'Save'))


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('Save', 'Save'))


class NegativeSizeForm(ModelForm):
    class Meta:
        model = NegativeSize
        fields = [
            'name',
            'width',
            'height',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('Save', 'Save'))


class OrderForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['negative'].queryset = Negative.objects.filter(
            owner=get_current_user())
        self.fields['print'].queryset = Print.objects.filter(
            owner=get_current_user())
        self.fields['recipient'].queryset = Person.objects.filter(
            owner=get_current_user())

        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('Save', 'Save'))

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
            'colour',
            'finish',
            'tags',
        ]
        if ('makemigrations' in sys.argv or 'migrate' in sys.argv or 'test' in sys.argv):
            fields.remove('manufacturer')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('Save', 'Save'))


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('Save', 'Save'))


class PrintForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['negative'].queryset = Negative.objects.filter(
            owner=get_current_user())
        self.fields['enlarger'].queryset = Enlarger.objects.filter(
            owner=get_current_user())
        self.fields['lens'].queryset = Lens.objects.filter(
            owner=get_current_user())
        self.fields['archive'].queryset = Archive.objects.filter(
            owner=get_current_user(), type='Print', sealed=False)
        self.fields['printer'].queryset = Person.objects.filter(
            owner=get_current_user())
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('Save', 'Save'))

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('Save', 'Save'))


class RepairForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['camera'].queryset = Camera.objects.filter(
            owner=get_current_user())
        self.fields['lens'].queryset = Lens.objects.filter(
            owner=get_current_user())
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('Save', 'Save'))

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
        super().__init__(*args, **kwargs)
        self.fields['negative'].queryset = Negative.objects.filter(
            owner=get_current_user())
        self.fields['print'].queryset = Print.objects.filter(
            owner=get_current_user())
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('Save', 'Save'))

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
        super().__init__(*args, **kwargs)
        self.fields['film'].queryset = Film.objects.filter(
            owner=get_current_user())
        self.fields['lens'].queryset = Lens.objects.filter(
            owner=get_current_user())
        self.fields['mount_adapter'].queryset = MountAdapter.objects.filter(
            owner=get_current_user())
        self.fields['film'].queryset = Film.objects.filter(
            owner=get_current_user())
        self.fields['photographer'].queryset = Person.objects.filter(
            owner=get_current_user())
        self.fields['copy_of'].queryset = Negative.objects.filter(
            owner=get_current_user())
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('Save', 'Save'))

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
    class Meta:
        model = Film
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['camera'].queryset = Camera.objects.filter(
            owner=get_current_user())
        self.fields['bulk_film'].queryset = BulkFilm.objects.filter(
            owner=get_current_user())
        self.fields['processed_by'].queryset = Person.objects.filter(
            owner=get_current_user())
        self.fields['archive'].queryset = Archive.objects.filter(
            owner=get_current_user())
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'filmstock',
            'exposed_at',
            'format',
            'status',
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
            FormActions(
                Submit('save', 'Save'),
            ),
        )


class FilmAddForm(ModelForm):
    class Meta:
        model = Film
        fields = ['filmstock', 'format', 'frames', 'film_batch', 'expiry_date',
                  'purchase_date', 'price', 'bulk_film', 'bulk_film_loaded', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bulk_film'].queryset = BulkFilm.objects.filter(
            owner=get_current_user())
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Fieldset(
                'Add a new film to your collection',
                'filmstock',
                'format',
                'frames',
                Div(
                    TabHolder(
                        Tab('Single film',
                            HTML(
                                "<p>Choose Single Film for regular roll or sheet films</p>"),
                            'film_batch',
                            'expiry_date',
                            'purchase_date',
                            'price',
                            ),
                        Tab('Bulk film',
                            HTML(
                                "<p>Choose Bulk Film for film that has been cut from a bulk roll</p>"),
                            'bulk_film',
                            'bulk_film_loaded',
                            ),
                    ),
                    css_class="border",
                ),
            ),
            Hidden('status', 'Available'),
            FormActions(
                Submit('save', 'Save'),
            ),
        )


class FilmLoadForm(ModelForm):
    class Meta:
        model = Film
        fields = ['camera', 'title', 'exposed_at', 'date_loaded', 'frames', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['camera'].queryset = Camera.objects.filter(
            owner=get_current_user())
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Fieldset(
                'Load this film into a camera',
                'camera',
                'title',
                'exposed_at',
                'date_loaded',
                'frames',
            ),
            Hidden('status', 'Loaded'),
            FormActions(
                Submit('save', 'Save'),
            ),
        )


class FilmDevelopForm(ModelForm):
    class Meta:
        model = Film
        fields = ['date_processed', 'developer', 'directory', 'dev_uses', 'dev_time', 'dev_temp', 'dev_n', 'development_notes', 'processed_by', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['processed_by'].queryset = Person.objects.filter(
            owner=get_current_user())
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Fieldset(
                'Develop this film',
                'date_processed',
                'developer',
                'directory',
                'dev_uses',
                'dev_time',
                AppendedText('dev_temp', '&deg;C'),
                'dev_n',
                'development_notes',
                'processed_by',
            ),
            Hidden('status', 'Developed'),
            FormActions(
                Submit('save', 'Save'),
            ),
        )


class FilmArchiveForm(ModelForm):
    class Meta:
        model = Film
        fields = ['archive', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['processed_by'].queryset = Person.objects.filter(
            owner=get_current_user())
        self.fields['archive'].queryset = Archive.objects.filter(
            Q(type='Negative') | Q(type='Slide'), owner=get_current_user(), sealed=False)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Fieldset(
                'Archive this film',
                'archive',
            ),
            Hidden('status', 'Archived'),
            FormActions(
                Submit('save', 'Save'),
            ),
        )


class TeleconverterForm(ModelForm):
    class Meta:
        model = Teleconverter
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Fieldset(
                'Basics',
                'model',
                'manufacturer',
                'mount',
                AppendedText('factor', '&times;'),
                'elements',
                'groups',
                'multicoated',
            ),
            FormActions(
                Submit('save', 'Save')
            )
        )


class TonerForm(ModelForm):
    class Meta:
        model = Toner
        fields = [
            'name',
            'manufacturer',
            'formulation',
            'stock_dilution',
            'tags',
        ]
        if ('makemigrations' in sys.argv or 'migrate' in sys.argv or 'test' in sys.argv):
            fields.remove('manufacturer')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('Save', 'Save'))
