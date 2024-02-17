from iommi import Form
from schema.models import Battery, CameraModel, Manufacturer, Mount, PaperStock, Accessory, Archive, EnlargerModel, Developer, Format, FlashModel, FilmStock, LensModel, Process, Filter, Flash, Teleconverter, TeleconverterModel
from schema.models import Enlarger, BulkFilm, Camera, Lens, MountAdapter, NegativeSize, Person, Scan, Negative, Film, Print, Toner
#from django.forms import ModelForm
#from django.db.models import Q
#from django_currentuser.middleware import get_current_user
#from bootstrap_datepicker_plus.widgets import DatePickerInput, DateTimePickerInput, YearPickerInput, MonthPickerInput, TimePickerInput

def battery_edit(request, slug):
    return Form.edit(
        auto__instance=Battery.objects.get(slug=slug),
    )
    # fields = ['name', 'voltage', 'chemistry', 'compatible_with']
        #self.helper.layout = Layout(
        #    Fieldset('Summary',
        #             'name',
        #             AppendedText('voltage', 'V'),
        #             'chemistry',
        #             ),
        #    Fieldset('Compatibility',
        #             'compatible_with',
        #             ),

def cameramodel_edit(request, slug):
    return Form.edit(
        auto__instance=CameraModel.objects.get(slug=slug),
    )
        #widgets = {
        #    'introduced': YearPickerInput(format='%Y'),
        #    'discontinued': YearPickerInput(format='%Y'),
        #}
            #Fieldset('Summary',
            #         'manufacturer',
            #         'model',
            #         'disambiguation',
            #         'introduced',
            #         'discontinued',
            #         'format',
            #         'negative_size',
            #         'interchangeable_lens',
            #         ),
            #Div(
            #    TabHolder(
            #        Tab('Interchangeable lens',
            #            Fieldset('Lens mount',
            #                     'mount',
            #                     ),
            #            ),
            #        Tab('Fixed lens',
            #            Fieldset('Lens',
            #                     'lens_manufacturer',
            #                     'lens_model_name',
            #                     ),
            #            Fieldset('Optics',
            #                     'zoom',
            #                     AppendedText(
            #                         'min_focal_length', 'mm'),
            #                     AppendedText('max_focal_length', 'mm'),
            #                     PrependedText('max_aperture', 'f/'),
            #                     PrependedText('min_aperture', 'f/'),
            #                     AppendedText('closest_focus', 'm'),
            #                     'elements',
            #                     'groups',
            #                     AppendedText(
            #                         'nominal_min_angle_diag', '&deg;'),
            #                     AppendedText(
            #                         'nominal_max_angle_diag', '&deg;'),
            #                     'aperture_blades',
            #                     'coating',
            #                     AppendedText('magnification', '&times;'),
            #                     ),
            #            Fieldset('Physical',
            #                     AppendedText('filter_thread', 'mm'),
            #                     'hood',
            #                     ),
            #            ),
            #    ),
            #    css_class="border",
            #),
            #Fieldset('Physical',
            #         'body_type',
            #         AppendedText('weight', 'g'),
            #         ),
            #Fieldset('Focus',
            #         'focus_type',
            #         'af_points',
            #         AppendedText('viewfinder_coverage', '%'),
            #         ),
            #Fieldset('Metering',
            #         'metering',
            #         'metering_type',
            #         'min_iso',
            #         'max_iso',
            #         'dx_code',
            #         'meter_min_ev',
            #         'meter_max_ev',
            #         InlineCheckboxes('metering_modes'),
            #         InlineCheckboxes('exposure_programs'),
            #         ),
            #Fieldset('Shutter',
            #         'shutter_type',
            #         'shutter_model',
            #         'fastest_shutter_speed',
            #         'slowest_shutter_speed',
            #         'bulb',
            #         'time',
            #         ),
            #Fieldset('Film transport',
            #         'internal_power_drive',
            #         AppendedText('continuous_fps', 'fps'),
            #         'external_power_drive',
            #         ),
            #Fieldset('Power',
            #         'battery_qty',
            #         'battery_type',
            #         ),
            #Fieldset('Flash',
            #         'int_flash',
            #         AppendedText('int_flash_gn', 'm'),
            #         'ext_flash',
            #         'pc_sync',
            #         'shoe',
            #         'x_sync',
            #         ),
            #Fieldset('Features',
            #         'dof_preview',
            #         'mirror_lockup',
            #         'tripod',
            #         'self_timer',
            #         'date_imprint',
            #         'cable_release',
            #         'interchangeable_backs',
            #         'interchangeable_finders',
            #         'strap_lugs',
            #         'multiple_exposures',
            #         ),
            #Fieldset('Misc',
            #         'notes',
            #         'tags',
            #         'link',
            #         'image',
            #         'image_attribution',
            #         'image_attribution_link',
            #         ),


def manufacturer_create(request, slug):
    return Form.create(
        auto__model=Manufacturer
    )

def manufacturer_edit(request, slug):
    return Form.edit(
        auto__instance=Manufacturer.objects.get(slug=slug),
    )
        #fields = ['name', 'city', 'country', 'link',
        #          'founded', 'dissolved', 'tags']
        #widgets = {
        #    ,
        #    'founded': YearPickerInput(format='%Y'),
        #    'dissolved': YearPickerInput(format='%Y'),
        #}
        #self.helper.layout = Layout(
        #    Fieldset('Summary',
        #             'name',
        #             'city',
        #             'country',
        #             'link',
        #             'founded',
        #             'dissolved',
        #             ),
        #    Fieldset('Meta',
        #             'tags',
        #             ),


def mount_edit(request, slug):
    return Form.edit(
        auto__instance=Mount.objects.get(slug=slug),
    )
        #fields = ['mount', 'shutter_in_lens', 'type',
        #          'purpose', 'notes', 'manufacturer', 'tags']
        #self.helper.layout = Layout(
        #    Fieldset('Summary',
        #             'mount',
        #             'shutter_in_lens',
        #             'type',
        #             'purpose',
        #             'notes',
        #             'manufacturer',
        #             ),
        #    Fieldset('Meta',
         #            'tags',
        #             ),

def paperstock_edit(request, pk):
    return Form.edit(
        auto__instance=PaperStock.objects.get(pk=pk),
    )
        #fields = ['name', 'manufacturer',
        #          'resin_coated', 'colour', 'finish', 'tags']
        #self.helper.layout = Layout(
        #    Fieldset('Summary',
        #             'name',
        #             'manufacturer',
        #             'resin_coated',
        #             'colour',
        #             'finish',
        #             ),
        #    Fieldset('Meta',
        #             'tags',
        #             ),

def accessory_edit(request, id_owner):
    return Form.edit(
        auto__instance=Accessory.objects.get(id_owner=id_owner),
    )
        #fields = ['manufacturer', 'model', 'type', 'acquired', 'cost', 'lost',
        #          'lost_price', 'camera_model_compatibility', 'lens_model_compatibility']
        #widgets = {
        #    'acquired': DatePickerInput(format='%Y-%m-%d'),
        #    'lost': DatePickerInput(format='%Y-%m-%d'),
        #self.helper.layout = Layout(
        #    Fieldset('Summary',
        #             'manufacturer',
        #             'model',
        #             'type',
        #             ),
        #    Fieldset('Compatibility',
        #             'camera_model_compatibility',
        #             'lens_model_compatibility',
        #             ),
        #    Fieldset('Ownership',
        #             'acquired',
        #             'cost',
        #             'lost',
        #             'lost_price',
        #             ),

def archive_edit(request, id_owner):
    return Form.edit(
        auto__instance=Archive.objects.get(id_owner=id_owner),
    )
        #fields = ['name', 'type', 'max_width',
        #          'max_height', 'location', 'storage', 'sealed']
        #self.helper.layout = Layout(
        #    Div(
        #        'name',
        #        'type',
        #        AppendedText('max_width', '"'),
        #        AppendedText('max_height', '"'),
        #        'location',
        #        'storage',
        #        'sealed',
        #    ),

def enlargermodel_edit(request, id_owner):
    return Form.edit(
        auto__instance=EnlargerModel.objects.get(id_owner=id_owner),
    )
        #fields = ['manufacturer', 'model', 'disambiguation', 'negative_size',
        #          'type', 'light_source', 'introduced', 'discontinued', 'tags', 'image', 'image_attribution', 'image_attribution_link']
        #widgets = {
        #    'introduced': YearPickerInput(format='%Y'),
        #    'discontinued': YearPickerInput(format='%Y'),   
        #}
        #self.helper.layout = Layout(
        #    Fieldset('Summary',
        #             'manufacturer',
        #             'model',
        #             'disambiguation',
        #             'negative_size',
        #             'type',
        #             'light_source',
        #             'introduced',
        #             'discontinued',
        #             ),
        #    Fieldset('Meta',
        #             'tags',
        #             'image',
        #             'image_attribution',
        #             'image_attribution_link',
        #             ),

def developer_edit(request, slug):
    return Form.edit(
        auto__instance=Developer.objects.get(slug=slug),
    )
        #fields = ['manufacturer', 'name', 'for_paper',
        #          'for_film', 'chemistry', 'tags']
        #self.helper.layout = Layout(
        #    Fieldset('Summary',
        #             'manufacturer',
        #             'name',
        #             'for_paper',
        #             'for_film',
        #             'chemistry',
        #             ),
        #    Fieldset('Meta',
        #             'tags',
        #             ),

def format_edit(request, pk):
    return Form.edit(
        auto__instance=Format.objects.get(pk=pk),
    )
        #fields = ['format', 'negative_size']
        #self.helper.layout = Layout(
        #    'format',
        #    'negative_size',
        #    FormActionButtons
        #)

def flashmodel_edit(request, slug):
    return Form.edit(
        auto__instance=FlashModel.objects.get(slug=slug),
    )
        #fields = ['manufacturer', 'model', 'disambiguation', 'guide_number', 'gn_info', 'battery_powered', 'pc_sync', 'hot_shoe', 'light_stand', 'battery_type',
        #          'battery_qty', 'manual_control', 'swivel_head', 'tilt_head', 'zoom', 'ttl', 'trigger_voltage', 'tags', 'image', 'image_attribution', 'image_attribution_link']
        #self.helper.layout = Layout(
        #    Fieldset('Summary',
        #             'manufacturer',
        #             'model',
        #             'disambiguation',
        #             AppendedText('guide_number', 'm'),
        #             'gn_info',
        #             AppendedText('trigger_voltage', 'V'),
        #             ),
        #    Fieldset('Features',
        #             'pc_sync',
        #             'hot_shoe',
        #             'light_stand',
        #             'manual_control',
        #             'swivel_head',
        #             'tilt_head',
        #             'zoom',
        #             'ttl',
        #             ),
        #    Fieldset('Power',
        #             'battery_powered',
        #             'battery_type',
        #             'battery_qty',
        #             ),
        #    Fieldset('Meta',
        #             'tags',
        #             'image',
        #             'image_attribution',
        #             'image_attribution_link',
        #             ),

def filmstock_edit(request, slug):
    return Form.edit(
        auto__instance=FilmStock.objects.get(slug=slug),
    )
        #fields = ['name', 'manufacturer', 'iso',
        #          'colour', 'panchromatic', 'process', 'tags']
        #self.helper.layout = Layout(
        #    Fieldset('Summary',
        #             'name',
        #             'manufacturer',
        #             'iso',
        #             ),
        #    Fieldset('Features',
        #             'colour',
        #             'panchromatic',
        #             'process',
        #             ),
        #    Fieldset('Meta',
        #             'tags',
        #             ),



def lensmodel_edit(request, slug):
    return Form.edit(
        auto__instance=LensModel.objects.get(slug=slug),
    )
        #fields = ['manufacturer', 'model', 'disambiguation', 'mount', 'purpose', 'introduced', 'discontinued', 'zoom', 'min_focal_length', 'max_focal_length', 'max_aperture', 'min_aperture', 'closest_focus', 'elements', 'groups', 'nominal_min_angle_diag', 'nominal_max_angle_diag', 'lens_type', 'image_circle', 'aperture_blades',
        #          'coating', 'autofocus', 'perspective_control', 'magnification', 'negative_size', 'weight', 'length', 'diameter', 'filter_thread', 'hood', 'shutter_model', 'notes', 'tags', 'link', 'image', 'image_attribution', 'image_attribution_link', 'diagram', 'diagram_attribution', 'diagram_attribution_link']
        #widgets = {
        #    ,
        #    'introduced': YearPickerInput(format='%Y'),
        #    'discontinued': YearPickerInput(format='%Y'),
        #}
        #self.helper.layout = Layout(
        #    Fieldset('Summary',
        #             'manufacturer',
        #             'model',
        #             'disambiguation',
        #             'mount',
        #             'purpose',
        #             'introduced',
        #             'discontinued',
        #             ),
        #    Fieldset('Optics',
        #             'zoom',
        #             AppendedText('min_focal_length', 'mm'),
        #             AppendedText('max_focal_length', 'mm'),
        #             PrependedText('max_aperture', 'f/'),
        #             PrependedText('min_aperture', 'f/'),
        #             AppendedText('closest_focus', 'm'),
        #             'elements',
        #             'groups',
        #             AppendedText('nominal_min_angle_diag', '&deg;'),
        #             AppendedText('nominal_max_angle_diag', '&deg;'),
        #             'lens_type',
        #             AppendedText('magnification', '&times;'),
        #             'negative_size',
        #             'aperture_blades',
        #             AppendedText('image_circle', 'mm'),
        #             'coating',
        #             'diagram',
        #             'diagram_attribution',
        #             'diagram_attribution_link',
        #             ),
        #    Fieldset('Features',
        #             'autofocus',
        #             'perspective_control',
        #             'hood',
        #             'shutter_model',
        #             ),
        #    Fieldset('Physical',
        #             AppendedText('weight', 'g'),
        #             AppendedText('length', 'mm'),
        #             AppendedText('diameter', 'mm'),
        #             AppendedText('filter_thread', 'mm'),
        #             ),
        #    Fieldset('Misc',
        #             'notes',
        #             'link',
        #             'image',
        #             'image_attribution',
        #             'image_attribution_link',
        #             ),
        #    Fieldset('Meta',
        #             'tags',
        #             ),

def process_edit(request, pk):
    return Form.edit(
        auto__instance=Process.objects.get(pk=pk),
    )
        #fields = ['name', 'colour', 'positive']
        #self.helper.layout = Layout(
        #    'name',
        #    'colour',
        #    'positive',

def filter_edit(request, pk):
    return Form.edit(
        auto__instance=Filter.objects.get(pk=pk),
    )
        #fields = ['type', 'shortname', 'attenuation', 'colour']
        #self.helper.layout = Layout(
        #    'type',
        #    'shortname',
        #    'attenuation',
        #    'colour',


def flash_edit(request, id_owner):
    return Form.edit(
        auto__instance=Flash.objects.get(id_owner=id_owner),
    )
        #fields = ['flashmodel', 'serial', 'own',
        #          'acquired', 'cost', 'lost', 'lost_price']
        #widgets = {
        #    'acquired': DatePickerInput(format='%Y-%m-%d'),
        #    'lost': DatePickerInput(format='%Y-%m-%d'),
        #}
        #self.helper.layout = Layout(
        #    Fieldset('Summary',
        #             'flashmodel',
        #             'serial',
        #             ),
        #    Fieldset('Ownership',
        #             'own',
        #             'acquired',
        #             'cost',
        #             'lost',
        #             'lost_price',
        #             ),

def teleconvertermodel_edit(request, slug):
    return Form.edit(
        auto__instance=TeleconverterModel.objects.get(slug=slug),
    )
       #fields = ['model', 'manufacturer', 'disambiguation', 'mount',
        #          'factor', 'elements', 'groups', 'multicoated', 'tags', 'image', 'image_attribution', 'image_attribution_link']#

        #self.helper.layout = Layout(
        #    Fieldset('Summary',
        #             'manufacturer',
        #             'model',
        #             'disambiguation'
        #             'mount',
        #             ),
        #    Fieldset('Optics',
        #             AppendedText('factor', '&times;'),
        #             'elements',
        #             'groups',
        #             'multicoated',
        #             ),
        #    Fieldset('Meta',
        #             'tags',
        #             'image',
        #             'image_attribution',
        #             'image_attribution_link',
        #             ),

def teleconverter_edit(request, id_owner):
    return Form.edit(
        auto__instance=Teleconverter.objects.get(id_owner=id_owner),
    )
        #fields = ['teleconvertermodel', 'serial', 'own',
        #          'acquired', 'cost', 'lost', 'lost_price', ]
        #widgets = {
        #    'acquired': DatePickerInput(format='%Y-%m-%d'),
        #    'lost': DatePickerInput(format='%Y-%m-%d'),
        #}
        #self.helper.layout = Layout(
        #    Fieldset('Summary',
        #             'teleconvertermodel',
        #             'serial',
        #             ),
        #    Fieldset('Ownership',
        #             'own',
        #             'acquired',
        #             'cost',
        #             'lost',
        #             'lost_price',
        #             ),

def enlarger_edit(request, id_owner):
    return Form.edit(
        auto__instance=Enlarger.objects.get(id_owner=id_owner),
    )
        #fields = ['enlargermodel', 'serial', 'own',
        #          'acquired', 'cost', 'lost', 'lost_price']
        #widgets = {
        #    'acquired': DatePickerInput(format='%Y-%m-%d'),
        #    'lost': DatePickerInput(format='%Y-%m-%d'),
        #}
        #self.helper.layout = Layout(
        #    Fieldset('Summary',
        #             'enlargermodel',
        #             'serial',
        #             ),
        #    Fieldset('Ownership',
        #             'own',
        #             'acquired',
        #             'cost',
        #             'lost',
        #             'lost_price',
        #             ),


def bulkfilm_edit(request, id_owner):
    return Form.edit(
        auto__instance=BulkFilm.objects.get(id_owner=id_owner),
    )
        #fields = ['format', 'filmstock', 'length', 'finished', 'purchase_date',
        #          'cost', 'source', 'batch', 'expiry']
        #widgets = {
        #    'purchase_date': DatePickerInput(format='%Y-%m-%d'),
        #    'expiry': MonthPickerInput(format='%Y-%m-01'),
        #}
        #self.helper.layout = Layout(
        #    Fieldset('Summary',
        #             'format',
        #             'filmstock',
        #             AppendedText('length', 'm'),
        #             'finished',
        #             'batch',
        #             'expiry',
        #             ),
        #    Fieldset('Ownership',
        #             'purchase_date',
        #             'cost',
        #             'source',
        #             ),

def camera_edit(request, id_owner):
    return Form.edit(
        auto__instance=Camera.objects.get(id_owner=id_owner),
    )
        #fields = ['cameramodel', 'acquired', 'cost', 'source', 'serial', 'datecode',
        #          'manufactured', 'own', 'notes', 'lost', 'lost_price', 'condition', 'condition_notes']
        #widgets = {
        #    'acquired': DatePickerInput(format='%Y-%m-%d'),
        #    'lost': DatePickerInput(format='%Y-%m-%d'),
        #}

        #self.helper.layout = Layout(
        #    Fieldset('Summary',
        #             'cameramodel',
        #             'serial',
        #             'datecode',
        #             'manufactured',
        #             'notes',
        #             'condition',
        #             'condition_notes',
        #             ),
        #    Fieldset('Ownership',
        #             'own',
        #             'acquired',
        #             'cost',
        #             'source',
        #             'lost',
        #             'lost_price',
        #             ),

def lens_edit(request, id_owner):
    return Form.edit(
        auto__instance=Lens.objects.get(id_owner=id_owner),
    )
        #fields = ['lensmodel', 'serial', 'date_code', 'manufactured', 'acquired', 'cost',
        #          'notes', 'own', 'lost', 'lost_price', 'source', 'condition', 'condition_notes']
        #widgets = {
        #    'acquired': DatePickerInput(format='%Y-%m-%d'),
        #    'lost': DatePickerInput(format='%Y-%m-%d'),
        #}
        #self.helper.layout = Layout(
        #    Fieldset('Summary',
        #             'lensmodel',
        #             'serial',
        #             'date_code',
        #             'manufactured',
        #             'notes',
        #             'condition',
        #             'condition_notes',
        #             ),
        #    Fieldset('Ownership',
        #             'own',
        #             'acquired',
        #             'cost',
        #             'source',
        #             'lost',
        #             'lost_price',
        #             ),


def mountadapter_edit(request, id_owner):
    return Form.edit(
        auto__instance=MountAdapter.objects.get(id_owner=id_owner),
    )
    #   fields = ['camera_mount', 'lens_mount',
    #              'has_optics', 'infinity_focus', 'notes']
    #    self.helper.layout = Layout(
    #        'camera_mount',
    #        'lens_mount',
    #        'has_optics',
    #        'infinity_focus',
    #        'notes',


def negativesize_edit(request, pk):
    return Form.edit(
        auto__instance=NegativeSize.objects.get(pk=pk),
    )
        #fields = [
        #    'name',
        #    'width',
        #    'height',
        #]
        #self.helper.layout = Layout(
        #    'name',
        #    AppendedText('width', 'mm'),
        #    AppendedText('height', 'mm'),
        #    FormActionButtons
        #)


def person_edit(request, id_owner):
    return Form.edit(
        auto__instance=Person.objects.get(id_owner=id_owner),
    )
       #fields = ['name', 'type']
       # self.helper.layout = Layout(
       #     'name',
       #     'type',

def scan_edit(request, uuid):
    return Form.edit(
        auto__instance=Scan.objects.get(uuid=uuid),
    )
        #fields = ['negative', 'print', 'filename', 'date']
        #widgets = {
        #    'date': DatePickerInput(format='%Y-%m-%d'),
        #}
        #self.fields['negative'].queryset = Negative.objects.filter(
        #    owner=get_current_user())
        #self.fields['print'].queryset = Print.objects.filter(
        #    owner=get_current_user())
        #self.helper = FormHelper(self)
        #self.helper.layout = Layout(
        #    'negative',
        #    'print',
        #    'filename',
        #    'date',

def negative_edit(request, slug):
    return Form.edit(
        auto__instance=Negative.objects.get(slug=slug),
    )
        #fields = ['film', 'frame', 'caption', 'date', 'lens', 'shutter_speed', 'aperture', 'filter', 'teleconverter', 'notes',
        #          'mount_adapter', 'focal_length', 'location', 'flash', 'metering_mode', 'exposure_program', 'photographer', 'copy_of']
        #widgets = {
        #    'date': DateTimePickerInput(format='%Y-%m-%d %H:%M', options={"sideBySide": True}),
        #}
        #self.fields['film'].queryset = Film.objects.filter(
        #    owner=get_current_user()).exclude(status='Available')
        #self.fields['lens'].queryset = Lens.objects.filter(
        #    owner=get_current_user())
        #self.fields['mount_adapter'].queryset = MountAdapter.objects.filter(
        #    owner=get_current_user())
        #self.fields['photographer'].queryset = Person.objects.filter(
        #    owner=get_current_user())
        #self.fields['copy_of'].queryset = Negative.objects.filter(
        #    owner=get_current_user())
        #self.helper.layout = Layout(
        #    Fieldset('Summary',
        #             'film',
        #             'frame',
        #             'caption',
        #             'date',
        #             ),
        #    Fieldset('Exposure',
        #             'lens',
        #             AppendedText('focal_length', 'mm'),
        #             'shutter_speed',
        #             PrependedText('aperture', 'f/'),
        #             'filter',
        #             'teleconverter',
        #             'mount_adapter',
        #             'flash',
        #             'metering_mode',
        #             'exposure_program',
        #             ),
        #    Fieldset('Misc',
        #             'photographer',
        #             'copy_of',
        #             'notes',
        #             'location',
        #             ),

def film_edit(request, id_owner):
    return Form.edit(
        auto__instance=Film.objects.get(id_owner=id_owner),
    )
        #fields = ['filmstock', 'exposed_at', 'format', 'status', 'date_loaded', 'date_processed', 'camera', 'title', 'frames', 'developer', 'developer_previous_uses', 'development_time',
        #          'development_temperature', 'development_compensation', 'development_notes', 'bulk_film', 'bulk_film_loaded', 'film_batch', 'expiry_date', 'purchase_date', 'price', 'processed_by', 'archive']
        #widgets = {
        #    'date_loaded': DatePickerInput(format='%Y-%m-%d'),
        #    'date_processed': DatePickerInput(format='%Y-%m-%d'),
        #    'purchase_date': DatePickerInput(format='%Y-%m-%d'),
        #    'bulk_film_loaded': DatePickerInput(format='%Y-%m-%d'),
        #    'expiry_date': MonthPickerInput(format='%Y-%m-01'),
        #    'dev_time': TimePickerInput(format='%H:%M:%S',
        #                                options={
        #                                    "useCurrent": False,
        #                                    "showTodayButton": False,
        #                                }),
        #}
        #self.fields['camera'].queryset = Camera.objects.filter(
        #    owner=get_current_user())
        #self.fields['bulk_film'].queryset = BulkFilm.objects.filter(
        #    owner=get_current_user())
        #self.fields['processed_by'].queryset = Person.objects.filter(
        #    owner=get_current_user())
        #self.fields['archive'].queryset = Archive.objects.filter(
        #    owner=get_current_user())
        #self.fields['bulk_film'].queryset = BulkFilm.objects.filter(
        #    owner=get_current_user(), finished=False)
        #self.helper = FormHelper(self)
        #self.helper.layout = Layout(
        #    Fieldset('Summary',
        #             'title',
        #             'status',
        #             ),
        #    Fieldset('Filmstock',
        #             'filmstock',
        #             'format',
        #             'bulk_film',
        #             'bulk_film_loaded',
        #             'film_batch',
        #             'expiry_date'
        #             ),
        #    Fieldset('Exposure',
        #             'camera',
        #             'date_loaded',
        #             'frames',
        #             'exposed_at',
        #             ),
        #    Fieldset('Development',
        #             'developer',
        #             'date_processed',
        #             'developer_previous_uses',
        #             'development_time',
        #             AppendedText('development_temperature', '&deg;C'),
        #             PrependedText('development_compensation', 'N'),
        #             'development_notes',
        #             'processed_by',
        #             ),
        #    Fieldset('Archive',
        #             'archive',
        #             ),
        #    Fieldset('Ownership',
        #             'purchase_date',
        #             'price',
        #             ),

def print_edit(request, id_owner):
    return Form.edit(
        auto__instance=Print.objects.get(id_owner=id_owner),
    )
        #fields = ['negative', 'date', 'paper_stock', 'height', 'width', 'aperture', 'exposure_time', 'filtration_grade', 'development_time',
        #          'toner', 'own', 'location', 'sold_price', 'enlarger', 'lens', 'developer', 'fine', 'notes', 'archive', 'printer']
        #widgets = {
        #    'date': DatePickerInput(format='%Y-%m-%d'),
        #}

        #self.fields['negative'].queryset = Negative.objects.filter(
        #    owner=get_current_user())
        #self.fields['enlarger'].queryset = Enlarger.objects.filter(
        #    owner=get_current_user())
        #self.fields['lens'].queryset = Lens.objects.filter(
        #    owner=get_current_user())
        #self.fields['archive'].queryset = Archive.objects.filter(
        #    owner=get_current_user(), type='Print', sealed=False)
        #self.fields['printer'].queryset = Person.objects.filter(
        #    owner=get_current_user())
        #self.helper.layout = Layout(
        #    Fieldset('Summary',
        #             'negative',
        #             'date',
        #             'paper_stock',
        #             AppendedText('width', '"'),
        #             AppendedText('height', '"'),
        #             'fine',
        #             ),
        #    Fieldset('Exposure',
        #             'enlarger',
        #             'lens',
        #             PrependedText('aperture', 'f/'),
        #             'exposure_time',
        #             'filtration_grade',
        #             ),
        #    Fieldset('Development',
        #             'developer',
        #             'development_time',
        #             'toner',
        #             'notes',
        #             'printer',
        #             ),
        #    Fieldset('Ownership',
        #             'own',
        #             'location',
        #             'sold_price',
        #             'archive',
        #             ),

def toner_edit(request, slug):
    return Form.edit(
        auto__instance=Toner.objects.get(slug=slug),
    )
        #fields = [
        #    'name',
        #    'manufacturer',
        #    'formulation',
        #    'stock_dilution',
        #    'tags',
        #]
        #self.helper.layout = Layout(
        #    Fieldset('Summary',
        #             'name',
        #             'manufacturer',
        #             'formulation',
        #             'stock_dilution',
        #             ),
        #    Fieldset('Meta',
        #             'tags',
        #             ),

#class CameraSellForm(ModelForm):
#    class Meta:
#        model = Camera
#        fields = ['lost', 'lost_price', 'own']
#        widgets = {
#            'lost': DatePickerInput(format='%Y-%m-%d'),
#        }

#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        self.helper = FormHelper(self)
#        self.helper.layout = Layout(
#            Div(
#                Hidden('own', False),
#                'lost',
#                'lost_price',
#            ),
#            FormActionButtons
#        )

#class LensSellForm(ModelForm):
#    class Meta:
#        model = Lens
#        fields = ['own', 'lost', 'lost_price']
#        widgets = {
#            'lost': DatePickerInput(format='%Y-%m-%d'),
#        }

#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        self.helper = FormHelper(self)
#        self.helper.layout = Layout(
#            Div(
#                Hidden('own', False),
#                'lost',
#                'lost_price',
#            ),
#            FormActionButtons
#        )


#class PrintArchiveForm(ModelForm):
#    class Meta:
#        model = Print
#        fields = ['archive']

#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        self.fields['archive'].queryset = Archive.objects.filter(type='Print', owner=get_current_user(), sealed=False)
#        self.helper = FormHelper(self)
#        self.helper.layout = Layout(
#            Fieldset('Archive this print',
#                     'archive',
#                     ),
#            Hidden('status', 'Archived'),
#            FormActionButtons
#        )

#class PrintSellForm(ModelForm):
#    class Meta:
#        model = Print
#        fields = ['location', 'sold_price', 'own', 'archive']

#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        self.helper = FormHelper(self)
#        self.helper.layout = Layout(
#            Fieldset('Sell this print',
#                     'location',
#                     'sold_price',
#                     ),
#            #Hidden('status', 'Sold'),
#            Hidden('own', False),
#            Hidden('archive', None),
#            FormActionButtons
#        )


#class FilmAddForm(ModelForm):
#    class Meta:
#        model = Film
#        fields = ['filmstock', 'format', 'frames', 'film_batch', 'expiry_date',
#                  'purchase_date', 'price', 'bulk_film', 'bulk_film_loaded', 'status']
#        widgets = {
#            'purchase_date': DatePickerInput(format='%Y-%m-%d'),
#            'expiry_date': MonthPickerInput(format='%Y-%m-01'),
#            'bulk_film_loaded': DatePickerInput(format='%Y-%m-%d'),
#        }

#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        self.fields['bulk_film'].queryset = BulkFilm.objects.filter(
#            owner=get_current_user(), finished=False)
#        self.helper = FormHelper(self)
#        self.helper.layout = Layout(
#            Fieldset('Add a new film to your collection',
#                     'filmstock',
#                     'format',
#                     'frames',
#                     Div(
#                         TabHolder(
#                             Tab('Single film',
#                                 HTML(
#                                     "<p>Choose Single Film for regular roll or sheet films</p>"),
#                                 'film_batch',
#                                 'expiry_date',
#                                 'purchase_date',
#                                 'price',
#                                 ),
 #                            Tab('Bulk film',
#                                 HTML(
#                                     "<p>Choose Bulk Film for film that has been cut from a bulk roll</p>"),
#                                 'bulk_film',
#                                 'bulk_film_loaded',
#                                 ),
#                         ),
#                         css_class="border",
#                     ),
#                     ),
#            Hidden('status', 'Available'),
#            FormActionButtons
#        )

#class FilmLoadForm(ModelForm):
#    class Meta:
#        model = Film
#        fields = ['camera', 'title', 'exposed_at',
#                  'date_loaded', 'frames', 'status']
#        widgets = {
#            'date_loaded': DatePickerInput(format='%Y-%m-%d'),
#        }

#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        self.fields['camera'].queryset = Camera.objects.filter(
#            owner=get_current_user(), cameramodel__format=self.instance.format)
#        self.helper = FormHelper(self)
#        self.helper.layout = Layout(
#            Fieldset('Load this film into a camera',
#                     'camera',
#                     'title',
#                     'exposed_at',
#                     'date_loaded',
#                     'frames',
#                     ),
#            Hidden('status', 'Loaded'),
#            FormActionButtons
#        )


#class FilmDevelopForm(ModelForm):
#    class Meta:
#        model = Film
#        fields = ['date_processed', 'developer', 'developer_previous_uses', 'development_time',
#                  'development_temperature', 'development_compensation', 'development_notes', 'processed_by', 'status']
#        widgets = {
#            'date_processed': DatePickerInput(format='%Y-%m-%d'),
#            'dev_time': TimePickerInput(format='%H:%M:%S',
#                                        options={
#                                            "useCurrent": False,
#                                            "showTodayButton": False,
#                                        }),
#        }

#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        self.fields['processed_by'].queryset = Person.objects.filter(
#            owner=get_current_user())
#        self.helper = FormHelper(self)
#        self.helper.layout = Layout(
#            Fieldset('Develop this film',
#                     'date_processed',
#                     'developer',
#                     'developer_previous_uses',
#                     'development_time',
#                     AppendedText('development_temperature', '&deg;C'),
#                     PrependedText('development_compensation', 'N'),
#                     'development_notes',
#                     'processed_by',
#                     ),
#            Hidden('status', 'Developed'),
#            FormActionButtons
#        )


#class FilmArchiveForm(ModelForm):
#    class Meta:
#        model = Film
#        fields = ['archive', 'status']

#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        self.fields['archive'].queryset = Archive.objects.filter(
#            Q(type='Negative') | Q(type='Slide'), owner=get_current_user(), sealed=False)
#        self.helper = FormHelper(self)
#        self.helper.layout = Layout(
#            Fieldset('Archive this film',
#                     'archive',
#                     ),
#            Hidden('status', 'Archived'),
#            FormActionButtons
#        )
