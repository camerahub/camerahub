from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django_tables2 import SingleTableView
from django.contrib.auth.mixins import LoginRequiredMixin

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

class AccessoryList(LoginRequiredMixin, SingleTableListView):
  model = Accessory
  table_class = AccessoryTable
  def get_queryset(self):
    if self.request.user.is_authenticated:
      return Accessory.objects.filter(owner=self.request.user)
    else:
      return Accessory.objects.none()

class AccessoryDetail(LoginRequiredMixin, generic.DetailView):
  model = Accessory

class AccessoryCreate(LoginRequiredMixin, CreateView):
  model = Accessory
  fields = '__all__'
  template_name = 'schema/create.html'

class AccessoryUpdate(LoginRequiredMixin, UpdateView):
  model = Accessory
  fields = '__all__'
  template_name = 'schema/update.html'


class ArchiveList(LoginRequiredMixin, SingleTableListView):
  model = Archive
  table_class = ArchiveTable
  def get_queryset(self):
    if self.request.user.is_authenticated:
      return Archive.objects.filter(owner=self.request.user)
    else:
      return Archive.objects.none()

class ArchiveDetail(LoginRequiredMixin, generic.DetailView):
  model = Archive

class ArchiveCreate(LoginRequiredMixin, CreateView):
  model = Archive
  fields = '__all__'
  template_name = 'schema/create.html'

class ArchiveUpdate(LoginRequiredMixin, UpdateView):
  model = Archive
  fields = '__all__'
  template_name = 'schema/update.html'


class BatteryList(SingleTableListView):
  model = Battery
  table_class = BatteryTable

class BatteryDetail(generic.DetailView):
  model = Battery

class BatteryCreate(LoginRequiredMixin, CreateView):
  model = Battery
  fields = '__all__'
  template_name = 'schema/create.html'

class BatteryUpdate(LoginRequiredMixin, UpdateView):
  model = Battery
  fields = '__all__'
  template_name = 'schema/update.html'


class BulkFilmList(LoginRequiredMixin, SingleTableListView):
  model = BulkFilm
  table_class = BulkFilmTable
  def get_queryset(self):
    if self.request.user.is_authenticated:
      return BulkFilm.objects.filter(owner=self.request.user)
    else:
      return BulkFilm.objects.none()

class BulkFilmDetail(LoginRequiredMixin, generic.DetailView):
  model = BulkFilm

class BulkFilmCreate(LoginRequiredMixin, CreateView):
  model = BulkFilm
  fields = '__all__'
  template_name = 'schema/create.html'

class BulkFilmUpdate(LoginRequiredMixin, UpdateView):
  model = BulkFilm
  fields = '__all__'
  template_name = 'schema/update.html'


class CameraList(LoginRequiredMixin, SingleTableListView):
  model = Camera
  table_class = CameraTable
  def get_queryset(self):
    if self.request.user.is_authenticated:
      return Camera.objects.filter(owner=self.request.user)
    else:
      return Camera.objects.none()

class CameraDetail(LoginRequiredMixin, generic.DetailView):
  model = Camera

class CameraCreate(LoginRequiredMixin, CreateView):
  model = Camera
  fields = '__all__'
  template_name = 'schema/create.html'

class CameraUpdate(LoginRequiredMixin, UpdateView):
  model = Camera
  fields = '__all__'
  template_name = 'schema/update.html'

class CameraModelList(SingleTableListView):
  model = CameraModel
  table_class = CameraModelTable

class CameraModelDetail(generic.DetailView):
  model = CameraModel

class CameraModelCreate(LoginRequiredMixin, CreateView):
  model = CameraModel
  fields = '__all__'
  template_name = 'schema/create.html'

class CameraModelUpdate(LoginRequiredMixin, UpdateView):
  model = CameraModel
  fields = '__all__'
  template_name = 'schema/update.html'


class DeveloperList(SingleTableListView):
  model = Developer
  table_class = DeveloperTable

class DeveloperDetail(generic.DetailView):
  model = Developer

class DeveloperCreate(LoginRequiredMixin, CreateView):
  model = Developer
  fields = '__all__'
  template_name = 'schema/create.html'

class DeveloperUpdate(LoginRequiredMixin, UpdateView):
  model = Developer
  fields = '__all__'
  template_name = 'schema/update.html'


class EnlargerList(LoginRequiredMixin, SingleTableListView):
  model = Enlarger
  table_class = EnlargerTable
  def get_queryset(self):
    if self.request.user.is_authenticated:
      return Enlarger.objects.filter(owner=self.request.user)
    else:
      return Enlarger.objects.none()

class EnlargerDetail(LoginRequiredMixin, generic.DetailView):
  model = Enlarger

class EnlargerCreate(LoginRequiredMixin, CreateView):
  model = Enlarger
  fields = '__all__'
  template_name = 'schema/create.html'

class EnlargerUpdate(LoginRequiredMixin, UpdateView):
  model = Enlarger
  fields = '__all__'
  template_name = 'schema/update.html'


class FilmStockList(SingleTableListView):
  model = FilmStock
  table_class = FilmStockTable

class FilmStockDetail(generic.DetailView):
  model = FilmStock

class FilmStockCreate(LoginRequiredMixin, CreateView):
  model = FilmStock
  fields = '__all__'
  template_name = 'schema/create.html'

class FilmStockUpdate(LoginRequiredMixin, UpdateView):
  model = FilmStock
  fields = '__all__'
  template_name = 'schema/update.html'


class FilterList(LoginRequiredMixin, SingleTableListView):
  model = Filter
  table_class = FilterTable
  def get_queryset(self):
    if self.request.user.is_authenticated:
      return Filter.objects.filter(owner=self.request.user)
    else:
      return Filter.objects.none()

class FilterDetail(LoginRequiredMixin, generic.DetailView):
  model = Filter

class FilterCreate(LoginRequiredMixin, CreateView):
  model = Filter
  fields = '__all__'
  template_name = 'schema/create.html'

class FilterUpdate(LoginRequiredMixin, UpdateView):
  model = Filter
  fields = '__all__'
  template_name = 'schema/update.html'


class FlashList(LoginRequiredMixin, SingleTableListView):
  model = Flash
  table_class = FlashTable
  def get_queryset(self):
    if self.request.user.is_authenticated:
      return Flash.objects.filter(owner=self.request.user)
    else:
      return Flash.objects.none()

class FlashDetail(LoginRequiredMixin, generic.DetailView):
  model = Flash

class FlashCreate(LoginRequiredMixin, CreateView):
  model = Flash
  fields = '__all__'
  template_name = 'schema/create.html'

class FlashUpdate(LoginRequiredMixin, UpdateView):
  model = Flash
  fields = '__all__'
  template_name = 'schema/update.html'


class FlashProtocolList(SingleTableListView):
  model = FlashProtocol
  table_class = FlashProtocolTable

class FlashProtocolDetail(generic.DetailView):
  model = FlashProtocol

class FlashProtocolCreate(LoginRequiredMixin, CreateView):
  model = FlashProtocol
  fields = '__all__'
  template_name = 'schema/create.html'

class FlashProtocolUpdate(LoginRequiredMixin, UpdateView):
  model = FlashProtocol
  fields = '__all__'
  template_name = 'schema/update.html'


class FormatList(SingleTableListView):
  model = Format
  table_class = FormatTable

class FormatDetail(generic.DetailView):
  model = Format

class FormatCreate(LoginRequiredMixin, CreateView):
  model = Format
  fields = '__all__'
  template_name = 'schema/create.html'

class FormatUpdate(LoginRequiredMixin, UpdateView):
  model = Format
  fields = '__all__'
  template_name = 'schema/update.html'


class LensList(LoginRequiredMixin, SingleTableListView):
  model = Lens
  table_class = LensTable
  def get_queryset(self):
    if self.request.user.is_authenticated:
      return Lens.objects.filter(owner=self.request.user)
    else:
      return Lens.objects.none()

class LensDetail(LoginRequiredMixin, generic.DetailView):
  model = Lens

class LensCreate(LoginRequiredMixin, CreateView):
  model = Lens
  fields = '__all__'
  template_name = 'schema/create.html'

class LensUpdate(LoginRequiredMixin, UpdateView):
  model = Lens
  fields = '__all__'
  template_name = 'schema/update.html'


class LensModelList(SingleTableListView):
  model = LensModel
  table_class = LensModelTable

class LensModelDetail(generic.DetailView):
  model = LensModel

class LensModelCreate(LoginRequiredMixin, CreateView):
  model = LensModel
  fields = '__all__'
  template_name = 'schema/create.html'

class LensModelUpdate(LoginRequiredMixin, UpdateView):
  model = LensModel
  fields = '__all__'
  template_name = 'schema/update.html'


class ManufacturerList(SingleTableListView):
  model = Manufacturer
  table_class = ManufacturerTable

class ManufacturerDetail(generic.DetailView):
  model = Manufacturer

class ManufacturerCreate(LoginRequiredMixin, CreateView):
  model = Manufacturer
  fields = '__all__'
  template_name = 'schema/create.html'

class ManufacturerUpdate(LoginRequiredMixin, UpdateView):
  model = Manufacturer
  fields = '__all__'
  template_name = 'schema/update.html'


class MountList(SingleTableListView):
  model = Mount
  table_class = MountTable

class MountDetail(generic.DetailView):
  model = Mount

class MountCreate(LoginRequiredMixin, CreateView):
  model = Mount
  fields = '__all__'
  template_name = 'schema/create.html'

class MountUpdate(LoginRequiredMixin, UpdateView):
  model = Mount
  fields = '__all__'
  template_name = 'schema/update.html'


class MountAdapterList(LoginRequiredMixin, SingleTableListView):
  model = MountAdapter
  table_class = MountAdapterTable
  def get_queryset(self):
    if self.request.user.is_authenticated:
      return MountAdapter.objects.filter(owner=self.request.user)
    else:
      return MountAdapter.objects.none()

class MountAdapterDetail(LoginRequiredMixin, generic.DetailView):
  model = MountAdapter

class MountAdapterCreate(LoginRequiredMixin, CreateView):
  model = MountAdapter
  fields = '__all__'
  template_name = 'schema/create.html'

class MountAdapterUpdate(LoginRequiredMixin, UpdateView):
  model = MountAdapter
  fields = '__all__'
  template_name = 'schema/update.html'


class NegativeSizeList(SingleTableListView):
  model = NegativeSize
  table_class = NegativeSizeTable

class NegativeSizeDetail(generic.DetailView):
  model = NegativeSize

class NegativeSizeCreate(LoginRequiredMixin, CreateView):
  model = NegativeSize
  fields = '__all__'
  template_name = 'schema/create.html'

class NegativeSizeUpdate(LoginRequiredMixin, UpdateView):
  model = NegativeSize
  fields = '__all__'
  template_name = 'schema/update.html'


class OrderList(LoginRequiredMixin, SingleTableListView):
  model = Order
  table_class = OrderTable
  def get_queryset(self):
    if self.request.user.is_authenticated:
      return Order.objects.filter(owner=self.request.user)
    else:
      return Order.objects.none()

class OrderDetail(LoginRequiredMixin, generic.DetailView):
  model = Order

class OrderCreate(LoginRequiredMixin, CreateView):
  model = Order
  fields = '__all__'
  template_name = 'schema/create.html'

class OrderUpdate(LoginRequiredMixin, UpdateView):
  model = Order
  fields = '__all__'
  template_name = 'schema/update.html'


class PaperStockList(SingleTableListView):
  model = PaperStock
  table_class = PaperStockTable

class PaperStockDetail(generic.DetailView):
  model = PaperStock

class PaperStockCreate(LoginRequiredMixin, CreateView):
  model = PaperStock
  fields = '__all__'
  template_name = 'schema/create.html'

class PaperStockUpdate(LoginRequiredMixin, UpdateView):
  model = PaperStock
  fields = '__all__'
  template_name = 'schema/update.html'


class PersonList(LoginRequiredMixin, SingleTableListView):
  model = Person
  table_class = PersonTable
  def get_queryset(self):
    if self.request.user.is_authenticated:
      return Person.objects.filter(owner=self.request.user)
    else:
      return Person.objects.none()

class PersonDetail(LoginRequiredMixin, generic.DetailView):
  model = Person

class PersonCreate(LoginRequiredMixin, CreateView):
  model = Person
  fields = '__all__'
  template_name = 'schema/create.html'

class PersonUpdate(LoginRequiredMixin, UpdateView):
  model = Person
  fields = '__all__'
  template_name = 'schema/update.html'


class PrintList(LoginRequiredMixin, SingleTableListView):
  model = Print
  table_class = PrintTable
  def get_queryset(self):
    if self.request.user.is_authenticated:
      return Print.objects.filter(owner=self.request.user)
    else:
      return Print.objects.none()

class PrintDetail(LoginRequiredMixin, generic.DetailView):
  model = Print

class PrintCreate(LoginRequiredMixin, CreateView):
  model = Print
  fields = '__all__'
  template_name = 'schema/create.html'

class PrintUpdate(LoginRequiredMixin, UpdateView):
  model = Print
  fields = '__all__'
  template_name = 'schema/update.html'


class ProcessList(SingleTableListView):
  model = Process
  table_class = ProcessTable

class ProcessDetail(generic.DetailView):
  model = Process

class ProcessCreate(LoginRequiredMixin, CreateView):
  model = Process
  fields = '__all__'
  template_name = 'schema/create.html'

class ProcessUpdate(LoginRequiredMixin, UpdateView):
  model = Process
  fields = '__all__'
  template_name = 'schema/update.html'


class RepairList(LoginRequiredMixin, SingleTableListView):
  model = Repair
  table_class = RepairTable
  def get_queryset(self):
    if self.request.user.is_authenticated:
      return Repair.objects.filter(owner=self.request.user)
    else:
      return Repair.objects.none()

class RepairDetail(LoginRequiredMixin, generic.DetailView):
  model = Repair

class RepairCreate(LoginRequiredMixin, CreateView):
  model = Repair
  fields = '__all__'
  template_name = 'schema/create.html'

class RepairUpdate(LoginRequiredMixin, UpdateView):
  model = Repair
  fields = '__all__'
  template_name = 'schema/update.html'


class ScanList(LoginRequiredMixin, SingleTableListView):
  model = Scan
  table_class = ScanTable
  def get_queryset(self):
    if self.request.user.is_authenticated:
      return Scan.objects.filter(owner=self.request.user)
    else:
      return Scan.objects.none()

class ScanDetail(LoginRequiredMixin, generic.DetailView):
  model = Scan

class ScanCreate(LoginRequiredMixin, CreateView):
  model = Scan
  fields = '__all__'
  template_name = 'schema/create.html'

class ScanUpdate(LoginRequiredMixin, UpdateView):
  model = Scan
  fields = '__all__'
  template_name = 'schema/update.html'


class NegativeList(LoginRequiredMixin, SingleTableListView):
  model = Negative
  table_class = NegativeTable
  def get_queryset(self):
    if self.request.user.is_authenticated:
      return Negative.objects.filter(owner=self.request.user)
    else:
      return Negative.objects.none()

class NegativeDetail(LoginRequiredMixin, generic.DetailView):
  model = Negative

class NegativeCreate(LoginRequiredMixin, CreateView):
  model = Negative
  fields = '__all__'
  template_name = 'schema/create.html'

class NegativeUpdate(LoginRequiredMixin, UpdateView):
  model = Negative
  fields = '__all__'
  template_name = 'schema/update.html'


class FilmList(LoginRequiredMixin, SingleTableListView):
  model = Film
  table_class = FilmTable
  def get_queryset(self):
    if self.request.user.is_authenticated:
      return Film.objects.filter(owner=self.request.user)
    else:
      return Film.objects.none()

class FilmDetail(LoginRequiredMixin, generic.DetailView):
  model = Film

class FilmCreate(LoginRequiredMixin, CreateView):
  model = Film
  fields = '__all__'
  template_name = 'schema/create.html'

class FilmUpdate(LoginRequiredMixin, UpdateView):
  model = Film
  fields = '__all__'
  template_name = 'schema/update.html'


class SeriesList(LoginRequiredMixin, SingleTableListView):
  model = Series
  table_class = SeriesTable
  def get_queryset(self):
    if self.request.user.is_authenticated:
      return Series.objects.filter(owner=self.request.user)
    else:
      return Series.objects.none()

class SeriesDetail(LoginRequiredMixin, generic.DetailView):
  model = Series

class SeriesCreate(LoginRequiredMixin, CreateView):
  model = Series
  fields = '__all__'
  template_name = 'schema/create.html'

class SeriesUpdate(LoginRequiredMixin, UpdateView):
  model = Series
  fields = '__all__'
  template_name = 'schema/update.html'


class TeleconverterList(LoginRequiredMixin, SingleTableListView):
  model = Teleconverter
  table_class = TeleconverterTable
  def get_queryset(self):
    if self.request.user.is_authenticated:
      return Teleconverter.objects.filter(owner=self.request.user)
    else:
      return Teleconverter.objects.none()

class TeleconverterDetail(LoginRequiredMixin, generic.DetailView):
  model = Teleconverter

class TeleconverterCreate(LoginRequiredMixin, CreateView):
  model = Teleconverter
  fields = '__all__'
  template_name = 'schema/create.html'

class TeleconverterUpdate(LoginRequiredMixin, UpdateView):
  model = Teleconverter
  fields = '__all__'
  template_name = 'schema/update.html'


class TonerList(SingleTableListView):
  model = Toner
  table_class = TonerTable

class TonerDetail(generic.DetailView):
  model = Toner

class TonerCreate(LoginRequiredMixin, CreateView):
  model = Toner
  fields = '__all__'
  template_name = 'schema/create.html'

class TonerUpdate(LoginRequiredMixin, UpdateView):
  model = Toner
  fields = '__all__'
  template_name = 'schema/update.html'