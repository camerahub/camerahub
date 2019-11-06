import django_tables2 as tables
from django.utils.html import format_html

# Import all models that need admin pages
from .models import Accessory, Archive, Battery, BulkFilm, Camera, CameraModel, Developer, Enlarger, FilmStock, Filter
from .models import Flash, FlashProtocol, Format, Lens, LensModel, Manufacturer
from .models import MeteringType, Mount, MountAdapter, NegativeSize, Order, PaperStock, Person, Print, Toning
from .models import Process, Repair, Scan, Negative, Film, Series, ShutterSpeed, Teleconverter, Toner

#sequence – reorder columns
#fields – specify model fields to include
#exclude – specify model fields to exclude

class AccessoryTable(tables.Table):
    class Meta:
        model = Accessory
        exclude = ('id', 'cost_currency', 'lost', 'lost_price', 'lost_price_currency', 'owner',)

class ArchiveTable(tables.Table):
    class Meta:
        model = Archive
        exclude = ('id', 'owner',)

class BatteryTable(tables.Table):
    class Meta:
        model = Battery

class BulkFilmTable(tables.Table):
    class Meta:
        model = BulkFilm
        exclude = ('cost_currency', 'owner',)

class CameraTable(tables.Table):
    class Meta:
        model = Camera
        exclude = ('condition', 'cost_currency', 'lost', 'lost_price_currency', 'lost_price', 'owner',)

class CameraModelTable(tables.Table):
    class Meta:
        model = CameraModel
        exclude = ('manufacturer',)
    def render_model(self, value, record):
        return format_html("{} {}", record.manufacturer, value)

class DeveloperTable(tables.Table):
    class Meta:
        model = Developer
        exclude = ('id',)

class EnlargerTable(tables.Table):
    class Meta:
        model = Enlarger
        exclude = ('id', 'lost', 'cost_currency', 'lost_price_currency', 'lost_price', 'owner')

class FilmStockTable(tables.Table):
    class Meta:
        model = FilmStock
        exclude = ('id',)

class FilterTable(tables.Table):
    class Meta:
        model = Filter
        exclude = ('id', 'owner',)

class FlashTable(tables.Table):
    class Meta:
        model = Flash

class FlashProtocolTable(tables.Table):
    class Meta:
        model = FlashProtocol

class FormatTable(tables.Table):
    class Meta:
        model = Format

class LensTable(tables.Table):
    class Meta:
        model = Lens

class LensModelTable(tables.Table):
    class Meta:
        model = LensModel

class ManufacturerTable(tables.Table):
    class Meta:
        model = Manufacturer

class MeteringTypeTable(tables.Table):
    class Meta:
        model = MeteringType

class MountTable(tables.Table):
    class Meta:
        model = Mount

class MountAdapterTable(tables.Table):
    class Meta:
        model = MountAdapter

class NegativeSizeTable(tables.Table):
    class Meta:
        model = NegativeSize

class OrderTable(tables.Table):
    class Meta:
        model = Order

class PaperStockTable(tables.Table):
    class Meta:
        model = PaperStock

class PersonTable(tables.Table):
    class Meta:
        model = Person

class PrintTable(tables.Table):
    class Meta:
        model = Print

class ToningTable(tables.Table):
    class Meta:
        model = Toning

class ProcessTable(tables.Table):
    class Meta:
        model = Process

class RepairTable(tables.Table):
    class Meta:
        model = Repair

class ScanTable(tables.Table):
    class Meta:
        model = Scan

class NegativeTable(tables.Table):
    class Meta:
        model = Negative

class FilmTable(tables.Table):
    class Meta:
        model = Film

class SeriesTable(tables.Table):
    class Meta:
        model = Series

class ShutterSpeedTable(tables.Table):
    class Meta:
        model = ShutterSpeed

class TeleconverterTable(tables.Table):
    class Meta:
        model = Teleconverter

class TonerTable(tables.Table):
    class Meta:
        model = Toner