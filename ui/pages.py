from django.shortcuts import get_object_or_404
from django.template import Template, loader
from iommi import Page, html, Table
from schema.models import Accessory, Archive, Battery, BulkFilm, Camera, CameraModel, Developer, EnlargerModel, Enlarger
from schema.models import FilmStock, Filter, Flash, FlashModel, Format, Lens, LensModel, Manufacturer, Mount, MountAdapter
from schema.models import NegativeSize, PaperStock, Person, Print, Process, Scan, Negative, Film, Teleconverter, TeleconverterModel, Toner

class IndexPage(Page):
    title = html.h1('Placeholder')

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
