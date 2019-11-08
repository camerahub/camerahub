from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django_tables2 import SingleTableView

def index(request):
    return render(request, 'schema/index.html')

from .models import Accessory, Archive, Battery, BulkFilm, Camera, CameraModel, Developer, Enlarger, FilmStock, Filter
from .models import Flash, FlashProtocol, Format, Lens, LensModel, Manufacturer
from .models import Mount, MountAdapter, NegativeSize, Order, PaperStock, Person, Print, Toning
from .models import Process, Repair, Scan, Negative, Film, Series, ShutterSpeed, Teleconverter, Toner

from .tables import AccessoryTable, ArchiveTable, BatteryTable, BulkFilmTable, CameraTable, CameraModelTable, DeveloperTable, EnlargerTable, FilmStockTable, FilterTable
from .tables import FlashTable, FlashProtocolTable, FormatTable, LensTable, LensModelTable, ManufacturerTable
from .tables import MountTable, MountAdapterTable, NegativeSizeTable, OrderTable, PaperStockTable, PersonTable, PrintTable, ToningTable
from .tables import ProcessTable, RepairTable, ScanTable, NegativeTable, FilmTable, SeriesTable, ShutterSpeedTable, TeleconverterTable, TonerTable

# Custom class for displaying a list view in table format
class SingleTableListView(SingleTableView):
  template_name = 'schema/list.html'

class AccessoryList(SingleTableListView):
  model = Accessory
  table_class = AccessoryTable

class AccessoryDetail(generic.DetailView):
  model = Accessory

class AccessoryCreate(CreateView):
  model = Accessory
  fields = '__all__'
  template_name = 'schema/create.html'

class AccessoryUpdate(UpdateView):
  model = Accessory
  fields = '__all__'
  template_name = 'schema/update.html'


class ArchiveList(SingleTableListView):
  model = Archive
  table_class = ArchiveTable

class ArchiveDetail(generic.DetailView):
  model = Archive

class ArchiveCreate(CreateView):
  model = Archive
  fields = '__all__'
  template_name = 'schema/create.html'

class ArchiveUpdate(UpdateView):
  model = Archive
  fields = '__all__'
  template_name = 'schema/update.html'


class BatteryList(SingleTableListView):
  model = Battery
  table_class = BatteryTable

class BatteryDetail(generic.DetailView):
  model = Battery

class BatteryCreate(CreateView):
  model = Battery
  fields = '__all__'
  template_name = 'schema/create.html'

class BatteryUpdate(UpdateView):
  model = Battery
  fields = '__all__'
  template_name = 'schema/update.html'


class BulkFilmList(SingleTableListView):
  model = BulkFilm
  table_class = BulkFilmTable

class BulkFilmDetail(generic.DetailView):
  model = BulkFilm

class BulkFilmCreate(CreateView):
  model = BulkFilm
  fields = '__all__'
  template_name = 'schema/create.html'

class BulkFilmUpdate(UpdateView):
  model = BulkFilm
  fields = '__all__'
  template_name = 'schema/update.html'


class CameraList(SingleTableListView):
  model = Camera
  table_class = CameraTable

class CameraDetail(generic.DetailView):
  model = Camera

class CameraCreate(CreateView):
  model = Camera
  fields = '__all__'
  template_name = 'schema/create.html'

class CameraUpdate(UpdateView):
  model = Camera
  fields = '__all__'
  template_name = 'schema/update.html'

class CameraModelList(SingleTableListView):
  model = CameraModel
  table_class = CameraModelTable

class CameraModelDetail(generic.DetailView):
  model = CameraModel

class CameraModelCreate(CreateView):
  model = CameraModel
  fields = '__all__'
  template_name = 'schema/create.html'

class CameraModelUpdate(UpdateView):
  model = CameraModel
  fields = '__all__'
  template_name = 'schema/update.html'


class DeveloperList(SingleTableListView):
  model = Developer
  table_class = DeveloperTable

class DeveloperDetail(generic.DetailView):
  model = Developer

class DeveloperCreate(CreateView):
  model = Developer
  fields = '__all__'
  template_name = 'schema/create.html'

class DeveloperUpdate(UpdateView):
  model = Developer
  fields = '__all__'
  template_name = 'schema/update.html'


class EnlargerList(SingleTableListView):
  model = Enlarger
  table_class = EnlargerTable

class EnlargerDetail(generic.DetailView):
  model = Enlarger

class EnlargerCreate(CreateView):
  model = Enlarger
  fields = '__all__'
  template_name = 'schema/create.html'

class EnlargerUpdate(UpdateView):
  model = Enlarger
  fields = '__all__'
  template_name = 'schema/update.html'


class FilmStockList(SingleTableListView):
  model = FilmStock
  table_class = FilmStockTable

class FilmStockDetail(generic.DetailView):
  model = FilmStock

class FilmStockCreate(CreateView):
  model = FilmStock
  fields = '__all__'
  template_name = 'schema/create.html'

class FilmStockUpdate(UpdateView):
  model = FilmStock
  fields = '__all__'
  template_name = 'schema/update.html'


class FilterList(SingleTableListView):
  model = Filter
  table_class = FilterTable

class FilterDetail(generic.DetailView):
  model = Filter

class FilterCreate(CreateView):
  model = Filter
  fields = '__all__'
  template_name = 'schema/create.html'

class FilterUpdate(UpdateView):
  model = Filter
  fields = '__all__'
  template_name = 'schema/update.html'


class FlashList(SingleTableListView):
  model = Flash
  table_class = FlashTable

class FlashDetail(generic.DetailView):
  model = Flash

class FlashCreate(CreateView):
  model = Flash
  fields = '__all__'
  template_name = 'schema/create.html'

class FlashUpdate(UpdateView):
  model = Flash
  fields = '__all__'
  template_name = 'schema/update.html'


class FlashProtocolList(SingleTableListView):
  model = FlashProtocol
  table_class = FlashProtocolTable

class FlashProtocolDetail(generic.DetailView):
  model = FlashProtocol

class FlashProtocolCreate(CreateView):
  model = FlashProtocol
  fields = '__all__'
  template_name = 'schema/create.html'

class FlashProtocolUpdate(UpdateView):
  model = FlashProtocol
  fields = '__all__'
  template_name = 'schema/update.html'


class FormatList(SingleTableListView):
  model = Format
  table_class = FormatTable

class FormatDetail(generic.DetailView):
  model = Format

class FormatCreate(CreateView):
  model = Format
  fields = '__all__'
  template_name = 'schema/create.html'

class FormatUpdate(UpdateView):
  model = Format
  fields = '__all__'
  template_name = 'schema/update.html'


class LensList(SingleTableListView):
  model = Lens
  table_class = LensTable

class LensDetail(generic.DetailView):
  model = Lens

class LensCreate(CreateView):
  model = Lens
  fields = '__all__'
  template_name = 'schema/create.html'

class LensUpdate(UpdateView):
  model = Lens
  fields = '__all__'
  template_name = 'schema/update.html'


class LensModelList(SingleTableListView):
  model = LensModel
  table_class = LensModelTable

class LensModelDetail(generic.DetailView):
  model = LensModel

class LensModelCreate(CreateView):
  model = LensModel
  fields = '__all__'
  template_name = 'schema/create.html'

class LensModelUpdate(UpdateView):
  model = LensModel
  fields = '__all__'
  template_name = 'schema/update.html'


class ManufacturerList(SingleTableListView):
  model = Manufacturer
  table_class = ManufacturerTable

class ManufacturerDetail(generic.DetailView):
  model = Manufacturer

class ManufacturerCreate(CreateView):
  model = Manufacturer
  fields = '__all__'
  template_name = 'schema/create.html'

class ManufacturerUpdate(UpdateView):
  model = Manufacturer
  fields = '__all__'
  template_name = 'schema/update.html'


class MountList(SingleTableListView):
  model = Mount
  table_class = MountTable

class MountDetail(generic.DetailView):
  model = Mount

class MountCreate(CreateView):
  model = Mount
  fields = '__all__'
  template_name = 'schema/create.html'

class MountUpdate(UpdateView):
  model = Mount
  fields = '__all__'
  template_name = 'schema/update.html'


class MountAdapterList(SingleTableListView):
  model = MountAdapter
  table_class = MountAdapterTable

class MountAdapterDetail(generic.DetailView):
  model = MountAdapter

class MountAdapterCreate(CreateView):
  model = MountAdapter
  fields = '__all__'
  template_name = 'schema/create.html'

class MountAdapterUpdate(UpdateView):
  model = MountAdapter
  fields = '__all__'
  template_name = 'schema/update.html'


class NegativeSizeList(SingleTableListView):
  model = NegativeSize
  table_class = NegativeSizeTable

class NegativeSizeDetail(generic.DetailView):
  model = NegativeSize

class NegativeSizeCreate(CreateView):
  model = NegativeSize
  fields = '__all__'
  template_name = 'schema/create.html'

class NegativeSizeUpdate(UpdateView):
  model = NegativeSize
  fields = '__all__'
  template_name = 'schema/update.html'


class OrderList(SingleTableListView):
  model = Order
  table_class = OrderTable

class OrderDetail(generic.DetailView):
  model = Order

class OrderCreate(CreateView):
  model = Order
  fields = '__all__'
  template_name = 'schema/create.html'

class OrderUpdate(UpdateView):
  model = Order
  fields = '__all__'
  template_name = 'schema/update.html'


class PaperStockList(SingleTableListView):
  model = PaperStock
  table_class = PaperStockTable

class PaperStockDetail(generic.DetailView):
  model = PaperStock

class PaperStockCreate(CreateView):
  model = PaperStock
  fields = '__all__'
  template_name = 'schema/create.html'

class PaperStockUpdate(UpdateView):
  model = PaperStock
  fields = '__all__'
  template_name = 'schema/update.html'


class PersonList(SingleTableListView):
  model = Person
  table_class = PersonTable

class PersonDetail(generic.DetailView):
  model = Person

class PersonCreate(CreateView):
  model = Person
  fields = '__all__'
  template_name = 'schema/create.html'

class PersonUpdate(UpdateView):
  model = Person
  fields = '__all__'
  template_name = 'schema/update.html'


class PrintList(SingleTableListView):
  model = Print
  table_class = PrintTable

class PrintDetail(generic.DetailView):
  model = Print

class PrintCreate(CreateView):
  model = Print
  fields = '__all__'
  template_name = 'schema/create.html'

class PrintUpdate(UpdateView):
  model = Print
  fields = '__all__'
  template_name = 'schema/update.html'


class ProcessList(SingleTableListView):
  model = Process
  table_class = ProcessTable

class ProcessDetail(generic.DetailView):
  model = Process

class ProcessCreate(CreateView):
  model = Process
  fields = '__all__'
  template_name = 'schema/create.html'

class ProcessUpdate(UpdateView):
  model = Process
  fields = '__all__'
  template_name = 'schema/update.html'


class RepairList(SingleTableListView):
  model = Repair
  table_class = RepairTable

class RepairDetail(generic.DetailView):
  model = Repair

class RepairCreate(CreateView):
  model = Repair
  fields = '__all__'
  template_name = 'schema/create.html'

class RepairUpdate(UpdateView):
  model = Repair
  fields = '__all__'
  template_name = 'schema/update.html'


class ScanList(SingleTableListView):
  model = Scan
  table_class = ScanTable

class ScanDetail(generic.DetailView):
  model = Scan

class ScanCreate(CreateView):
  model = Scan
  fields = '__all__'
  template_name = 'schema/create.html'

class ScanUpdate(UpdateView):
  model = Scan
  fields = '__all__'
  template_name = 'schema/update.html'


class NegativeList(SingleTableListView):
  model = Negative
  table_class = NegativeTable

class NegativeDetail(generic.DetailView):
  model = Negative

class NegativeCreate(CreateView):
  model = Negative
  fields = '__all__'
  template_name = 'schema/create.html'

class NegativeUpdate(UpdateView):
  model = Negative
  fields = '__all__'
  template_name = 'schema/update.html'


class FilmList(SingleTableListView):
  model = Film
  table_class = FilmTable

class FilmDetail(generic.DetailView):
  model = Film

class FilmCreate(CreateView):
  model = Film
  fields = '__all__'
  template_name = 'schema/create.html'

class FilmUpdate(UpdateView):
  model = Film
  fields = '__all__'
  template_name = 'schema/update.html'


class SeriesList(SingleTableListView):
  model = Series
  table_class = SeriesTable

class SeriesDetail(generic.DetailView):
  model = Series

class SeriesCreate(CreateView):
  model = Series
  fields = '__all__'
  template_name = 'schema/create.html'

class SeriesUpdate(UpdateView):
  model = Series
  fields = '__all__'
  template_name = 'schema/update.html'


class TeleconverterList(SingleTableListView):
  model = Teleconverter
  table_class = TeleconverterTable

class TeleconverterDetail(generic.DetailView):
  model = Teleconverter

class TeleconverterCreate(CreateView):
  model = Teleconverter
  fields = '__all__'
  template_name = 'schema/create.html'

class TeleconverterUpdate(UpdateView):
  model = Teleconverter
  fields = '__all__'
  template_name = 'schema/update.html'


class TonerList(SingleTableListView):
  model = Toner
  table_class = TonerTable

class TonerDetail(generic.DetailView):
  model = Toner

class TonerCreate(CreateView):
  model = Toner
  fields = '__all__'
  template_name = 'schema/create.html'

class TonerUpdate(UpdateView):
  model = Toner
  fields = '__all__'
  template_name = 'schema/update.html'