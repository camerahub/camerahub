from django.shortcuts import get_object_or_404
from django.template import Template, loader
from django.urls import reverse_lazy
from django.db.models import Sum
from iommi import Page, html, Table
from watson.views import SearchMixin
from schema.models import Accessory, Archive, Battery, BulkFilm, Camera, CameraModel, Developer, EnlargerModel, Enlarger
from schema.models import FilmStock, Filter, Flash, FlashModel, Format, Lens, LensModel, Manufacturer, Mount, MountAdapter
from schema.models import NegativeSize, PaperStock, Person, Print, Process, Scan, Negative, Film, Teleconverter, TeleconverterModel, Toner

def get_stats_context():
    stats = [
        {
            'image': "svg/camera.svg",
            'url': reverse_lazy('cameramodel-list'),
            'item': "camera models in CameraHub",
            'value': CameraModel.objects.count(),
        },
        {
            'image': "svg/lens.svg",
            'url': reverse_lazy('lensmodel-list'),
            'item': "lens models in CameraHub",
            'value': LensModel.objects.count(),
        },
        {
            'image': "svg/film.svg",
            'url': reverse_lazy('filmstock-list'),
            'item': "film stocks in CameraHub",
            'value': FilmStock.objects.count(),
        },
        {
            'image': "svg/manufacturer.svg",
            'url': reverse_lazy('manufacturer-list'),
            'item': "manufacturers in CameraHub",
            'value': Manufacturer.objects.count(),
        },
        #{
        #    'image': "svg/person.svg",
        #    'item': "users on CameraHub",
        #    'value': get_user_model().objects.count
        #},
        {
            'image': "svg/weight.svg",
            'url': reverse_lazy('cameramodel-list'),
            'item': "total weight of all cameras in CameraHub",
            'value': str(round((CameraModel.objects.all().aggregate(totalweight=Sum('weight'))['totalweight'] or 0.00)/1000)) + 'kg',
        },
        {
            'image': "svg/ruler.svg",
            'url': reverse_lazy('lensmodel-list'),
            'item': "total length of all lenses in CameraHub, laid end to end",
            'value': str(round((LensModel.objects.all().aggregate(totallength=Sum('length'))['totallength'] or 0.00)/1000)) + 'm',
        },
        {
            'image': "svg/camera.svg",
            'url': reverse_lazy('camera-list'),
            'item': "cameras in user collections on CameraHub",
            'value': Camera.objects.count,
        },
        {
            'image': "svg/film.svg",
            'url': reverse_lazy('camera-list'),
            'item': "total length of exposed film in CameraHub",
            'value': str(round((Negative.objects.all().aggregate(totallength=Sum('film__camera__cameramodel__negative_size__width'))['totallength'] or 0.00)/1000 )) + 'm',
        }
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

    context = {
        'stats': stats
    }
    return context


def get_mystats_context():
    stats=[
        {
            'image': "svg/camera.svg",
            'url': reverse_lazy('camera-list'),
            'item': "cameras in your collection right now",
            #'value': Camera.objects.filter(owner=self.request.user, own=True).count,
        },
        {
            'image': "svg/camera.svg",
            'url': reverse_lazy('camera-list'),
            'item': "cameras ever in your collection",
            #'value': Camera.objects.filter(owner=self.request.user).count,
        },
        {
            'image': "svg/lens.svg",
            'url': reverse_lazy('lens-list'),
            'item': "lenses in your collection right now",
            #'value': Lens.objects.filter(owner=self.request.user, own=True).count,
        },
        {
            'image': "svg/lens.svg",
            'url': reverse_lazy('lens-list'),
            'item': "lenses ever in your collection",
            #'value': Lens.objects.filter(owner=self.request.user).count,
        },
        {
            'image': "svg/film.svg",
            'url': reverse_lazy('film-list'),
            'item': "films in your collection",
            #'value': Film.objects.filter(owner=self.request.user).count,
        },
        {
            'image': "svg/negative.svg",
            'url': reverse_lazy('negative-list'),
            'item': "negatives in your collection",
            #'value': Negative.objects.filter(owner=self.request.user).count,
        },
        {
            'image': "svg/print.svg",
            'url': reverse_lazy('print-list'),
            'item': "prints in your collection",
            #'value': Print.objects.filter(owner=self.request.user).count,
        },
        {
            'image': "svg/film.svg",
            'url': reverse_lazy('camera-list'),
            'item': "total length of exposed film in your collection",
            #'value': str(round((Negative.objects.filter(owner=self.request.user).aggregate(totallength=Sum('film__camera__cameramodel__negative_size__width'))['totallength'] or 0.00)/1000 )) + 'm',
        },
        {
            'image': "svg/percent.svg",
            'url': reverse_lazy('camera-list'),
            'item': "percentage of camera models you've owned",
            #'value': str(round(100*(int(Camera.objects.filter(owner=self.request.user).values('cameramodel').distinct().count())/int(CameraModel.objects.count())))) + '%',
        },
        {
            'image': "svg/percent.svg",
            'url': reverse_lazy('camera-list'),
            'item': "percentage of lens models you've owned",
            #'value': str(round(100*(int(Lens.objects.filter(owner=self.request.user).values('lensmodel').distinct().count())/int(LensModel.objects.count())))) + '%',
        },
        {
            'image': "svg/ownership.svg",
            'url': reverse_lazy('camera-list'),
            'item': "net spent on cameras",
            #'value': str(round(((Camera.objects.filter(owner=self.request.user).aggregate(diff=(Sum('cost') - Sum('lost_price')))['diff'] or 0)), 2)),
        },
        {
            'image': "svg/ownership.svg",
            'url': reverse_lazy('lens-list'),
            'item': "net spent on lenses",
            #'value': str(round(((Lens.objects.filter(owner=self.request.user).aggregate(diff=(Sum('cost') - Sum('lost_price')))['diff'] or 0)), 2)),
        }
    ]
    context = {
        'stats': stats
    }
    return context


class IndexPage(Page):
    title = html.h1('Index')
    template = loader.get_template("index.html")
    body = Template(template)

    class Meta:
        context={
            'cameramodels': CameraModel.objects.count(),
            'lensmodels': LensModel.objects.count(),
            'filmstocks': FilmStock.objects.count(),
        }


class StatsPage(Page):
    """
    View that performs a search and returns the search results.
    """
    title = html.h1('Stats')
    template = loader.get_template("stats.html")
    body = Template(template)

    class Meta:        
        context = get_stats_context()


class MyStatsPage(Page):
    title = html.h1('Stats')
    template = loader.get_template("stats.html")
    body = Template(template)

    class Meta:
        context = get_mystats_context()


class SearchPage(SearchMixin, Page):
    title = html.h1('Search')
    template = loader.get_template("search.html")
    body = Template(template)

def accessory_view(request, id_owner):
    obj = get_object_or_404(Accessory, id_owner=id_owner)
    context={'object':obj}
    template = loader.get_template("detail/accessory_detail.html")
    class AccessoryPage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
    return AccessoryPage(context=context)

def archive_view(request, id_owner):
    obj = get_object_or_404(Archive, id_owner=id_owner)
    context={'object':obj}
    template = loader.get_template("detail/archive_detail.html")
    class ArchivePage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
    return ArchivePage(context=context)

def battery_view(request, slug):
    obj = get_object_or_404(Battery, slug=slug)
    context={'object':obj}
    template = loader.get_template("detail/battery_detail.html")
    class BatteryPage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
    return BatteryPage(context=context)

def bulkfilm_view(request, slug):
    obj = get_object_or_404(BulkFilm, slug=slug)
    context={'object':obj}
    template = loader.get_template("detail/bulkfilm_detail.html")
    class BulkFilmPage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
    return BulkFilmPage(context=context)

def camera_view(request, id_owner):
    obj = get_object_or_404(Camera, id_owner=id_owner)
    context={'object':obj}
    template = loader.get_template("detail/camera_detail.html")
    class CameraPage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
    return CameraPage(context=context)

def cameramodel_view(request, slug):
    obj = get_object_or_404(CameraModel, slug=slug)
    context={'object':obj}
    template = loader.get_template("detail/cameramodel_detail.html")
    class CameraModelPage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
    return CameraModelPage(context=context)

def developer_view(request, slug):
    obj = get_object_or_404(Developer, slug=slug)
    context={'object':obj}
    template = loader.get_template("detail/developer_detail.html")
    class DeveloperPage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
    return DeveloperPage(context=context)

def enlargermodel_view(request, slug):
    obj = get_object_or_404(EnlargerModel, slug=slug)
    context={'object':obj}
    template = loader.get_template("detail/enlargermodel_detail.html")
    class EnlargerModelPage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
    return EnlargerModelPage(context=context)

def enlarger_view(request, id_owner):
    obj = get_object_or_404(Enlarger, id_owner=id_owner)
    context={'object':obj}
    template = loader.get_template("detail/enlarger_detail.html")
    class EnlargerPage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
    return EnlargerPage(context=context)

def filmstock_view(request, slug):
    obj = get_object_or_404(FilmStock, slug=slug)
    context={'object':obj}
    template = loader.get_template("detail/filmstock_detail.html")
    class FilmStockPage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
    return FilmStockPage(context=context)

def filter_view(request, pk):
    obj = get_object_or_404(Filter, pk=pk)
    context={'object':obj}
    template = loader.get_template("detail/filter_detail.html")
    class FilterPage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
    return FilterPage(context=context)

def flash_view(request, id_owner):
    obj = get_object_or_404(Flash, id_owner=id_owner)
    context={'object':obj}
    template = loader.get_template("detail/flash_detail.html")
    class FlashPage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
    return FlashPage(context=context)

def flashmodel_view(request, slug):
    obj = get_object_or_404(FlashModel, slug=slug)
    context={'object':obj}
    template = loader.get_template("detail/flashmodel_detail.html")
    class FlashModelPage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
    return FlashModelPage(context=context)

def format_view(request, pk):
    obj = get_object_or_404(Format, pk=pk)
    context={'object':obj}
    template = loader.get_template("detail/format_detail.html")
    class FormatPage(Page):
        title = html.h1(obj.format)
        body = Template(template.render(context, request))
    return FormatPage(context=context)

def lens_view(request, id_owner):
    obj = get_object_or_404(Lens, id_owner=id_owner)
    context={'object':obj}
    template = loader.get_template("detail/lens_detail.html")
    class LensPage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
    return LensPage(context=context)

def lensmodel_view(request, slug):
    obj = get_object_or_404(LensModel, slug=slug)
    context={'object':obj}
    template = loader.get_template("detail/lensmodel_detail.html")
    class LensModelPage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
    return LensModelPage(context=context)

def manufacturer_view(request, slug):
    obj = get_object_or_404(Manufacturer, slug=slug)
    context={'object':obj}
    template = loader.get_template("detail/manufacturer_detail.html")
    class ManufacturerPage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
        cameramodels = Table(rows=CameraModel.objects.filter(manufacturer=obj))
        lensmodels = Table(auto__model=LensModel)
    return ManufacturerPage(context=context)

def mount_view(request, slug):
    obj = get_object_or_404(Mount, slug=slug)
    context={'object':obj}
    template = loader.get_template("detail/mount_detail.html")
    class MountPage(Page):
        title = html.h1(obj.mount)
        body = Template(template.render(context, request))
    return MountPage(context=context)

def mountadapter_view(request, id_owner):
    obj = get_object_or_404(MountAdapter, id_owner=id_owner)
    context={'object':obj}
    template = loader.get_template("detail/mountadapter_detail.html")
    class LensPage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
    return LensPage(context=context)

def negativesize_view(request, pk):
    obj = get_object_or_404(NegativeSize, pk=pk)
    context={'object':obj}
    template = loader.get_template("detail/negativesize_detail.html")
    class NegativeSizePage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
    return NegativeSizePage(context=context)

def paperstock_view(request, pk):
    obj = get_object_or_404(PaperStock, pk=pk)
    context={'object':obj}
    template = loader.get_template("detail/paperstock_detail.html")
    class PaperStockPage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
    return PaperStockPage(context=context)

def person_view(request, id_owner):
    obj = get_object_or_404(Person, id_owner=id_owner)
    context={'object':obj}
    template = loader.get_template("detail/person_detail.html")
    class PersonPage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
    return PersonPage(context=context)

def print_view(request, id_owner):
    obj = get_object_or_404(Print, id_owner=id_owner)
    context={'object':obj}
    template = loader.get_template("detail/print_detail.html")
    class PrintPage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
    return PrintPage(context=context)

def process_view(request, pk):
    obj = get_object_or_404(Process, pk=pk)
    context={'object':obj}
    template = loader.get_template("detail/process_detail.html")
    class ProcessPage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
    return ProcessPage(context=context)

def scan_view(request, uuid):
    obj = get_object_or_404(Scan, uuid=uuid)
    context={'object':obj}
    template = loader.get_template("detail/scan_detail.html")
    class ScanPage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
    return ScanPage(context=context)

def negative_view(request, slug):
    obj = get_object_or_404(Negative, slug=slug)
    context={'object':obj}
    template = loader.get_template("detail/negative_detail.html")
    class NegativePage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
    return NegativePage(context=context)

def film_view(request, id_owner):
    obj = get_object_or_404(Film, id_owner=id_owner)
    context={'object':obj}
    template = loader.get_template("detail/film_detail.html")
    class FilmPage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
    return FilmPage(context=context)

def teleconverter_view(request, id_owner):
    obj = get_object_or_404(Teleconverter, id_owner=id_owner)
    context={'object':obj}
    template = loader.get_template("detail/teleconverter_detail.html")
    class TeleconverterPage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
    return TeleconverterPage(context=context)

def teleconvertermodel_view(request, slug):
    obj = get_object_or_404(TeleconverterModel, slug=slug)
    context={'object':obj}
    template = loader.get_template("detail/teleconvertermodel_detail.html")
    class TeleconverterModelPage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
    return TeleconverterModelPage(context=context)

def toner_view(request, slug):
    obj = get_object_or_404(Toner, slug=slug)
    context={'object':obj}
    template = loader.get_template("detail/toner_detail.html")
    class TonerPage(Page):
        title = html.h1(obj.name)
        body = Template(template.render(context, request))
    return TonerPage(context=context)
