# pylint: disable=no-member
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from iommi import Table, Action, Column
#from django.utils.html import format_html
#from schema.funcs import colouricon

# Import all models that need tables
from schema.models import Accessory, Archive, Battery, BulkFilm, Camera, CameraModel, Developer, Enlarger, EnlargerModel, FilmStock, Filter
from schema.models import Flash, FlashModel, Format, Lens, LensModel, Manufacturer
from schema.models import Mount, MountAdapter, NegativeSize, PaperStock, Person, Print
from schema.models import Process, Scan, Negative, Film, Teleconverter, TeleconverterModel, Toner
from taggit.models import Tag

class AccessoryTable(LoginRequiredMixin, Table):
    class Meta:
        auto__model = Accessory
        auto__include=['id_owner', 'model', 'type']
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('accessory-create'))
    #@classmethod
    #def render_id_owner(cls, value):
    #    return format_html("<a href=\"{}\">#{}</a>", reverse('schema:accessory-detail', args=[value]), value)
    #@classmethod
    #def render_model(cls, value, record):
    #    return format_html("<a href=\"{}\">{} {}</a>", reverse('schema:accessory-detail', args=[record.id_owner]), record.manufacturer, value)


class ArchiveTable(LoginRequiredMixin, Table):
    class Meta:  
        auto__model = Archive
        auto__include= ('name', 'type', 'max_size', 'sealed')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('archive-create'))
    #@classmethod
    #def render_id_owner(cls, value):
    #    return format_html("<a href=\"{}\">#{}</a>", reverse('schema:archive-detail', args=[value]), value)

    #@classmethod
    #def render_name(cls, value, record):
    #    return format_html("<a href=\"{}\">{}</a>", reverse('schema:archive-detail', args=[record.id_owner]), value)

class BatteryTable(Table):
    class Meta:
        auto__model = Battery
        auto__include= ('name', 'voltage', 'chemistry')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('battery-create'))
    #@classmethod
    #def render_name(cls, value, record):
    #    return format_html("<a href=\"{}\">{}</a>", reverse('schema:battery-detail', args=[record.slug]), value)

    #@classmethod
    #def render_voltage(cls, value):
    #    return format_html("{}V", value)

class BulkFilmTable(LoginRequiredMixin, Table):
    class Meta:
        auto__model = BulkFilm
        auto__include= ('id_owner', 'format', 'filmstock', 'length', 'finished')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('bulkfilm-create'))
    #@classmethod
    #def render_id_owner(cls, value):
    #    return format_html("<a href=\"{}\">#{}</a>", reverse('schema:bulkfilm-detail', args=[value]), value)

    #@classmethod
    #def render_format(cls, value):
    #    return format_html("<a href=\"{}\">{}</a>", reverse('schema:format-detail', args=[value.id]), value)

    #@classmethod
    #def render_filmstock(cls, value):
    #    return format_html("<a href=\"{}\">{}</a>", reverse('schema:filmstock-detail', args=[value.slug]), value)

    #@classmethod
    #def render_length(cls, value):
    #    return format_html("{}m", value)

class CameraTable(LoginRequiredMixin, Table):
    class Meta:
        auto__model = Camera
        auto__include= ('id_owner', 'cameramodel', 'serial', 'manufactured', 'cameramodel__mount', 'cameramodel__lens_model_name', 'own')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('camera-create'))
    #@classmethod
    #def render_id_owner(cls, value):
    #    return format_html("<a href=\"{}\">#{}</a>", reverse('schema:camera-detail', args=[value]), value)

    #@classmethod
    #def render_cameramodel(cls, value, record):
    #    return format_html("<a href=\"{}\">{}</a>", reverse('schema:cameramodel-detail', args=[record.cameramodel.slug]), value)

    #@classmethod
    #def render_serial(cls, value):
    #    return format_html("<code>{}</code>", value)

class CameraModelTable(Table):
    class Meta:
        auto__model=CameraModel
        auto__include=('manufacturer', 'model', 'mount', 'lens_model_name', 'format', 'introduced', 'body_type', 'negative_size')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('cameramodel-create'))
    #@classmethod
    #def render_model(cls, value, record):
    #    if record.disambiguation:
    #        mystr = format_html("<a href=\"{}\">{} {} [{}]</a>", reverse('schema:cameramodel-detail', args=[
    #            record.slug]), record.manufacturer, value, record.disambiguation)
    #    else:
    #        mystr = format_html("<a href=\"{}\">{} {}</a>", reverse(
    #            'schema:cameramodel-detail', args=[record.slug]), record.manufacturer, value)
    #    if cls.request.user.is_authenticated:
    #        qty = Camera.objects.filter(
    #            owner=cls.request.user, own=True, cameramodel=record).count()
    #        if qty > 0:
    #            badge = format_html(
    #                " <span class=\"badge badge-pill badge-primary\">{}</span>", qty)
    #        else:
    #            badge = format_html("")
    #    else:
    #        badge = format_html("")
    #    return mystr+badge

    #@classmethod
    #def render_mount(cls, value):
    #    return format_html("<a href=\"{}\">{}</a>", reverse('schema:mount-detail', args=[value.slug]), value)

    #@classmethod
    #def render_format(cls, value):
    #    return format_html("<a href=\"{}\">{}</a>", reverse('schema:format-detail', args=[value.id]), value)

    #@classmethod
    #def render_negative_size(cls, value):
    #    return format_html("<a href=\"{}\">{}</a>", reverse('schema:negativesize-detail', args=[value.id]), value)

class DeveloperTable(Table):
    class Meta:
        auto__model = Developer
        auto__include= ('name', 'for_paper', 'for_film')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('developer-create'))
    #@classmethod
    #def render_name(cls, value, record):
    #    return format_html("<a href=\"{}\">{} {}</a>", reverse('schema:developer-detail', args=[record.slug]), record.manufacturer, value)

class EnlargerModelTable(Table):
    class Meta:
        auto__model = EnlargerModel
        auto__include= ('model', 'negative_size', 'type')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('enlargermodel-create'))
    #@classmethod
    #def render_model(cls, value, record):
    #    return format_html("<a href=\"{}\">{} {}</a>", reverse('schema:enlargermodel-detail', args=[record.slug]), record.manufacturer, value)


class EnlargerTable(LoginRequiredMixin, Table):
    class Meta:
        auto__model = Enlarger
        auto__include= ('id_owner', 'enlargermodel')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('enlarger-create'))
#    @classmethod
#    def render_id_owner(cls, value):
#        return format_html("<a href=\"{}\">#{}</a>", reverse('schema:enlarger-detail', args=[value]), value)

#    @classmethod
#    def render_enlargermodel(cls, value, record):
#        return format_html("<a href=\"{}\">{}</a>", reverse('schema:enlargermodel-detail', args=[record.enlargermodel.slug]), value)


class FilmStockTable(Table):
    class Meta:
        auto__model = FilmStock
        auto__include= ('name', 'iso', 'colour', 'panchromatic', 'process')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('filmstock-create'))
    #@classmethod
    #def render_name(cls, value, record):
    #    return format_html("<a href=\"{}\">{} {}</a>", reverse('schema:filmstock-detail', args=[record.slug]), record.manufacturer, value)

    #@classmethod
    #def render_colour(cls, value):
    #    return format_html(colouricon(value))

class FilterTable(Table):
    class Meta:
        auto__model = Filter
        auto__include= ('type', 'shortname', 'attenuation')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('filter-create'))
#    @classmethod
#    def render_type(cls, value, record):
#        return format_html("<a href=\"{}\">{}</a>", reverse('schema:filter-detail', args=[record.id]), value)


class FlashModelTable(Table):
    class Meta:
        auto__model = FlashModel
        auto__include= ('model', 'guide_number', 'ttl')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('flashmodel-create'))
    #@classmethod
    #def render_model(cls, value, record):
    #    return format_html("<a href=\"{}\">{} {}</a>", reverse('schema:flashmodel-detail', args=[record.slug]), record.manufacturer, value)

class FlashTable(LoginRequiredMixin, Table):
    class Meta:
        auto__model = Flash
        auto__include= ('id_owner', 'flashmodel')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('flash-create'))
    #@classmethod
    #def render_id_owner(cls, value):
    #    return format_html("<a href=\"{}\">#{}</a>", reverse('schema:flash-detail', args=[value]), value)

    #@classmethod
    #def render_flashmodel(cls, value, record):
    #    return format_html("<a href=\"{}\">{}</a>", reverse('schema:flashmodel-detail', args=[record.flashmodel.slug]), value)

class FormatTable(Table):
    class Meta:
        auto__model = Format
        auto__include= ('format',)
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('format-create'))
    #@classmethod
    #def render_format(cls, value, record):
    #    return format_html("<a href=\"{}\">{}</a>", reverse('schema:format-detail', args=[record.id]), value)

class LensTable(LoginRequiredMixin, Table):
    class Meta:
        auto__model = Lens
        auto__include= ('id_owner', 'lensmodel', 'lensmodel__mount', 'serial', 'manufactured', 'own')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('lens-create'))
    #@classmethod
    #def render_id_owner(cls, value):
    #    return format_html("<a href=\"{}\">#{}</a>", reverse('schema:lens-detail', args=[value]), value)

    #@classmethod
    #def render_lensmodel(cls, value):
    #    return format_html("<a href=\"{}\">{}</a>", reverse('schema:lensmodel-detail', args=[value.slug]), value)

    #@classmethod
    #def render_lensmodel__mount(cls, value):
    #    return format_html("<a href=\"{}\">{}</a>", reverse('schema:mount-detail', args=[value.slug]), value)

    #@classmethod
    #def render_serial(cls, value):
    #    return format_html("<code>{}</code>", value)

class LensModelTable(Table):
    class Meta:
        auto__model = LensModel
        auto__include= ('model', 'mount', 'zoom', 'focal_length', 'max_aperture', 'autofocus', 'introduced')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('lensmodel-create'))
    #@classmethod
    #def render_model(cls, value, record):
    #    if record.disambiguation:
    #        mystr = format_html("<a href=\"{}\">{} {} [{}]</a>", reverse('schema:lensmodel-detail', args=[
    #            record.slug]), record.manufacturer, value, record.disambiguation)
    #    else:
    #        mystr = format_html("<a href=\"{}\">{} {}</a>", reverse(
    #            'schema:lensmodel-detail', args=[record.slug]), record.manufacturer, value)
    #    if cls.request.user.is_authenticated:
    #        qty = Lens.objects.filter(
    #            owner=cls.request.user, own=True, lensmodel=record).count()
    #        if qty > 0:
    #            badge = format_html(
    #                " <span class=\"badge badge-pill badge-primary\">{}</span>", qty)
    #        else:
    #            badge = format_html("")
    #    else:
    #        badge = format_html("")
    #    return mystr+badge

    #@classmethod
    #def render_mount(cls, value):
    #    return format_html("<a href=\"{}\">{}</a>", reverse('schema:mount-detail', args=[value.slug]), value)

    #@classmethod
    #def render_max_aperture(cls, value):
    #    return format_html("<em>f</em>/{}", value)


class ManufacturerTable(Table):
    select = Column.select()  # Shortcut for creating checkboxes to select rows

    class Meta:
        auto__model=Manufacturer
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('manufacturer-create'))
    #@classmethod
    #def render_name(cls, value, record):
    #    return format_html("<a href=\"{}\">{}</a>", reverse('schema:manufacturer-detail', args=[record.slug]), value)

    #@classmethod
    #def render_country(cls, record):
    #    return format_html("{} <img src=\"{}\">", record.country.name, record.country.flag)


class MountTable(Table):
    class Meta:
        auto__model = Mount
        auto__include= ('mount', 'shutter_in_lens', 'type', 'purpose')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('mount-create'))
    #@classmethod
    #def render_mount(cls, value, record):
    #    return format_html("<a href=\"{}\">{}</a>", reverse('schema:mount-detail', args=[record.slug]), value)

class MountAdapterTable(LoginRequiredMixin, Table):
    class Meta:
        auto__model = MountAdapter
        auto__include= ('id_owner', 'camera_mount', 'lens_mount', 'has_optics', 'infinity_focus')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('mountadapter-create'))
    #@classmethod
    #def render_id_owner(cls, value):
    #    return format_html("<a href=\"{}\">#{}</a>", reverse('schema:mountadapter-detail', args=[value]), value)

    #@classmethod
    #def render_camera_mount(cls, value):
    #    return format_html("<a href=\"{}\">{}</a>", reverse('schema:mount-detail', args=[value.slug]), value)

    #@classmethod
    #def render_lens_mount(cls, value):
    #    return format_html("<a href=\"{}\">{}</a>", reverse('schema:mount-detail', args=[value.slug]), value)


class NegativeSizeTable(Table):
    class Meta:
        auto__model = NegativeSize
        auto__include= ('name', 'size', 'crop_factor', 'area', 'aspect_ratio')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('negativesize-create'))
    #@classmethod
    #def render_name(cls, value, record):
    #    return format_html("<a href=\"{}\">{}</a>", reverse('schema:negativesize-detail', args=[record.id]), value)

    #@classmethod
    #def render_crop_factor(cls, value):
    #    return format_html("{}&times;", value)

    #@classmethod
    #def render_area(cls, value):
    #    return format_html("{}mm&sup2;", value)

    #@classmethod
    #def render_aspect_ratio(cls, value):
    #    return format_html("{}&times;", value)

class PaperStockTable(Table):
    class Meta:
        auto__model = PaperStock
        auto__include= ('name', 'resin_coated', 'colour', 'finish')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('paperstock-create'))
    #@classmethod
    #def render_name(cls, value, record):
    #    return format_html("<a href=\"{}\">{} {}</a>", reverse('schema:paperstock-detail', args=[record.id]), record.manufacturer, value)

class PersonTable(LoginRequiredMixin, Table):
    class Meta:
        auto__model = Person
        auto__include= ('id_owner', 'name', 'type')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('person-create'))
    #@classmethod
    #def render_id_owner(cls, value):
    #    return format_html("<a href=\"{}\">#{}</a>", reverse('schema:person-detail', args=[value]), value)

    #@classmethod
    #def render_name(cls, value, record):
    #    return format_html("<a href=\"{}\">{}</a>", reverse('schema:person-detail', args=[record.id_owner]), value)

    #def get_queryset(self):
    #    if self.request.user.is_authenticated:
    #        mystr = Person.objects.filter(owner=self.request.user)
    #    else:
    #        mystr = Person.objects.none()
    #    return mystr

class PrintTable(LoginRequiredMixin, Table):
    class Meta:
        auto__model = Print
        auto__include= ('id_owner', 'negative', 'date', 'size', 'own', 'archive')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('print-create'))
    #@classmethod
    #def render_id_owner(cls, value, record):
    #    return format_html("<a href=\"{}\">{}</a>", reverse('schema:print-detail', args=[value]), record)

    #@classmethod
    #def render_negative(cls, value):
    #    return format_html("<a href=\"{}\">#{}</a>", reverse('schema:negative-detail', args=[value.slug]), value.slug)

    #@classmethod
    #def render_archive(cls, value):
    #    return format_html("<a href=\"{}\">{}</a>", reverse('schema:archive-detail', args=[value.id_owner]), value)

class ProcessTable(Table):
    class Meta:
        auto__model = Process
        auto__include= ('name', 'colour', 'positive')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('process-create'))
    #@classmethod
    #def render_name(cls, value, record):
    #    return format_html("<a href=\"{}\">{}</a>", reverse('schema:process-detail', args=[record.id]), value)

class ScanTable(LoginRequiredMixin, Table):
    class Meta:
        auto__model = Scan
        auto__include= ('uuid', 'negative', 'print', 'filename', 'date')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('scan-create'))
    #@classmethod
    #def render_uuid(cls, value):
    #    return format_html("<code><a href=\"{}\">{}</a></code>", reverse('schema:scan-detail', args=[value]), value)

    #@classmethod
    #def render_negative(cls, value):
    #    return format_html("<a href=\"{}\">{}</a>", reverse('schema:negative-detail', args=[value.slug]), value)

    #@classmethod
    #def render_print(cls, value):
    #    return format_html("<a href=\"{}\">{}</a>", reverse('schema:print-detail', args=[value.id_owner]), value)

    #@classmethod
    #def render_filename(cls, value):
    #    return format_html("<code>{}</code>", value)

class NegativeTable(LoginRequiredMixin, Table):
    class Meta:
        auto__model = Negative
        auto__include= ('slug', 'film', 'date', 'film__camera', 'lens', 'shutter_speed', 'aperture')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('negative-create'))
    #@classmethod
    #def render_slug(cls, value, record):
    #    return format_html("<a href=\"{}\">{}</a>", reverse('schema:negative-detail', args=[value]), record)

    #@classmethod
    #def render_aperture(cls, value):
    #    return format_html("<em>f</em>/{}", value)

    #@classmethod
    #def render_film(cls, value):
    #    return format_html("<a href=\"{}\">{}</a>", reverse('schema:film-detail', args=[value.id_owner]), value)

    #@classmethod
    #def render_film__camera(cls, value):
    #    return format_html("<a href=\"{}\">{}</a>", reverse('schema:camera-detail', args=[value.id_owner]), value)

    #@classmethod
    #def render_lens(cls, value):
    #    return format_html("<a href=\"{}\">{}</a>", reverse('schema:lens-detail', args=[value.id_owner]), value)

class FilmTable(LoginRequiredMixin, Table):
    class Meta:
        auto__model = Film
        auto__include= ('id_owner', 'filmstock', 'format', 'status', 'negative_set__count', 'date_processed', 'camera')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('film-create'))
    #@classmethod
    #def render_id_owner(cls, value, record):
    #    return format_html("<a href=\"{}\">{}</a>", reverse('schema:film-detail', args=[value]), record)

    #@classmethod
    #def render_filmstock(cls, value):
    #    return format_html("<a href=\"{}\">{}</a>", reverse('schema:filmstock-detail', args=[value.slug]), value)

    #@classmethod
    #def render_format(cls, value):
    #    return format_html("<a href=\"{}\">{}</a>", reverse('schema:format-detail', args=[value.id]), value)

    #@classmethod
    #def render_camera(cls, value):
    #    return format_html("<a href=\"{}\">{}</a>", reverse('schema:camera-detail', args=[value.id_owner]), value)

class TagTable(Table):
    class Meta:
        auto__model = Tag
        query_from_indexes=True
        #actions__add=Action(attrs__href=reverse_lazy('tag-create'))


class TeleconverterTable(LoginRequiredMixin, Table):
    class Meta:
        auto__model = Teleconverter
        auto__include= ('id_owner', 'teleconvertermodel',)
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('teleconverter-create'))
    #@classmethod
    #def render_id_owner(cls, value):
    #    return format_html("<a href=\"{}\">#{}</a>", reverse('schema:teleconverter-detail', args=[value]), value)

    #@classmethod
    #def render_teleconvertermodel(cls, value, record):
    #    return format_html("<a href=\"{}\">{}</a>", reverse('schema:teleconvertermodel-detail', args=[record.teleconvertermodel.slug]), value)

class TeleconverterModelTable(Table):
    class Meta:
        auto__model = TeleconverterModel
        auto__include= ('model', 'mount', 'factor')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('teleconvertermodel-create'))
    #@classmethod
    #def render_model(cls, value, record):
    #    if record.manufacturer is not None:
    #        mystr = format_html("<a href=\"{}\">{} {}</a>", reverse(
    #            'schema:teleconvertermodel-detail', args=[record.slug]), record.manufacturer, value)
    #    else:
    #        mystr = format_html(
    #            "<a href=\"{}\">{}</a>", reverse('schema:teleconvertermodel-detail', args=[record.slug]), value)
    #    return mystr

    #@classmethod
    #def render_factor(cls, value):
    #    return format_html("{}&times;", value)

    #@classmethod
    #def render_mount(cls, value):
    #    return format_html("<a href=\"{}\">{}</a>", reverse('schema:mount-detail', args=[value.slug]), value)

class TonerTable(Table):
    class Meta:        
        auto__model = Toner
        auto__include= ('name', 'formulation', 'stock_dilution')
        query_from_indexes=True
        actions__add=Action(attrs__href=reverse_lazy('toner-create'))
    #@classmethod
    #def render_name(cls, value, record):
    #    return format_html("<a href=\"{}\">{} {}</a>", reverse('schema:toner-detail', args=[record.slug]), record.manufacturer, value)
