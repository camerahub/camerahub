from django.forms import ModelForm
from django import forms
from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)

from .models import Accessory, Archive, Battery, BulkFilm, Camera, CameraModel, Developer, Enlarger, FilmStock, Filter
from .models import Flash, FlashProtocol, Format, Lens, LensModel, Manufacturer
from .models import Mount, MountAdapter, NegativeSize, Order, PaperStock, Person, Print, Toning
from .models import Process, Repair, Scan, Negative, Film, Series, ShutterSpeed, Teleconverter, Toner

class AccessoryForm(ModelForm):
    class Meta:
        model = Accessory
        fields = '__all__'
        exclude = ['owner']

class ArchiveForm(ModelForm):
    class Meta:
        model = Archive
        fields = '__all__'
        exclude = ['owner']

class BatteryForm(ModelForm):
    class Meta:
        model = Battery
        fields = '__all__'

class BulkFilmForm(ModelForm):
    class Meta:
        model = BulkFilm
        fields = '__all__'
        exclude = ['owner']

class CameraForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CameraForm, self).__init__(*args, **kwargs)
        self.fields['lens'].queryset = Lens.objects.filter(owner = get_current_user())
        self.fields['display_lens'].queryset = Lens.objects.filter(owner = get_current_user())
    class Meta:
        model = Camera
        fields = '__all__'
        exclude = ['owner']

class CameraModelForm(ModelForm):
    class Meta:
        model = CameraModel
        fields = '__all__'

class DeveloperForm(ModelForm):
    class Meta:
        model = Developer
        fields = '__all__'

class EnlargerForm(ModelForm):
    class Meta:
        model = Enlarger
        fields = '__all__'
        exclude = ['owner']

class FilmStockForm(ModelForm):
    class Meta:
        model = FilmStock
        fields = '__all__'
        exclude = ['owner']

class FilterForm(ModelForm):
    class Meta:
        model = Filter
        fields = '__all__'
        exclude = ['owner']

class FlashForm(ModelForm):
    class Meta:
        model = Flash
        fields = '__all__'
        exclude = ['owner']

class FlashProtocolForm(ModelForm):
    class Meta:
        model = FlashProtocol
        fields = '__all__'

class FormatForm(ModelForm):
    class Meta:
        model = Format
        fields = '__all__'

class LensForm(ModelForm):
    class Meta:
        model = Lens
        fields = '__all__'
        exclude = ['owner']

class LensModelForm(ModelForm):
    class Meta:
        model = LensModel
        fields = '__all__'

class ManufacturerForm(ModelForm):
    class Meta:
        model = Manufacturer
        fields = '__all__'

class MountForm(ModelForm):
    class Meta:
        model = Mount
        fields = '__all__'

class MountAdapterForm(ModelForm):
    class Meta:
        model = MountAdapter
        fields = '__all__'
        exclude = ['owner']

class NegativeSizeForm(ModelForm):
    class Meta:
        model = NegativeSize
        fields = '__all__'

class OrderForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['negative'].queryset = Negative.objects.filter(owner = get_current_user())
        self.fields['print'].queryset = Print.objects.filter(owner = get_current_user())
        self.fields['recipient'].queryset = Person.objects.filter(owner = get_current_user())
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['owner']

class PaperStockForm(ModelForm):
    class Meta:
        model = PaperStock
        fields = '__all__'

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        exclude = ['owner']

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
        fields = '__all__'
        exclude = ['owner']

class ProcessForm(ModelForm):
    class Meta:
        model = Process
        fields = '__all__'

class RepairForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RepairForm, self).__init__(*args, **kwargs)
        self.fields['camera'].queryset = Camera.objects.filter(owner = get_current_user())
        self.fields['lens'].queryset = Lens.objects.filter(owner = get_current_user())
    class Meta:
        model = Repair
        fields = '__all__'
        exclude = ['owner']

class ScanForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ScanForm, self).__init__(*args, **kwargs)
        self.fields['negative'].queryset = Negative.objects.filter(owner = get_current_user())
        self.fields['print'].queryset = Print.objects.filter(owner = get_current_user())
    class Meta:
        model = Scan
        fields = '__all__'
        exclude = ['owner']

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
        fields = '__all__'
        exclude = ['owner']

class FilmForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FilmForm, self).__init__(*args, **kwargs)
        self.fields['camera'].queryset = Camera.objects.filter(owner = get_current_user())
        self.fields['bulk_film'].queryset = BulkFilm.objects.filter(owner = get_current_user())
        self.fields['processed_by'].queryset = Person.objects.filter(owner = get_current_user())
        self.fields['archive'].queryset = Archive.objects.filter(owner = get_current_user())
    class Meta:
        model = Film
        fields = '__all__'

class SeriesForm(ModelForm):
    class Meta:
        model = Series
        fields = '__all__'
        exclude = ['owner']

class TeleconverterForm(ModelForm):
    class Meta:
        model = Teleconverter
        fields = '__all__'
        exclude = ['owner']

class TonerForm(ModelForm):
    class Meta:
        model = Toner
        fields = '__all__'