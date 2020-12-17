# pylint: disable=no-member

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView, ListView
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.apps import apps
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django_tables2 import SingleTableView
from django_tables2.views import SingleTableMixin
from django_filters.views import FilterView
from watson.views import SearchMixin
from taggit.models import Tag
from dal import autocomplete

from schema.models import Accessory, Archive, Battery, BulkFilm, Camera, CameraModel, Developer, Enlarger, EnlargerModel, FilmStock, Filter
from schema.models import Flash, FlashModel, Format, Lens, LensModel, Manufacturer
from schema.models import Mount, MountAdapter, NegativeSize, Order, PaperStock, Person, Print
from schema.models import Process, Scan, Negative, Film, Teleconverter, TeleconverterModel, Toner

from schema.tables import AccessoryTable, ArchiveTable, BatteryTable, BulkFilmTable, CameraTable, CameraModelTable, DeveloperTable, EnlargerTable, EnlargerModelTable, FilmStockTable, FilterTable
from schema.tables import FlashTable, FlashModelTable, FormatTable, LensTable, LensModelTable, ManufacturerTable
from schema.tables import MountTable, MountAdapterTable, NegativeSizeTable, OrderTable, PaperStockTable, PersonTable, PrintTable
from schema.tables import ProcessTable, ScanTable, NegativeTable, FilmTable, TeleconverterTable, TeleconverterModelTable, TonerTable

from schema.forms import AccessoryForm, ArchiveForm, BatteryForm, BulkFilmForm, CameraForm, CameraSellForm, CameraModelForm, DeveloperForm, EnlargerForm, EnlargerModelForm, FilmStockForm, FilterForm
from schema.forms import FlashForm, FlashModelForm, FormatForm, LensForm, LensSellForm, LensModelForm, ManufacturerForm
from schema.forms import MountForm, MountAdapterForm, NegativeSizeForm, OrderForm, PaperStockForm, PersonForm, PrintForm
from schema.forms import ProcessForm, ScanForm, NegativeForm, FilmForm, FilmAddForm, FilmLoadForm, FilmDevelopForm, FilmArchiveForm, TeleconverterForm, TeleconverterModelForm, TonerForm

from schema.filters import AccessoryFilter, BatteryFilter, BulkFilmFilter, CameraFilter, CameraModelFilter, DeveloperFilter
from schema.filters import EnlargerFilter, EnlargerModelFilter, FilmFilter, FilmStockFilter, FlashFilter, FlashModelFilter, LensFilter, LensModelFilter
from schema.filters import MountAdapterFilter, MountFilter, NegativeFilter, OrderFilter, PaperStockFilter, PrintFilter
from schema.filters import TeleconverterFilter, TeleconverterModelFilter, TonerFilter

from schema.formhelpers import AccessoryFormHelper, BatteryFormHelper, BulkFilmFormHelper, CameraFormHelper, CameraModelFormHelper
from schema.formhelpers import DeveloperFormHelper, EnlargerFormHelper, EnlargerModelFormHelper, FilmFormHelper, FilmStockFormHelper, FlashFormHelper, FlashModelFormHelper
from schema.formhelpers import LensFormHelper, LensModelFormHelper, MountAdapterFormHelper, MountFormHelper, NegativeFormHelper
from schema.formhelpers import OrderFormHelper, PaperStockFormHelper, PrintFormHelper, TeleconverterFormHelper, TeleconverterModelFormHelper, TonerFormHelper

from .funcs import to_dict

# Custom class for filtered list views in table format


class PagedFilteredTableView(SingleTableMixin, FilterView):
    filterset_class = None
    formhelper_class = None
    context_filter_name = 'filter'
    form_method = 'POST'
    template_name = 'list.html'
    paginate_by = 25

    # pylint: disable=not-callable,attribute-defined-outside-init
    def get_queryset(self):
        qs = super().get_queryset()
        self.filter = self.filterset_class(self.request.GET, queryset=qs)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs

 #   def get_table(self, **kwargs):
 #       table = super().get_table()
 #       RequestConfig(self.request, paginate={'page': self.kwargs['page'],
 #                           "per_page": self.paginate_by}).configure(table)
 #       return table

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context[self.context_filter_name] = self.filter
        return context

# Custom class for displaying a list view in table format


class SingleTableListView(SingleTableView):
    template_name = 'list.html'
    paginate_by = 25


class AccessoryList(LoginRequiredMixin, PagedFilteredTableView):
    model = Accessory
    table_class = AccessoryTable
    filterset_class = AccessoryFilter
    formhelper_class = AccessoryFormHelper


class AccessoryDetail(LoginRequiredMixin, generic.DetailView):
    model = Accessory

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Accessory, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class AccessoryCreate(LoginRequiredMixin, CreateView):
    model = Accessory
    form_class = AccessoryForm
    template_name = 'create.html'


class AccessoryUpdate(LoginRequiredMixin, UpdateView):
    model = Accessory
    form_class = AccessoryForm
    template_name = 'update.html'

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Accessory, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class ArchiveList(LoginRequiredMixin, SingleTableListView):
    model = Archive
    table_class = ArchiveTable


class ArchiveDetail(LoginRequiredMixin, generic.DetailView):
    model = Archive

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Archive, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class ArchiveCreate(LoginRequiredMixin, CreateView):
    model = Archive
    form_class = ArchiveForm
    template_name = 'create.html'


class ArchiveUpdate(LoginRequiredMixin, UpdateView):
    model = Archive
    form_class = ArchiveForm
    template_name = 'update.html'

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Archive, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class BatteryList(PagedFilteredTableView):
    model = Battery
    table_class = BatteryTable
    filterset_class = BatteryFilter
    formhelper_class = BatteryFormHelper


class BatteryDetail(generic.DetailView):
    model = Battery

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.get_object().history.all():
            context['history'] = self.get_object().history.all()
        return context


class BatteryCreate(LoginRequiredMixin, CreateView):
    model = Battery
    form_class = BatteryForm
    template_name = 'create.html'


class BatteryUpdate(LoginRequiredMixin, UpdateView):
    model = Battery
    form_class = BatteryForm
    template_name = 'update.html'


class BulkFilmList(LoginRequiredMixin, PagedFilteredTableView):
    model = BulkFilm
    table_class = BulkFilmTable
    filterset_class = BulkFilmFilter
    formhelper_class = BulkFilmFormHelper


class BulkFilmDetail(LoginRequiredMixin, generic.DetailView):
    model = BulkFilm

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(BulkFilm, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class BulkFilmCreate(LoginRequiredMixin, CreateView):
    model = BulkFilm
    form_class = BulkFilmForm
    template_name = 'create.html'


class BulkFilmUpdate(LoginRequiredMixin, UpdateView):
    model = BulkFilm
    form_class = BulkFilmForm
    template_name = 'update.html'

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(BulkFilm, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class CameraList(LoginRequiredMixin, PagedFilteredTableView):
    model = Camera
    table_class = CameraTable
    filterset_class = CameraFilter
    formhelper_class = CameraFormHelper


class CameraDetail(LoginRequiredMixin, generic.DetailView):
    model = Camera

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Camera, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class CameraCreate(LoginRequiredMixin, CreateView):
    model = Camera
    form_class = CameraForm
    template_name = 'create.html'

    def get_initial(self):
        initial = super().get_initial()
        if 'cameramodel' in self.request.GET:
            initial.update({'cameramodel': self.request.GET['cameramodel']})
        return initial


class CameraUpdate(LoginRequiredMixin, UpdateView):
    model = Camera
    form_class = CameraForm
    template_name = 'update.html'

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Camera, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class CameraSell(LoginRequiredMixin, UpdateView):
    model = Camera
    form_class = CameraSellForm
    template_name = 'update.html'

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Camera, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class CameraModelList(PagedFilteredTableView):
    model = CameraModel
    table_class = CameraModelTable
    filterset_class = CameraModelFilter
    formhelper_class = CameraModelFormHelper

    # Pass request object to table context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        table = self.table_class
        table.request = self.request
        return context


class CameraModelDetail(generic.DetailView):
    model = CameraModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Find similar objects of the same type
        similarobjects = self.get_object().tags.similar_objects()
        items = []
        for item in similarobjects:
            if type(item) == type(self.get_object()):  # pylint: disable=unidiomatic-typecheck
                detailitem = get_object_or_404(type(item), pk=item.pk)
                items.append(detailitem)
        context['related'] = items

        if self.request.user.is_authenticated:
            context['mine'] = self.get_object().camera_set.filter(
                owner=self.request.user)

        if self.get_object().history.all():
            context['history'] = self.get_object().history.all()

        return context


class CameraModelCreate(LoginRequiredMixin, CreateView):
    model = CameraModel
    form_class = CameraModelForm
    template_name = 'create.html'

    def get_initial(self):
        initial = super().get_initial()
        if 'clone' in self.request.GET:
            # Retrieve original object
            original = CameraModel.objects.get(slug=self.request.GET['clone'])

            # Copy the original object to the initial state of the new one
            initial = to_dict(original)

            # Set disambiguation
            initial['disambiguation'] = 'Clone of ' + str(original)

        return initial


class CameraModelUpdate(LoginRequiredMixin, UpdateView):
    model = CameraModel
    form_class = CameraModelForm
    template_name = 'update.html'


class DeveloperList(PagedFilteredTableView):
    model = Developer
    table_class = DeveloperTable
    filterset_class = DeveloperFilter
    formhelper_class = DeveloperFormHelper


class DeveloperDetail(generic.DetailView):
    model = Developer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Find similar objects of the same type
        similarobjects = self.get_object().tags.similar_objects()
        items = []
        for item in similarobjects:
            if type(item) == type(self.get_object()):  # pylint: disable=unidiomatic-typecheck
                detailitem = get_object_or_404(type(item), pk=item.pk)
                items.append(detailitem)
        context['related'] = items

        if self.get_object().history.all():
            context['history'] = self.get_object().history.all()

        return context


class DeveloperCreate(LoginRequiredMixin, CreateView):
    model = Developer
    form_class = DeveloperForm
    template_name = 'create.html'


class DeveloperUpdate(LoginRequiredMixin, UpdateView):
    model = Developer
    form_class = DeveloperForm
    template_name = 'update.html'


class EnlargerModelList(LoginRequiredMixin, PagedFilteredTableView):
    model = EnlargerModel
    table_class = EnlargerModelTable
    filterset_class = EnlargerModelFilter
    formhelper_class = EnlargerModelFormHelper


class EnlargerModelDetail(LoginRequiredMixin, generic.DetailView):
    model = EnlargerModel

class EnlargerModelCreate(LoginRequiredMixin, CreateView):
    model = EnlargerModel
    form_class = EnlargerModelForm
    template_name = 'create.html'


class EnlargerModelUpdate(LoginRequiredMixin, UpdateView):
    model = EnlargerModel
    form_class = EnlargerModelForm
    template_name = 'update.html'

class EnlargerList(LoginRequiredMixin, PagedFilteredTableView):
    model = Enlarger
    table_class = EnlargerTable
    filterset_class = EnlargerFilter
    formhelper_class = EnlargerFormHelper


class EnlargerDetail(LoginRequiredMixin, generic.DetailView):
    model = Enlarger

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Enlarger, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class EnlargerCreate(LoginRequiredMixin, CreateView):
    model = Enlarger
    form_class = EnlargerForm
    template_name = 'create.html'


class EnlargerUpdate(LoginRequiredMixin, UpdateView):
    model = Enlarger
    form_class = EnlargerForm
    template_name = 'update.html'

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Enlarger, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class FilmStockList(PagedFilteredTableView):
    model = FilmStock
    table_class = FilmStockTable
    filterset_class = FilmStockFilter
    formhelper_class = FilmStockFormHelper


class FilmStockDetail(generic.DetailView):
    model = FilmStock

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Find similar objects of the same type
        similarobjects = self.get_object().tags.similar_objects()
        items = []
        for item in similarobjects:
            if type(item) == type(self.get_object()):  # pylint: disable=unidiomatic-typecheck
                detailitem = get_object_or_404(type(item), pk=item.pk)
                items.append(detailitem)
        context['related'] = items

        if self.get_object().history.all():
            context['history'] = self.get_object().history.all()

        return context


class FilmStockCreate(LoginRequiredMixin, CreateView):
    model = FilmStock
    form_class = FilmStockForm
    template_name = 'create.html'


class FilmStockUpdate(LoginRequiredMixin, UpdateView):
    model = FilmStock
    form_class = FilmStockForm
    template_name = 'update.html'


class FilterList(SingleTableListView):
    model = Filter
    table_class = FilterTable


class FilterDetail(generic.DetailView):
    model = Filter


class FilterCreate(LoginRequiredMixin, CreateView):
    model = Filter
    form_class = FilterForm
    template_name = 'create.html'


class FilterUpdate(LoginRequiredMixin, UpdateView):
    model = Filter
    form_class = FilterForm
    template_name = 'update.html'


class FlashModelList(LoginRequiredMixin, PagedFilteredTableView):
    model = FlashModel
    table_class = FlashModelTable
    filterset_class = FlashModelFilter
    formhelper_class = FlashModelFormHelper


class FlashModelDetail(LoginRequiredMixin, generic.DetailView):
    model = FlashModel


class FlashModelCreate(LoginRequiredMixin, CreateView):
    model = FlashModel
    form_class = FlashModelForm
    template_name = 'create.html'


class FlashModelUpdate(LoginRequiredMixin, UpdateView):
    model = FlashModel
    form_class = FlashModelForm
    template_name = 'update.html'


class FlashList(LoginRequiredMixin, PagedFilteredTableView):
    model = Flash
    table_class = FlashTable
    filterset_class = FlashFilter
    formhelper_class = FlashFormHelper


class FlashDetail(LoginRequiredMixin, generic.DetailView):
    model = Flash

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Flash, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class FlashCreate(LoginRequiredMixin, CreateView):
    model = Flash
    form_class = FlashForm
    template_name = 'create.html'


class FlashUpdate(LoginRequiredMixin, UpdateView):
    model = Flash
    form_class = FlashForm
    template_name = 'update.html'

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Flash, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class FormatList(SingleTableListView):
    model = Format
    table_class = FormatTable


class FormatDetail(generic.DetailView):
    model = Format

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.get_object().history.all():
            context['history'] = self.get_object().history.all()
        return context


class FormatCreate(LoginRequiredMixin, CreateView):
    model = Format
    form_class = FormatForm
    template_name = 'create.html'


class FormatUpdate(LoginRequiredMixin, UpdateView):
    model = Format
    form_class = FormatForm
    template_name = 'update.html'


class LensList(LoginRequiredMixin, PagedFilteredTableView):
    model = Lens
    table_class = LensTable
    filterset_class = LensFilter
    formhelper_class = LensFormHelper


class LensDetail(LoginRequiredMixin, generic.DetailView):
    model = Lens

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Lens, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class LensCreate(LoginRequiredMixin, CreateView):
    model = Lens
    form_class = LensForm
    template_name = 'create.html'

    def get_initial(self):
        initial = super().get_initial()
        if 'lensmodel' in self.request.GET:
            initial.update({'lensmodel': self.request.GET['lensmodel']})
        return initial


class LensUpdate(LoginRequiredMixin, UpdateView):
    model = Lens
    form_class = LensForm
    template_name = 'update.html'

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Lens, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class LensSell(LoginRequiredMixin, UpdateView):
    model = Lens
    form_class = LensSellForm
    template_name = 'update.html'

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Lens, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class LensModelList(PagedFilteredTableView):
    model = LensModel
    table_class = LensModelTable
    filterset_class = LensModelFilter
    formhelper_class = LensModelFormHelper

    # Pass request object to table context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        table = self.table_class
        table.request = self.request
        return context


class LensModelDetail(generic.DetailView):
    model = LensModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Find similar objects of the same type
        similarobjects = self.get_object().tags.similar_objects()
        items = []
        for item in similarobjects:
            if type(item) == type(self.get_object()):  # pylint: disable=unidiomatic-typecheck
                detailitem = get_object_or_404(type(item), pk=item.pk)
                items.append(detailitem)
        context['related'] = items

        if self.request.user.is_authenticated:
            context['mine'] = self.get_object().lens_set.filter(
                owner=self.request.user)

        if self.get_object().history.all():
            context['history'] = self.get_object().history.all()

        return context


class LensModelCreate(LoginRequiredMixin, CreateView):
    model = LensModel
    form_class = LensModelForm
    template_name = 'create.html'

    def get_initial(self):
        initial = super().get_initial()
        if 'clone' in self.request.GET:
            # Retrieve original object
            original = LensModel.objects.get(slug=self.request.GET['clone'])

            # Copy the original object to the initial state of the new one
            initial = to_dict(original)

            # Set disambiguation
            initial['disambiguation'] = 'Clone of ' + str(original)

        return initial


class LensModelUpdate(LoginRequiredMixin, UpdateView):
    model = LensModel
    form_class = LensModelForm
    template_name = 'update.html'


class ManufacturerList(SingleTableListView):
    model = Manufacturer
    table_class = ManufacturerTable


class ManufacturerDetail(generic.DetailView):
    model = Manufacturer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Find similar objects of the same type
        similarobjects = self.get_object().tags.similar_objects()
        items = []
        for item in similarobjects:
            if type(item) == type(self.get_object()):  # pylint: disable=unidiomatic-typecheck
                detailitem = get_object_or_404(type(item), pk=item.pk)
                items.append(detailitem)
        context['related'] = items

        if self.get_object().history.all():
            context['history'] = self.get_object().history.all()

        return context


class ManufacturerCreate(LoginRequiredMixin, CreateView):
    model = Manufacturer
    form_class = ManufacturerForm
    template_name = 'create.html'


class ManufacturerUpdate(LoginRequiredMixin, UpdateView):
    model = Manufacturer
    form_class = ManufacturerForm
    template_name = 'update.html'


class MountList(PagedFilteredTableView):
    model = Mount
    table_class = MountTable
    filterset_class = MountFilter
    formhelper_class = MountFormHelper


class MountDetail(generic.DetailView):
    model = Mount

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Find similar objects of the same type
        similarobjects = self.get_object().tags.similar_objects()
        items = []
        for item in similarobjects:
            if type(item) == type(self.get_object()):  # pylint: disable=unidiomatic-typecheck
                detailitem = get_object_or_404(type(item), pk=item.pk)
                items.append(detailitem)
        context['related'] = items

        if self.get_object().history.all():
            context['history'] = self.get_object().history.all()

        return context


class MountCreate(LoginRequiredMixin, CreateView):
    model = Mount
    form_class = MountForm
    template_name = 'create.html'


class MountUpdate(LoginRequiredMixin, UpdateView):
    model = Mount
    form_class = MountForm
    template_name = 'update.html'


class MountAdapterList(LoginRequiredMixin, PagedFilteredTableView):
    model = MountAdapter
    table_class = MountAdapterTable
    filterset_class = MountAdapterFilter
    formhelper_class = MountAdapterFormHelper


class MountAdapterDetail(LoginRequiredMixin, generic.DetailView):
    model = MountAdapter

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(MountAdapter, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class MountAdapterCreate(LoginRequiredMixin, CreateView):
    model = MountAdapter
    form_class = MountAdapterForm
    template_name = 'create.html'


class MountAdapterUpdate(LoginRequiredMixin, UpdateView):
    model = MountAdapter
    form_class = MountAdapterForm
    template_name = 'update.html'

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(MountAdapter, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class NegativeSizeList(SingleTableListView):
    model = NegativeSize
    table_class = NegativeSizeTable


class NegativeSizeDetail(generic.DetailView):
    model = NegativeSize

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.get_object().history.all():
            context['history'] = self.get_object().history.all()
        return context


class NegativeSizeCreate(LoginRequiredMixin, CreateView):
    model = NegativeSize
    form_class = NegativeSizeForm
    template_name = 'create.html'


class NegativeSizeUpdate(LoginRequiredMixin, UpdateView):
    model = NegativeSize
    form_class = NegativeSizeForm
    template_name = 'update.html'


class OrderList(LoginRequiredMixin, PagedFilteredTableView):
    model = Order
    table_class = OrderTable
    filterset_class = OrderFilter
    formhelper_class = OrderFormHelper


class OrderDetail(LoginRequiredMixin, generic.DetailView):
    model = Order

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Order, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class OrderCreate(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'create.html'


class OrderUpdate(LoginRequiredMixin, UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'update.html'

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Order, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class PaperStockList(PagedFilteredTableView):
    model = PaperStock
    table_class = PaperStockTable
    filterset_class = PaperStockFilter
    formhelper_class = PaperStockFormHelper


class PaperStockDetail(generic.DetailView):
    model = PaperStock

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Find similar objects of the same type
        similarobjects = self.get_object().tags.similar_objects()
        items = []
        for item in similarobjects:
            if type(item) == type(self.get_object()):  # pylint: disable=unidiomatic-typecheck
                detailitem = get_object_or_404(type(item), pk=item.pk)
                items.append(detailitem)
        context['related'] = items

        if self.get_object().history.all():
            context['history'] = self.get_object().history.all()

        return context


class PaperStockCreate(LoginRequiredMixin, CreateView):
    model = PaperStock
    form_class = PaperStockForm
    template_name = 'create.html'


class PaperStockUpdate(LoginRequiredMixin, UpdateView):
    model = PaperStock
    form_class = PaperStockForm
    template_name = 'update.html'


class PersonList(LoginRequiredMixin, SingleTableListView):
    model = Person
    table_class = PersonTable

    def get_queryset(self):
        if self.request.user.is_authenticated:
            mystr = Person.objects.filter(owner=self.request.user)
        else:
            mystr = Person.objects.none()
        return mystr


class PersonDetail(LoginRequiredMixin, generic.DetailView):
    model = Person

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Person, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class PersonCreate(LoginRequiredMixin, CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'create.html'


class PersonUpdate(LoginRequiredMixin, UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'update.html'

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Person, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class PrintList(LoginRequiredMixin, PagedFilteredTableView):
    model = Print
    table_class = PrintTable
    filterset_class = PrintFilter
    formhelper_class = PrintFormHelper


class PrintDetail(LoginRequiredMixin, generic.DetailView):
    model = Print

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Print, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class PrintCreate(LoginRequiredMixin, CreateView):
    model = Print
    form_class = PrintForm
    template_name = 'create.html'

    def get_initial(self):
        initial = super().get_initial()
        if 'negative' in self.request.GET:
            initial.update({'negative': self.request.GET['negative']})
        return initial


class PrintUpdate(LoginRequiredMixin, UpdateView):
    model = Print
    form_class = PrintForm
    template_name = 'update.html'

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Print, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class ProcessList(SingleTableListView):
    model = Process
    table_class = ProcessTable


class ProcessDetail(generic.DetailView):
    model = Process


class ProcessCreate(LoginRequiredMixin, CreateView):
    model = Process
    form_class = ProcessForm
    template_name = 'create.html'


class ProcessUpdate(LoginRequiredMixin, UpdateView):
    model = Process
    form_class = ProcessForm
    template_name = 'update.html'


class ScanList(LoginRequiredMixin, SingleTableListView):
    model = Scan
    table_class = ScanTable

    def get_queryset(self):
        if self.request.user.is_authenticated:
            mystr = Scan.objects.filter(owner=self.request.user)
        else:
            mystr = Scan.objects.none()
        return mystr


class ScanDetail(LoginRequiredMixin, generic.DetailView):
    model = Scan

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Scan, owner=self.request.user, uuid=self.kwargs['uuid'])


class ScanCreate(LoginRequiredMixin, CreateView):
    model = Scan
    form_class = ScanForm
    template_name = 'create.html'


class ScanUpdate(LoginRequiredMixin, UpdateView):
    model = Scan
    form_class = ScanForm
    template_name = 'update.html'

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Scan, owner=self.request.user, uuid=self.kwargs['uuid'])


class NegativeList(LoginRequiredMixin, PagedFilteredTableView):
    model = Negative
    table_class = NegativeTable
    filterset_class = NegativeFilter
    formhelper_class = NegativeFormHelper


class NegativeDetail(LoginRequiredMixin, generic.DetailView):
    model = Negative

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Negative, owner=self.request.user, slug=self.kwargs['slug'])


class NegativeCreate(LoginRequiredMixin, CreateView):
    model = Negative
    form_class = NegativeForm
    template_name = 'create.html'

    def get_initial(self):
        initial = super().get_initial()
        if 'film' in self.request.GET:
            initial.update({'film': self.request.GET['film']})
        return initial


class NegativeUpdate(LoginRequiredMixin, UpdateView):
    model = Negative
    form_class = NegativeForm
    template_name = 'update.html'

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Negative, owner=self.request.user, slug=self.kwargs['slug'])


class FilmList(LoginRequiredMixin, PagedFilteredTableView):
    model = Film
    table_class = FilmTable
    filterset_class = FilmFilter
    formhelper_class = FilmFormHelper


class FilmDetail(LoginRequiredMixin, generic.DetailView):
    model = Film

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Film, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class FilmCreate(LoginRequiredMixin, CreateView):
    model = Film
    form_class = FilmAddForm
    template_name = 'create.html'


class FilmUpdate(LoginRequiredMixin, UpdateView):
    model = Film
    form_class = FilmForm
    template_name = 'update.html'

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Film, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class FilmLoad(LoginRequiredMixin, UpdateView):
    model = Film
    form_class = FilmLoadForm
    template_name = 'update.html'

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Film, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class FilmDevelop(LoginRequiredMixin, UpdateView):
    model = Film
    form_class = FilmDevelopForm
    template_name = 'update.html'

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Film, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class FilmArchive(LoginRequiredMixin, UpdateView):
    model = Film
    form_class = FilmArchiveForm
    template_name = 'update.html'

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Film, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class TeleconverterList(LoginRequiredMixin, PagedFilteredTableView):
    model = Teleconverter
    table_class = TeleconverterTable
    filterset_class = TeleconverterFilter
    formhelper_class = TeleconverterFormHelper


class TeleconverterDetail(LoginRequiredMixin, generic.DetailView):
    model = Teleconverter

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Teleconverter, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class TeleconverterCreate(LoginRequiredMixin, CreateView):
    model = Teleconverter
    form_class = TeleconverterForm
    template_name = 'create.html'


class TeleconverterUpdate(LoginRequiredMixin, UpdateView):
    model = Teleconverter
    form_class = TeleconverterForm
    template_name = 'update.html'

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Teleconverter, owner=self.request.user, id_owner=self.kwargs['id_owner'])

class TeleconverterModelList(LoginRequiredMixin, PagedFilteredTableView):
    model = TeleconverterModel
    table_class = TeleconverterModelTable
    filterset_class = TeleconverterModelFilter
    formhelper_class = TeleconverterModelFormHelper


class TeleconverterModelDetail(LoginRequiredMixin, generic.DetailView):
    model = TeleconverterModel


class TeleconverterModelCreate(LoginRequiredMixin, CreateView):
    model = TeleconverterModel
    form_class = TeleconverterModelForm
    template_name = 'create.html'


class TeleconverterModelUpdate(LoginRequiredMixin, UpdateView):
    model = TeleconverterModel
    form_class = TeleconverterModelForm
    template_name = 'update.html'


class TonerList(PagedFilteredTableView):
    model = Toner
    table_class = TonerTable
    filterset_class = TonerFilter
    formhelper_class = TonerFormHelper


class TonerDetail(generic.DetailView):
    model = Toner

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Find similar objects of the same type
        similarobjects = self.get_object().tags.similar_objects()
        items = []
        for item in similarobjects:
            if type(item) == type(self.get_object()):  # pylint: disable=unidiomatic-typecheck
                detailitem = get_object_or_404(type(item), pk=item.pk)
                items.append(detailitem)
        context['related'] = items

        if self.get_object().history.all():
            context['history'] = self.get_object().history.all()

        return context


class TonerCreate(LoginRequiredMixin, CreateView):
    model = Toner
    form_class = TonerForm
    template_name = 'create.html'


class TonerUpdate(LoginRequiredMixin, UpdateView):
    model = Toner
    form_class = TonerForm
    template_name = 'update.html'


class StatsView(TemplateView):
    template_name = "stats.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stats = [
            {
                'image': "svg/camera.svg",
                'url': reverse('schema:cameramodel-list'),
                'item': "camera models in CameraHub",
                'value': CameraModel.objects.count,
            },
            {
                'image': "svg/lens.svg",
                'url': reverse('schema:lensmodel-list'),
                'item': "lens models in CameraHub",
                'value': LensModel.objects.count,
            },
            {
                'image': "svg/film.svg",
                'url': reverse('schema:filmstock-list'),
                'item': "film stocks in CameraHub",
                'value': FilmStock.objects.count
            },
            {
                'image': "svg/manufacturer.svg",
                'url': reverse('schema:manufacturer-list'),
                'item': "manufacturers in CameraHub",
                'value': Manufacturer.objects.count
            },
            {
                'image': "svg/person.svg",
                'item': "users on CameraHub",
                'value': get_user_model().objects.count
            },
        ]

        oldestcamera = CameraModel.objects.filter(
            introduced__isnull=False).order_by('introduced').first()
        if oldestcamera:
            stats.append(
                {
                    'image': "svg/vintagecamera.svg",
                    'url': oldestcamera.get_absolute_url,
                    'item': "oldest camera on CameraHub",
                    'subheading': oldestcamera.introduced,
                    'value': oldestcamera,
                }
            )

        heaviestcamera = CameraModel.objects.filter(
            weight__isnull=False).order_by('weight').last()
        if heaviestcamera:
            stats.append(
                {
                    'image': "svg/bigcamera.svg",
                    'url': heaviestcamera.get_absolute_url,
                    'item': "heaviest camera on CameraHub",
                    'subheading': str(heaviestcamera.weight) + 'g',
                    'value': heaviestcamera
                }
            )

        longestlens = LensModel.objects.filter(
            max_focal_length__isnull=False).order_by('max_focal_length').last()
        if longestlens:
            stats.append(
                {
                    'image': "svg/lens.svg",
                    'url': longestlens.get_absolute_url,
                    'item': "longest lens on CameraHub",
                    'subheading': str(longestlens.max_focal_length) + 'mm',
                    'value': longestlens
                }
            )

        fastestlens = LensModel.objects.filter(
            max_aperture__isnull=False).order_by('max_aperture').first()
        if fastestlens:
            stats.append(
                {
                    'image': "svg/teleconverter.svg",
                    'url': fastestlens.get_absolute_url,
                    'item': "fastest lens on CameraHub",
                    'subheading': 'f/' + str(fastestlens.max_aperture),
                    'value': fastestlens
                }
            )

        stats.append(
            {
                'image': "svg/weight.svg",
                'url': reverse('schema:cameramodel-list'),
                'item': "total weight of all cameras in CameraHub",
                'value': str(round((CameraModel.objects.all().aggregate(totalweight=Sum('weight'))['totalweight'] or 0.00)/1000)) + 'kg',
            }
        )

        stats.append(
            {
                'image': "svg/ruler.svg",
                'url': reverse('schema:lensmodel-list'),
                'item': "total length of all lenses in CameraHub, laid end to end",
                'value': str(round((LensModel.objects.all().aggregate(totallength=Sum('length'))['totallength'] or 0.00)/1000)) + 'm',
            }
        )

        context['stats'] = stats
        context['title'] = "Public stats"
        return context


class MyStatsView(LoginRequiredMixin, TemplateView):
    template_name = "stats.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stats = [
            {
                'image': "svg/camera.svg",
                'url': reverse('schema:camera-list'),
                'item': "cameras in your collection right now",
                'value': Camera.objects.filter(owner=self.request.user, own=True).count,
            },
            {
                'image': "svg/camera.svg",
                'url': reverse('schema:camera-list'),
                'item': "cameras ever in your collection",
                'value': Camera.objects.filter(owner=self.request.user).count,
            },
            {
                'image': "svg/lens.svg",
                'url': reverse('schema:lens-list'),
                'item': "lenses in your collection right now",
                'value': Lens.objects.filter(owner=self.request.user, own=True).count,
            },
            {
                'image': "svg/lens.svg",
                'url': reverse('schema:lens-list'),
                'item': "lenses ever in your collection",
                'value': Lens.objects.filter(owner=self.request.user).count,
            },
            {
                'image': "svg/film.svg",
                'url': reverse('schema:film-list'),
                'item': "films in your collection",
                'value': Film.objects.filter(owner=self.request.user).count,
            },
            {
                'image': "svg/negative.svg",
                'url': reverse('schema:negative-list'),
                'item': "negatives in your collection",
                'value': Negative.objects.filter(owner=self.request.user).count,
            },
            {
                'image': "svg/print.svg",
                'url': reverse('schema:print-list'),
                'item': "prints in your collection",
                'value': Print.objects.filter(owner=self.request.user).count,
            },
        ]

        context['stats'] = stats
        context['title'] = "Private stats"
        return context


class SearchView(SearchMixin, generic.ListView):

    """View that performs a search and returns the search results."""

    template_name = "search.html"


class TagList(ListView):
    model = Tag
    template_name = 'tag-list.html'


class TagDetail(generic.DetailView):
    model = Tag
    template_name = 'tag-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        taggeditems = self.get_object().taggit_taggeditem_items.all()

        items = []
        for item in taggeditems:
            model = apps.get_model('schema', item.content_type.model)
            detailitem = get_object_or_404(model, pk=item.object_id)
            items.append(detailitem)

        context['taggeditems'] = items
        return context


class TagAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Tag.objects.none()

        qs = Tag.objects.all().order_by('name')

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs
