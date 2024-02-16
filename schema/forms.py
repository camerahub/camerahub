import sys
from django.forms import ModelForm
from django.db.models import Q
from django_currentuser.middleware import get_current_user
from bootstrap_datepicker_plus.widgets import DatePickerInput, DateTimePickerInput, YearPickerInput, MonthPickerInput, TimePickerInput

from schema.models import Accessory, Archive, Battery, BulkFilm, Camera, CameraModel, Developer, Enlarger, EnlargerModel, FilmStock, Filter
from schema.models import Flash, FlashModel, Format, Lens, LensModel, Manufacturer
from schema.models import Mount, MountAdapter, NegativeSize, PaperStock, Person, Print
from schema.models import Process, Scan, Negative, Film, Teleconverter, TeleconverterModel, Toner


class CameraSellForm(ModelForm):
    class Meta:
        model = Camera
        fields = ['lost', 'lost_price', 'own']
        widgets = {
            'lost': DatePickerInput(format='%Y-%m-%d'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                Hidden('own', False),
                'lost',
                'lost_price',
            ),
            FormActionButtons
        )

class LensSellForm(ModelForm):
    class Meta:
        model = Lens
        fields = ['own', 'lost', 'lost_price']
        widgets = {
            'lost': DatePickerInput(format='%Y-%m-%d'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                Hidden('own', False),
                'lost',
                'lost_price',
            ),
            FormActionButtons
        )


class PrintArchiveForm(ModelForm):
    class Meta:
        model = Print
        fields = ['archive']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['archive'].queryset = Archive.objects.filter(type='Print', owner=get_current_user(), sealed=False)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Fieldset('Archive this print',
                     'archive',
                     ),
            Hidden('status', 'Archived'),
            FormActionButtons
        )

class PrintSellForm(ModelForm):
    class Meta:
        model = Print
        fields = ['location', 'sold_price', 'own', 'archive']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Fieldset('Sell this print',
                     'location',
                     'sold_price',
                     ),
            #Hidden('status', 'Sold'),
            Hidden('own', False),
            Hidden('archive', None),
            FormActionButtons
        )


class FilmAddForm(ModelForm):
    class Meta:
        model = Film
        fields = ['filmstock', 'format', 'frames', 'film_batch', 'expiry_date',
                  'purchase_date', 'price', 'bulk_film', 'bulk_film_loaded', 'status']
        widgets = {
            'purchase_date': DatePickerInput(format='%Y-%m-%d'),
            'expiry_date': MonthPickerInput(format='%Y-%m-01'),
            'bulk_film_loaded': DatePickerInput(format='%Y-%m-%d'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bulk_film'].queryset = BulkFilm.objects.filter(
            owner=get_current_user(), finished=False)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Fieldset('Add a new film to your collection',
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
            FormActionButtons
        )


class FilmLoadForm(ModelForm):
    class Meta:
        model = Film
        fields = ['camera', 'title', 'exposed_at',
                  'date_loaded', 'frames', 'status']
        widgets = {
            'date_loaded': DatePickerInput(format='%Y-%m-%d'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['camera'].queryset = Camera.objects.filter(
            owner=get_current_user(), cameramodel__format=self.instance.format)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Fieldset('Load this film into a camera',
                     'camera',
                     'title',
                     'exposed_at',
                     'date_loaded',
                     'frames',
                     ),
            Hidden('status', 'Loaded'),
            FormActionButtons
        )


class FilmDevelopForm(ModelForm):
    class Meta:
        model = Film
        fields = ['date_processed', 'developer', 'developer_previous_uses', 'development_time',
                  'development_temperature', 'development_compensation', 'development_notes', 'processed_by', 'status']
        widgets = {
            'date_processed': DatePickerInput(format='%Y-%m-%d'),
            'dev_time': TimePickerInput(format='%H:%M:%S',
                                        options={
                                            "useCurrent": False,
                                            "showTodayButton": False,
                                        }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['processed_by'].queryset = Person.objects.filter(
            owner=get_current_user())
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Fieldset('Develop this film',
                     'date_processed',
                     'developer',
                     'developer_previous_uses',
                     'development_time',
                     AppendedText('development_temperature', '&deg;C'),
                     PrependedText('development_compensation', 'N'),
                     'development_notes',
                     'processed_by',
                     ),
            Hidden('status', 'Developed'),
            FormActionButtons
        )


class FilmArchiveForm(ModelForm):
    class Meta:
        model = Film
        fields = ['archive', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['archive'].queryset = Archive.objects.filter(
            Q(type='Negative') | Q(type='Slide'), owner=get_current_user(), sealed=False)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Fieldset('Archive this film',
                     'archive',
                     ),
            Hidden('status', 'Archived'),
            FormActionButtons
        )
