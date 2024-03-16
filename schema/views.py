# pylint: disable=no-member

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.apps import apps
from django.shortcuts import get_object_or_404
from taggit.models import Tag

from schema.models import Accessory, Archive, Battery, BulkFilm, Camera, CameraModel, Developer, Enlarger, EnlargerModel, FilmStock, Filter
from schema.models import Flash, FlashModel, Format, Lens, LensModel, Manufacturer
from schema.models import Mount, MountAdapter, NegativeSize, PaperStock, Person, Print
from schema.models import Process, Scan, Negative, Film, Teleconverter, TeleconverterModel, Toner

class AccessoryDetail(LoginRequiredMixin, generic.DetailView):
    model = Accessory
    def get_object(self):
        return get_object_or_404(Accessory, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class ArchiveDetail(LoginRequiredMixin, generic.DetailView):
    model = Archive
    def get_object(self):
        return get_object_or_404(Archive, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class ArchivePrint(LoginRequiredMixin, generic.DetailView):
    model = Archive
    template_name = 'schema/archive_print.html'
    def get_object(self):
        return get_object_or_404(Archive, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class BulkFilmDetail(LoginRequiredMixin, generic.DetailView):
    model = BulkFilm
    def get_object(self):
        return get_object_or_404(BulkFilm, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class CameraDetail(LoginRequiredMixin, generic.DetailView):
    model = Camera
    def get_object(self):
        return get_object_or_404(Camera, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class CameraModelDetail(generic.DetailView):
    model = CameraModel
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Find similar objects of the same type
        similarobjects = self.get_object().tags.similar_objects()
        items = []
        for index, item in zip(range(10), similarobjects): # pylint: disable=unused-variable
            if type(item) == type(self.get_object()):  # pylint: disable=unidiomatic-typecheck
                detailitem = get_object_or_404(type(item), pk=item.pk)
                items.append(detailitem)
        context['related'] = items

        if self.request.user.is_authenticated:
            context['mine'] = self.get_object().camera_set.filter(
                owner=self.request.user)

        return context


class DeveloperDetail(generic.DetailView):
    model = Developer
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Find similar objects of the same type
        similarobjects = self.get_object().tags.similar_objects()
        items = []
        for index, item in zip(range(10), similarobjects): # pylint: disable=unused-variable
            if type(item) == type(self.get_object()):  # pylint: disable=unidiomatic-typecheck
                detailitem = get_object_or_404(type(item), pk=item.pk)
                items.append(detailitem)
        context['related'] = items

        return context


class EnlargerDetail(LoginRequiredMixin, generic.DetailView):
    model = Enlarger
    def get_object(self):
        return get_object_or_404(Enlarger, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class FilmStockDetail(generic.DetailView):
    model = FilmStock
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Find similar objects of the same type
        similarobjects = self.get_object().tags.similar_objects()
        items = []
        for index, item in zip(range(10), similarobjects): # pylint: disable=unused-variable
            if type(item) == type(self.get_object()):  # pylint: disable=unidiomatic-typecheck
                detailitem = get_object_or_404(type(item), pk=item.pk)
                items.append(detailitem)
        context['related'] = items

        return context


class FlashDetail(LoginRequiredMixin, generic.DetailView):
    model = Flash
    def get_object(self):
        return get_object_or_404(Flash, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class FormatDetail(generic.DetailView):
    model = Format
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class LensDetail(LoginRequiredMixin, generic.DetailView):
    model = Lens
    def get_object(self):
        return get_object_or_404(Lens, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class LensModelDetail(generic.DetailView):
    model = LensModel
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Find similar objects of the same type
        similarobjects = self.get_object().tags.similar_objects()
        items = []
        for index, item in zip(range(10), similarobjects): # pylint: disable=unused-variable
            if type(item) == type(self.get_object()):  # pylint: disable=unidiomatic-typecheck
                detailitem = get_object_or_404(type(item), pk=item.pk)
                items.append(detailitem)
        context['related'] = items

        if self.request.user.is_authenticated:
            context['mine'] = self.get_object().lens_set.filter(
                owner=self.request.user)

        return context


class ManufacturerDetail(generic.DetailView):
    model = Manufacturer
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Find similar objects of the same type
        similarobjects = self.get_object().tags.similar_objects()
        items = []
        for index, item in zip(range(10), similarobjects): # pylint: disable=unused-variable
            if type(item) == type(self.get_object()):  # pylint: disable=unidiomatic-typecheck
                detailitem = get_object_or_404(type(item), pk=item.pk)
                items.append(detailitem)
        context['related'] = items

        return context


class MountDetail(generic.DetailView):
    model = Mount
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Find similar objects of the same type
        similarobjects = self.get_object().tags.similar_objects()
        items = []
        for index, item in zip(range(10), similarobjects): # pylint: disable=unused-variable
            if type(item) == type(self.get_object()):  # pylint: disable=unidiomatic-typecheck
                detailitem = get_object_or_404(type(item), pk=item.pk)
                items.append(detailitem)
        context['related'] = items

        return context


class MountAdapterDetail(LoginRequiredMixin, generic.DetailView):
    model = MountAdapter
    def get_object(self):
        return get_object_or_404(MountAdapter, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class NegativeSizeDetail(generic.DetailView):
    model = NegativeSize
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PaperStockDetail(generic.DetailView):
    model = PaperStock
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Find similar objects of the same type
        similarobjects = self.get_object().tags.similar_objects()
        items = []
        for index, item in zip(range(10), similarobjects): # pylint: disable=unused-variable
            if type(item) == type(self.get_object()):  # pylint: disable=unidiomatic-typecheck
                detailitem = get_object_or_404(type(item), pk=item.pk)
                items.append(detailitem)
        context['related'] = items

        return context


class PersonDetail(LoginRequiredMixin, generic.DetailView):
    model = Person
    def get_object(self):
        return get_object_or_404(Person, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class PrintDetail(LoginRequiredMixin, generic.DetailView):
    model = Print
    def get_object(self):
        return get_object_or_404(Print, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class PrintPrint(LoginRequiredMixin, generic.DetailView):
    model = Print
    template_name = 'schema/print_print.html'
    def get_object(self):
        return get_object_or_404(Print, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class ScanDetail(LoginRequiredMixin, generic.DetailView):
    model = Scan
    def get_object(self):
        return get_object_or_404(Scan, owner=self.request.user, uuid=self.kwargs['uuid'])


class NegativeDetail(LoginRequiredMixin, generic.DetailView):
    model = Negative
    def get_object(self):
        return get_object_or_404(Negative, owner=self.request.user, slug=self.kwargs['slug'])


class FilmDetail(LoginRequiredMixin, generic.DetailView):
    model = Film
    def get_object(self):
        return get_object_or_404(Film, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class FilmPrint(LoginRequiredMixin, generic.DetailView):
    model = Film
    template_name = 'schema/film_print.html'
    def get_object(self):
        return get_object_or_404(Film, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class TeleconverterDetail(LoginRequiredMixin, generic.DetailView):
    model = Teleconverter
    def get_object(self):
        return get_object_or_404(Teleconverter, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class TonerDetail(generic.DetailView):
    model = Toner

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Find similar objects of the same type
        similarobjects = self.get_object().tags.similar_objects()
        items = []
        for index, item in zip(range(10), similarobjects): # pylint: disable=unused-variable
            if type(item) == type(self.get_object()):  # pylint: disable=unidiomatic-typecheck
                detailitem = get_object_or_404(type(item), pk=item.pk)
                items.append(detailitem)
        context['related'] = items

        return context


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
