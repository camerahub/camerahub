from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView

def index(request):
    return render(request, 'schema/index.html')

from .models import Accessory, Archive, Battery, BulkFilm, Camera, CameraModel, Developer, Enlarger, FilmStock, Filter
from .models import Flash, FlashProtocol, Format, Lens, LensModel, Manufacturer
from .models import MeteringType, Mount, MountAdapter, NegativeSize, Order, PaperStock, Person, Print, Toning
from .models import Process, Repair, Scan, Negative, Film, Series, ShutterSpeed, Teleconverter, Toner

class AccessoryList(generic.ListView):
  model = Accessory
  template_name = 'schema/list.html'

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


class ArchiveList(generic.ListView):
  model = Archive
  template_name = 'schema/list.html'

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


class BatteryList(generic.ListView):
  model = Battery
  template_name = 'schema/list.html'

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


class BulkFilmList(generic.ListView):
  model = BulkFilm
  template_name = 'schema/list.html'

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


class CameraList(generic.ListView):
  model = Camera
  template_name = 'schema/list.html'
  paginate_by = 10

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

class CameraModelList(generic.ListView):
  model = CameraModel
  template_name = 'schema/list.html'

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


class DeveloperList(generic.ListView):
  model = Developer
  template_name = 'schema/list.html'

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


class EnlargerList(generic.ListView):
  model = Enlarger
  template_name = 'schema/list.html'

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


class FilmStockList(generic.ListView):
  model = FilmStock
  template_name = 'schema/list.html'

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


class FilterList(generic.ListView):
  model = Filter
  template_name = 'schema/list.html'

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


class FlashList(generic.ListView):
  model = Flash
  template_name = 'schema/list.html'

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


class FlashProtocolList(generic.ListView):
  model = FlashProtocol
  template_name = 'schema/list.html'

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


class FormatList(generic.ListView):
  model = Format
  template_name = 'schema/list.html'

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


class LensList(generic.ListView):
  model = Lens
  template_name = 'schema/list.html'

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


class LensModelList(generic.ListView):
  model = LensModel
  template_name = 'schema/list.html'

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


class ManufacturerList(generic.ListView):
  model = Manufacturer
  template_name = 'schema/list.html'

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


class MeteringTypeList(generic.ListView):
  model = MeteringType
  template_name = 'schema/list.html'

class MeteringTypeDetail(generic.DetailView):
  model = MeteringType

class MeteringTypeCreate(CreateView):
  model = MeteringType
  fields = '__all__'
  template_name = 'schema/create.html'

class MeteringTypeUpdate(UpdateView):
  model = MeteringType
  fields = '__all__'
  template_name = 'schema/update.html'


class MountList(generic.ListView):
  model = Mount
  template_name = 'schema/list.html'

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


class MountAdapterList(generic.ListView):
  model = MountAdapter
  template_name = 'schema/list.html'

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


class NegativeSizeList(generic.ListView):
  model = NegativeSize
  template_name = 'schema/list.html'

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


class OrderList(generic.ListView):
  model = Order
  template_name = 'schema/list.html'

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


class PaperStockList(generic.ListView):
  model = PaperStock
  template_name = 'schema/list.html'

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


class PersonList(generic.ListView):
  model = Person
  template_name = 'schema/list.html'

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


class PrintList(generic.ListView):
  model = Print
  template_name = 'schema/list.html'

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


class ProcessList(generic.ListView):
  model = Process
  template_name = 'schema/list.html'

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


class RepairList(generic.ListView):
  model = Repair
  template_name = 'schema/list.html'

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


class ScanList(generic.ListView):
  model = Scan
  template_name = 'schema/list.html'

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


class NegativeList(generic.ListView):
  model = Negative
  template_name = 'schema/list.html'

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


class FilmList(generic.ListView):
  model = Film
  template_name = 'schema/list.html'

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


class SeriesList(generic.ListView):
  model = Series
  template_name = 'schema/list.html'

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


class TeleconverterList(generic.ListView):
  model = Teleconverter
  template_name = 'schema/list.html'

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


class TonerList(generic.ListView):
  model = Toner
  template_name = 'schema/list.html'

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