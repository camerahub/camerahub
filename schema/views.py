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

class ArchiveList(generic.ListView):
  model = Archive
  template_name = 'schema/list.html'

class ArchiveDetail(generic.DetailView):
  model = Archive

class BatteryList(generic.ListView):
  model = Battery
  template_name = 'schema/list.html'

class BatteryDetail(generic.DetailView):
  model = Battery

class BulkFilmList(generic.ListView):
  model = BulkFilm
  template_name = 'schema/list.html'

class BulkFilmDetail(generic.DetailView):
  model = BulkFilm

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

class DeveloperList(generic.ListView):
  model = Developer
  template_name = 'schema/list.html'

class DeveloperDetail(generic.DetailView):
  model = Developer

class EnlargerList(generic.ListView):
  model = Enlarger
  template_name = 'schema/list.html'

class EnlargerDetail(generic.DetailView):
  model = Enlarger

class FilmStockList(generic.ListView):
  model = FilmStock
  template_name = 'schema/list.html'

class FilmStockDetail(generic.DetailView):
  model = FilmStock

class FilterList(generic.ListView):
  model = Filter
  template_name = 'schema/list.html'

class FilterDetail(generic.DetailView):
  model = Filter

class FlashList(generic.ListView):
  model = Flash
  template_name = 'schema/list.html'

class FlashDetail(generic.DetailView):
  model = Flash

class FlashProtocolList(generic.ListView):
  model = FlashProtocol
  template_name = 'schema/list.html'

class FlashProtocolDetail(generic.DetailView):
  model = FlashProtocol

class FormatList(generic.ListView):
  model = Format
  template_name = 'schema/list.html'

class FormatDetail(generic.DetailView):
  model = Format

class LensList(generic.ListView):
  model = Lens
  template_name = 'schema/list.html'

class LensDetail(generic.DetailView):
  model = Lens

class LensModelList(generic.ListView):
  model = LensModel
  template_name = 'schema/list.html'

class LensModelDetail(generic.DetailView):
  model = LensModel

class ManufacturerList(generic.ListView):
  model = Manufacturer
  template_name = 'schema/list.html'

class ManufacturerDetail(generic.DetailView):
  model = Manufacturer

class MeteringTypeList(generic.ListView):
  model = MeteringType
  template_name = 'schema/list.html'

class MeteringTypeDetail(generic.DetailView):
  model = MeteringType

class MountList(generic.ListView):
  model = Mount
  template_name = 'schema/list.html'

class MountDetail(generic.DetailView):
  model = Mount

class MountAdapterList(generic.ListView):
  model = MountAdapter
  template_name = 'schema/list.html'

class MountAdapterDetail(generic.DetailView):
  model = MountAdapter

class NegativeSizeList(generic.ListView):
  model = NegativeSize
  template_name = 'schema/list.html'

class NegativeSizeDetail(generic.DetailView):
  model = NegativeSize

class OrderList(generic.ListView):
  model = Order
  template_name = 'schema/list.html'

class OrderDetail(generic.DetailView):
  model = Order

class PaperStockList(generic.ListView):
  model = PaperStock
  template_name = 'schema/list.html'

class PaperStockDetail(generic.DetailView):
  model = PaperStock

class PersonList(generic.ListView):
  model = Person
  template_name = 'schema/list.html'

class PersonDetail(generic.DetailView):
  model = Person

class PrintList(generic.ListView):
  model = Print
  template_name = 'schema/list.html'

class PrintDetail(generic.DetailView):
  model = Print

class ProcessList(generic.ListView):
  model = Process
  template_name = 'schema/list.html'

class ProcessDetail(generic.DetailView):
  model = Process

class RepairList(generic.ListView):
  model = Repair
  template_name = 'schema/list.html'

class RepairDetail(generic.DetailView):
  model = Repair

class ScanList(generic.ListView):
  model = Scan
  template_name = 'schema/list.html'

class ScanDetail(generic.DetailView):
  model = Scan

class NegativeList(generic.ListView):
  model = Negative
  template_name = 'schema/list.html'

class NegativeDetail(generic.DetailView):
  model = Negative

class FilmList(generic.ListView):
  model = Film
  template_name = 'schema/list.html'

class FilmDetail(generic.DetailView):
  model = Film

class SeriesList(generic.ListView):
  model = Series
  template_name = 'schema/list.html'

class SeriesDetail(generic.DetailView):
  model = Series

class TeleconverterList(generic.ListView):
  model = Teleconverter
  template_name = 'schema/list.html'

class TeleconverterDetail(generic.DetailView):
  model = Teleconverter

class TonerList(generic.ListView):
  model = Toner
  template_name = 'schema/list.html'

class TonerDetail(generic.DetailView):
  model = Toner