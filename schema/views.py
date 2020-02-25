from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from django_tables2 import SingleTableView
from django.contrib.auth.mixins import LoginRequiredMixin

from schema.models import Accessory, Archive, Battery, BulkFilm, Camera, CameraModel, Developer, Enlarger, FilmStock, Filter
from schema.models import Flash, FlashProtocol, Format, Lens, LensModel, Manufacturer
from schema.models import Mount, MountAdapter, NegativeSize, Order, PaperStock, Person, Print, Toning
from schema.models import Process, Repair, Scan, Negative, Film, Series, ShutterSpeed, Teleconverter, Toner

from schema.tables import AccessoryTable, ArchiveTable, BatteryTable, BulkFilmTable, CameraTable, CameraModelTable, DeveloperTable, EnlargerTable, FilmStockTable, FilterTable
from schema.tables import FlashTable, FlashProtocolTable, FormatTable, LensTable, LensModelTable, ManufacturerTable
from schema.tables import MountTable, MountAdapterTable, NegativeSizeTable, OrderTable, PaperStockTable, PersonTable, PrintTable, ToningTable
from schema.tables import ProcessTable, RepairTable, ScanTable, NegativeTable, FilmTable, SeriesTable, ShutterSpeedTable, TeleconverterTable, TonerTable

from schema.forms import AccessoryForm, ArchiveForm, BatteryForm, BulkFilmForm, CameraForm, CameraModelForm, DeveloperForm, EnlargerForm, FilmStockForm, FilterForm
from schema.forms import FlashForm, FlashProtocolForm, FormatForm, LensForm, LensModelForm, ManufacturerForm
from schema.forms import MountForm, MountAdapterForm, NegativeSizeForm, OrderForm, PaperStockForm, PersonForm, PrintForm
from schema.forms import ProcessForm, RepairForm, ScanForm, NegativeForm, FilmForm, SeriesForm, TeleconverterForm, TonerForm

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
  form_class = AccessoryForm
  template_name = 'schema/create.html'

class AccessoryUpdate(LoginRequiredMixin, UpdateView):
  model = Accessory
  form_class = AccessoryForm
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
  form_class = ArchiveForm
  template_name = 'schema/create.html'

class ArchiveUpdate(LoginRequiredMixin, UpdateView):
  model = Archive
  form_class = ArchiveForm
  template_name = 'schema/update.html'


class BatteryList(SingleTableListView):
  model = Battery
  table_class = BatteryTable

class BatteryDetail(generic.DetailView):
  model = Battery

class BatteryCreate(LoginRequiredMixin, CreateView):
  model = Battery
  form_class = BatteryForm
  template_name = 'schema/create.html'

class BatteryUpdate(LoginRequiredMixin, UpdateView):
  model = Battery
  form_class = BatteryForm
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
  form_class = BulkFilmForm
  template_name = 'schema/create.html'

class BulkFilmUpdate(LoginRequiredMixin, UpdateView):
  model = BulkFilm
  form_class = BulkFilmForm
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
  form_class = CameraForm
  template_name = 'schema/create.html'

class CameraUpdate(LoginRequiredMixin, UpdateView):
  model = Camera
  form_class = CameraForm
  template_name = 'schema/update.html'

class CameraModelList(SingleTableListView):
  model = CameraModel
  table_class = CameraModelTable

class CameraModelDetail(generic.DetailView):
  model = CameraModel

class CameraModelCreate(LoginRequiredMixin, CreateView):
  model = CameraModel
  form_class = CameraModelForm
  template_name = 'schema/create.html'

class CameraModelUpdate(LoginRequiredMixin, UpdateView):
  model = CameraModel
  form_class = CameraModelForm
  template_name = 'schema/update.html'


class DeveloperList(SingleTableListView):
  model = Developer
  table_class = DeveloperTable

class DeveloperDetail(generic.DetailView):
  model = Developer

class DeveloperCreate(LoginRequiredMixin, CreateView):
  model = Developer
  form_class = DeveloperForm
  template_name = 'schema/create.html'

class DeveloperUpdate(LoginRequiredMixin, UpdateView):
  model = Developer
  form_class = DeveloperForm
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
  form_class = EnlargerForm
  template_name = 'schema/create.html'

class EnlargerUpdate(LoginRequiredMixin, UpdateView):
  model = Enlarger
  form_class = EnlargerForm
  template_name = 'schema/update.html'


class FilmStockList(SingleTableListView):
  model = FilmStock
  table_class = FilmStockTable

class FilmStockDetail(generic.DetailView):
  model = FilmStock

class FilmStockCreate(LoginRequiredMixin, CreateView):
  model = FilmStock
  form_class = FilmStockForm
  template_name = 'schema/create.html'

class FilmStockUpdate(LoginRequiredMixin, UpdateView):
  model = FilmStock
  form_class = FilmStockForm
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
  form_class = FilterForm
  template_name = 'schema/create.html'

class FilterUpdate(LoginRequiredMixin, UpdateView):
  model = Filter
  form_class = FilterForm
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
  form_class = FlashForm
  template_name = 'schema/create.html'

class FlashUpdate(LoginRequiredMixin, UpdateView):
  model = Flash
  form_class = FlashForm
  template_name = 'schema/update.html'


class FlashProtocolList(SingleTableListView):
  model = FlashProtocol
  table_class = FlashProtocolTable

class FlashProtocolDetail(generic.DetailView):
  model = FlashProtocol

class FlashProtocolCreate(LoginRequiredMixin, CreateView):
  model = FlashProtocol
  form_class = FlashProtocolForm
  template_name = 'schema/create.html'

class FlashProtocolUpdate(LoginRequiredMixin, UpdateView):
  model = FlashProtocol
  form_class = FlashProtocolForm
  template_name = 'schema/update.html'


class FormatList(SingleTableListView):
  model = Format
  table_class = FormatTable

class FormatDetail(generic.DetailView):
  model = Format

class FormatCreate(LoginRequiredMixin, CreateView):
  model = Format
  form_class = FormatForm
  template_name = 'schema/create.html'

class FormatUpdate(LoginRequiredMixin, UpdateView):
  model = Format
  form_class = FormatForm
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
  form_class = LensForm
  template_name = 'schema/create.html'

class LensUpdate(LoginRequiredMixin, UpdateView):
  model = Lens
  form_class = LensForm
  template_name = 'schema/update.html'


class LensModelList(SingleTableListView):
  model = LensModel
  table_class = LensModelTable

class LensModelDetail(generic.DetailView):
  model = LensModel

class LensModelCreate(LoginRequiredMixin, CreateView):
  model = LensModel
  form_class = LensModelForm
  template_name = 'schema/create.html'

class LensModelUpdate(LoginRequiredMixin, UpdateView):
  model = LensModel
  form_class = LensModelForm
  template_name = 'schema/update.html'


class ManufacturerList(SingleTableListView):
  model = Manufacturer
  table_class = ManufacturerTable

class ManufacturerDetail(generic.DetailView):
  model = Manufacturer

class ManufacturerCreate(LoginRequiredMixin, CreateView):
  model = Manufacturer
  form_class = ManufacturerForm
  template_name = 'schema/create.html'

class ManufacturerUpdate(LoginRequiredMixin, UpdateView):
  model = Manufacturer
  form_class = ManufacturerForm
  template_name = 'schema/update.html'


class MountList(SingleTableListView):
  model = Mount
  table_class = MountTable

class MountDetail(generic.DetailView):
  model = Mount

class MountCreate(LoginRequiredMixin, CreateView):
  model = Mount
  form_class = MountForm
  template_name = 'schema/create.html'

class MountUpdate(LoginRequiredMixin, UpdateView):
  model = Mount
  form_class = MountForm
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
  form_class = MountAdapterForm
  template_name = 'schema/create.html'

class MountAdapterUpdate(LoginRequiredMixin, UpdateView):
  model = MountAdapter
  form_class = MountAdapterForm
  template_name = 'schema/update.html'


class NegativeSizeList(SingleTableListView):
  model = NegativeSize
  table_class = NegativeSizeTable

class NegativeSizeDetail(generic.DetailView):
  model = NegativeSize

class NegativeSizeCreate(LoginRequiredMixin, CreateView):
  model = NegativeSize
  form_class = NegativeSizeForm
  template_name = 'schema/create.html'

class NegativeSizeUpdate(LoginRequiredMixin, UpdateView):
  model = NegativeSize
  form_class = NegativeSizeForm
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
  form_class = OrderForm
  template_name = 'schema/create.html'

class OrderUpdate(LoginRequiredMixin, UpdateView):
  model = Order
  form_class = OrderForm
  template_name = 'schema/update.html'


class PaperStockList(SingleTableListView):
  model = PaperStock
  table_class = PaperStockTable

class PaperStockDetail(generic.DetailView):
  model = PaperStock

class PaperStockCreate(LoginRequiredMixin, CreateView):
  model = PaperStock
  form_class = PaperStockForm
  template_name = 'schema/create.html'

class PaperStockUpdate(LoginRequiredMixin, UpdateView):
  model = PaperStock
  form_class = PaperStockForm
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
  form_class = PersonForm
  template_name = 'schema/create.html'

class PersonUpdate(LoginRequiredMixin, UpdateView):
  model = Person
  form_class = PersonForm
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
  form_class = PrintForm
  template_name = 'schema/create.html'

class PrintUpdate(LoginRequiredMixin, UpdateView):
  model = Print
  form_class = PrintForm
  template_name = 'schema/update.html'


class ProcessList(SingleTableListView):
  model = Process
  table_class = ProcessTable

class ProcessDetail(generic.DetailView):
  model = Process

class ProcessCreate(LoginRequiredMixin, CreateView):
  model = Process
  form_class = ProcessForm
  template_name = 'schema/create.html'

class ProcessUpdate(LoginRequiredMixin, UpdateView):
  model = Process
  form_class = ProcessForm
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
  form_class = RepairForm
  template_name = 'schema/create.html'

class RepairUpdate(LoginRequiredMixin, UpdateView):
  model = Repair
  form_class = RepairForm
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
  form_class = ScanForm
  template_name = 'schema/create.html'

class ScanUpdate(LoginRequiredMixin, UpdateView):
  model = Scan
  form_class = ScanForm
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
  form_class = NegativeForm
  template_name = 'schema/create.html'

class NegativeUpdate(LoginRequiredMixin, UpdateView):
  model = Negative
  form_class = NegativeForm
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
  form_class = FilmForm
  template_name = 'schema/create.html'

class FilmUpdate(LoginRequiredMixin, UpdateView):
  model = Film
  form_class = FilmForm
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
  form_class = SeriesForm
  template_name = 'schema/create.html'

class SeriesUpdate(LoginRequiredMixin, UpdateView):
  model = Series
  form_class = SeriesForm
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
  form_class = TeleconverterForm
  template_name = 'schema/create.html'

class TeleconverterUpdate(LoginRequiredMixin, UpdateView):
  model = Teleconverter
  form_class = TeleconverterForm
  template_name = 'schema/update.html'


class TonerList(SingleTableListView):
  model = Toner
  table_class = TonerTable

class TonerDetail(generic.DetailView):
  model = Toner

class TonerCreate(LoginRequiredMixin, CreateView):
  model = Toner
  form_class = TonerForm
  template_name = 'schema/create.html'

class TonerUpdate(LoginRequiredMixin, UpdateView):
  model = Toner
  form_class = TonerForm
  template_name = 'schema/update.html'

class StatsView(TemplateView):
  template_name = "schema/stats.html"

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['num_camera_models'] = CameraModel.objects.count
      context['num_lens_models'] = LensModel.objects.count
      context['num_filmstocks'] = FilmStock.objects.count
      return context
