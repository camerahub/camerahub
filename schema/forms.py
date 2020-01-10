from django.forms import ModelForm

from .models import Accessory, Archive, Battery, BulkFilm, Camera, CameraModel, Developer, Enlarger, FilmStock, Filter
from .models import Flash, FlashProtocol, Format, Lens, LensModel, Manufacturer
from .models import Mount, MountAdapter, NegativeSize, Order, PaperStock, Person, Print, Toning
from .models import Process, Repair, Scan, Negative, Film, Series, ShutterSpeed, Teleconverter, Toner

class AccessoryForm(ModelForm):
    class Meta:
        model = Accessory
        fields = '__all__'

class ArchiveForm(ModelForm):
    class Meta:
        model = Archive
        fields = '__all__'

class BatteryForm(ModelForm):
    class Meta:
        model = Battery
        fields = '__all__'

class BulkFilmForm(ModelForm):
    class Meta:
        model = BulkFilm
        fields = '__all__'

class CameraForm(ModelForm):
    class Meta:
        model = Camera
        fields = '__all__'

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

class FilmStockForm(ModelForm):
    class Meta:
        model = FilmStock
        fields = '__all__'

class FilterForm(ModelForm):
    class Meta:
        model = Filter
        fields = '__all__'

class FlashForm(ModelForm):
    class Meta:
        model = Flash
        fields = '__all__'

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

class NegativeSizeForm(ModelForm):
    class Meta:
        model = NegativeSize
        fields = '__all__'

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class PaperStockForm(ModelForm):
    class Meta:
        model = PaperStock
        fields = '__all__'

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

class PrintForm(ModelForm):
    class Meta:
        model = Print
        fields = '__all__'

class ProcessForm(ModelForm):
    class Meta:
        model = Process
        fields = '__all__'

class RepairForm(ModelForm):
    class Meta:
        model = Repair
        fields = '__all__'

class ScanForm(ModelForm):
    class Meta:
        model = Scan
        fields = '__all__'

class NegativeForm(ModelForm):
    class Meta:
        model = Negative
        fields = '__all__'

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = '__all__'

class SeriesForm(ModelForm):
    class Meta:
        model = Series
        fields = '__all__'

class TeleconverterForm(ModelForm):
    class Meta:
        model = Teleconverter
        fields = '__all__'

class TonerForm(ModelForm):
    class Meta:
        model = Toner
        fields = '__all__'