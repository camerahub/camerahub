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
from django_filters.views import FilterView
from watson.views import SearchMixin
from taggit.models import Tag

from schema.models import Accessory, Archive, Battery, BulkFilm, Camera, CameraModel, Developer, Enlarger, EnlargerModel, FilmStock, Filter
from schema.models import Flash, FlashModel, Format, Lens, LensModel, Manufacturer
from schema.models import Mount, MountAdapter, NegativeSize, PaperStock, Person, Print
from schema.models import Process, Scan, Negative, Film, Teleconverter, TeleconverterModel, Toner

from .funcs import to_dict

class AccessoryDetail(LoginRequiredMixin, generic.DetailView):
    model = Accessory

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Accessory, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class ArchiveDetail(LoginRequiredMixin, generic.DetailView):
    model = Archive

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Archive, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class ArchivePrint(LoginRequiredMixin, generic.DetailView):
    model = Archive
    template_name = 'schema/archive_print.html'

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Archive, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class BatteryDetail(generic.DetailView):
    model = Battery


class BulkFilmDetail(LoginRequiredMixin, generic.DetailView):
    model = BulkFilm

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(BulkFilm, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class CameraDetail(LoginRequiredMixin, generic.DetailView):
    model = Camera

    # Restrict to objects we own
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


class EnlargerModelDetail(generic.DetailView):
    model = EnlargerModel

class EnlargerDetail(LoginRequiredMixin, generic.DetailView):
    model = Enlarger

    # Restrict to objects we own
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


class FilterDetail(generic.DetailView):
    model = Filter


class FlashModelDetail(generic.DetailView):
    model = FlashModel


class FlashDetail(LoginRequiredMixin, generic.DetailView):
    model = Flash

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Flash, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class FormatDetail(generic.DetailView):
    model = Format

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class LensDetail(LoginRequiredMixin, generic.DetailView):
    model = Lens

    # Restrict to objects we own
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

    # Restrict to objects we own
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

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Person, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class PrintDetail(LoginRequiredMixin, generic.DetailView):
    model = Print

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Print, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class PrintPrint(LoginRequiredMixin, generic.DetailView):
    model = Print
    template_name = 'schema/print_print.html'

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Print, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class ProcessDetail(generic.DetailView):
    model = Process


class ScanDetail(LoginRequiredMixin, generic.DetailView):
    model = Scan

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Scan, owner=self.request.user, uuid=self.kwargs['uuid'])


class NegativeDetail(LoginRequiredMixin, generic.DetailView):
    model = Negative

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Negative, owner=self.request.user, slug=self.kwargs['slug'])


class FilmDetail(LoginRequiredMixin, generic.DetailView):
    model = Film

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Film, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class FilmPrint(LoginRequiredMixin, generic.DetailView):
    model = Film
    template_name = 'schema/film_print.html'

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Film, owner=self.request.user, id_owner=self.kwargs['id_owner'])


class TeleconverterDetail(LoginRequiredMixin, generic.DetailView):
    model = Teleconverter

    # Restrict to objects we own
    def get_object(self):
        return get_object_or_404(Teleconverter, owner=self.request.user, id_owner=self.kwargs['id_owner'])

class TeleconverterModelDetail(generic.DetailView):
    model = TeleconverterModel


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


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cameramodels'] = CameraModel.objects.count()
        context['lensmodels'] = LensModel.objects.count()
        context['filmstocks'] = FilmStock.objects.count()
        return context

class StatsView(TemplateView):
    template_name = "stats.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stats = [
            {
                'image': "svg/camera.svg",
                'url': reverse('cameramodel-list'),
                'item': "camera models in CameraHub",
                'value': CameraModel.objects.count,
            },
            {
                'image': "svg/lens.svg",
                'url': reverse('lensmodel-list'),
                'item': "lens models in CameraHub",
                'value': LensModel.objects.count,
            },
            {
                'image': "svg/film.svg",
                'url': reverse('filmstock-list'),
                'item': "film stocks in CameraHub",
                'value': FilmStock.objects.count
            },
            {
                'image': "svg/manufacturer.svg",
                'url': reverse('manufacturer-list'),
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
                'url': reverse('cameramodel-list'),
                'item': "total weight of all cameras in CameraHub",
                'value': str(round((CameraModel.objects.all().aggregate(totalweight=Sum('weight'))['totalweight'] or 0.00)/1000)) + 'kg',
            }
        )

        stats.append(
            {
                'image': "svg/ruler.svg",
                'url': reverse('lensmodel-list'),
                'item': "total length of all lenses in CameraHub, laid end to end",
                'value': str(round((LensModel.objects.all().aggregate(totallength=Sum('length'))['totallength'] or 0.00)/1000)) + 'm',
            }
        )

        stats.append(
            {
                'image': "svg/camera.svg",
                'url': reverse('camera-list'),
                'item': "cameras in user collections on CameraHub",
                'value': Camera.objects.count,
            }
        )

        stats.append(
            {
                'image': "svg/film.svg",
                'url': reverse('camera-list'),
                'item': "total length of exposed film in CameraHub",
                'value': str(round((Negative.objects.all().aggregate(totallength=Sum('film__camera__cameramodel__negative_size__width'))['totallength'] or 0.00)/1000 )) + 'm',
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
                'url': reverse('camera-list'),
                'item': "cameras in your collection right now",
                'value': Camera.objects.filter(owner=self.request.user, own=True).count,
            },
            {
                'image': "svg/camera.svg",
                'url': reverse('camera-list'),
                'item': "cameras ever in your collection",
                'value': Camera.objects.filter(owner=self.request.user).count,
            },
            {
                'image': "svg/lens.svg",
                'url': reverse('lens-list'),
                'item': "lenses in your collection right now",
                'value': Lens.objects.filter(owner=self.request.user, own=True).count,
            },
            {
                'image': "svg/lens.svg",
                'url': reverse('lens-list'),
                'item': "lenses ever in your collection",
                'value': Lens.objects.filter(owner=self.request.user).count,
            },
            {
                'image': "svg/film.svg",
                'url': reverse('film-list'),
                'item': "films in your collection",
                'value': Film.objects.filter(owner=self.request.user).count,
            },
            {
                'image': "svg/negative.svg",
                'url': reverse('negative-list'),
                'item': "negatives in your collection",
                'value': Negative.objects.filter(owner=self.request.user).count,
            },
            {
                'image': "svg/print.svg",
                'url': reverse('print-list'),
                'item': "prints in your collection",
                'value': Print.objects.filter(owner=self.request.user).count,
            },
            {
                'image': "svg/film.svg",
                'url': reverse('camera-list'),
                'item': "total length of exposed film in your collection",
                'value': str(round((Negative.objects.filter(owner=self.request.user).aggregate(totallength=Sum('film__camera__cameramodel__negative_size__width'))['totallength'] or 0.00)/1000 )) + 'm',
            },
            {
                'image': "svg/percent.svg",
                'url': reverse('camera-list'),
                'item': "percentage of camera models you've owned",
                'value': str(round(100*(int(Camera.objects.filter(owner=self.request.user).values('cameramodel').distinct().count())/int(CameraModel.objects.count())))) + '%',
            },
            {
                'image': "svg/percent.svg",
                'url': reverse('camera-list'),
                'item': "percentage of lens models you've owned",
                'value': str(round(100*(int(Lens.objects.filter(owner=self.request.user).values('lensmodel').distinct().count())/int(LensModel.objects.count())))) + '%',
            },
            {
                'image': "svg/ownership.svg",
                'url': reverse('camera-list'),
                'item': "net spent on cameras",
                'value': str(round(((Camera.objects.filter(owner=self.request.user).aggregate(diff=(Sum('cost') - Sum('lost_price')))['diff'] or 0)), 2)),
            },
            {
                'image': "svg/ownership.svg",
                'url': reverse('lens-list'),
                'item': "net spent on lenses",
                'value': str(round(((Lens.objects.filter(owner=self.request.user).aggregate(diff=(Sum('cost') - Sum('lost_price')))['diff'] or 0)), 2)),
            }
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
