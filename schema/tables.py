import django_tables2 as tables
from django.utils.html import format_html
from django.urls import reverse

# Import all models that need admin pages
from schema.models import Accessory, Archive, Battery, BulkFilm, Camera, CameraModel, Developer, Enlarger, FilmStock, Filter
from schema.models import Flash, FlashProtocol, Format, Lens, LensModel, Manufacturer
from schema.models import Mount, MountAdapter, NegativeSize, Order, PaperStock, Person, Print
from schema.models import Process, Repair, Scan, Negative, Film, Teleconverter, Toner


class AccessoryTable(tables.Table):
    class Meta:
        model = Accessory
        fields = ('model', 'type')

    @classmethod
    def render_model(cls, value, record):
        return format_html("<a href=\"{}\">{} {}</a>", reverse('accessory-detail', args=[record.id]), record.manufacturer, value)


class ArchiveTable(tables.Table):
    class Meta:
        model = Archive
        fields = ('name', 'type', 'location', 'storage', 'sealed')
        sequence = ('name',)

    @classmethod
    def render_name(cls, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('archive-detail', args=[record.id]), value)


class BatteryTable(tables.Table):
    class Meta:
        model = Battery
        fields = ('name', 'voltage', 'chemistry')

    @classmethod
    def render_name(cls, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('battery-detail', args=[record.slug]), value)


class BulkFilmTable(tables.Table):
    class Meta:
        model = BulkFilm
        fields = ('id', 'format', 'filmstock', 'id_owner')

    @classmethod
    def render_id(cls, value):
        return format_html("<a href=\"{}\">#{}</a>", reverse('bulkfilm-detail', args=[value]), value)


class CameraTable(tables.Table):
    class Meta:
        model = Camera
        fields = ('id', 'cameramodel', 'serial',
                  'manufactured', 'lens', 'id_owner')

    @classmethod
    def render_id(cls, value):
        return format_html("<a href=\"{}\">{}</a>", reverse('camera-detail', args=[value]), value)

    @classmethod
    def render_cameramodel(cls, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('cameramodel-detail', args=[record.slug]), value)


class CameraModelTable(tables.Table):
    class Meta:
        model = CameraModel
        fields = ('model', 'mount', 'format', 'introduced',
                  'body_type', 'negative_size', 'shutter_type')

    @classmethod
    def render_model(cls, value, record):
        if record.disambiguation:
            mystr = format_html("<a href=\"{}\">{} {} [{}]</a>", reverse('cameramodel-detail', args=[
                record.slug]), record.manufacturer, value, record.disambiguation)
        else:
            mystr = format_html("<a href=\"{}\">{} {}</a>", reverse(
                'cameramodel-detail', args=[record.slug]), record.manufacturer, value)
        return mystr

    @classmethod
    def render_mount(cls, value):
        return format_html("<a href=\"{}\">{}</a>", reverse('mount-detail', args=[value.slug]), value)

    @classmethod
    def render_format(cls, value):
        return format_html("<a href=\"{}\">{}</a>", reverse('format-detail', args=[value.id]), value)


class DeveloperTable(tables.Table):
    class Meta:
        model = Developer
        fields = ('name', 'for_paper', 'for_film')

    @classmethod
    def render_name(cls, value, record):
        return format_html("<a href=\"{}\">{} {}</a>", reverse('developer-detail', args=[record.slug]), record.manufacturer, value)


class EnlargerTable(tables.Table):
    class Meta:
        model = Enlarger
        fields = ('model', 'negative_size', 'type', 'id_owner')

    @classmethod
    def render_model(cls, value, record):
        return format_html("<a href=\"{}\">{} {}</a>", reverse('enlarger-detail', args=[record.id]), record.manufacturer, value)


class FilmStockTable(tables.Table):
    class Meta:
        model = FilmStock
        fields = ('name', 'iso', 'colour', 'panchromatic', 'process')

    @classmethod
    def render_name(cls, value, record):
        return format_html("<a href=\"{}\">{} {}</a>", reverse('filmstock-detail', args=[record.slug]), record.manufacturer, value)


class FilterTable(tables.Table):
    class Meta:
        model = Filter
        fields = ('type',)

    @classmethod
    def render_type(cls, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('filter-detail', args=[record.id]), value)


class FlashTable(tables.Table):
    class Meta:
        model = Flash
        fields = ('model', 'guide_number', 'ttl', 'flash_protocol', 'id_owner')

    @classmethod
    def render_model(cls, value, record):
        return format_html("<a href=\"{}\">{} {}</a>", reverse('flash-detail', args=[record.id]), record.manufacturer, value)


class FlashProtocolTable(tables.Table):
    class Meta:
        model = FlashProtocol
        fields = ('name',)

    @classmethod
    def render_name(cls, value, record):
        if record.manufacturer is not None:
            mystr = format_html("<a href=\"{}\">{} {}</a>", reverse(
                'flashprotocol-detail', args=[record.id]), record.manufacturer, value)
        else:
            mystr = format_html(
                "<a href=\"{}\">{}</a>", reverse('flashprotocol-detail', args=[record.id]), value)
        return mystr


class FormatTable(tables.Table):
    class Meta:
        model = Format
        fields = ('format',)

    @classmethod
    def render_format(cls, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('format-detail', args=[record.id]), value)


class LensTable(tables.Table):
    class Meta:
        model = Lens
        fields = ('id', 'lensmodel', 'serial',
                  'manufactured', 'acquired', 'id_owner')

    @classmethod
    def render_id(cls, value):
        return format_html("<a href=\"{}\">{}</a>", reverse('lens-detail', args=[value]), value)

    @classmethod
    def render_lensmodel(cls, value):
        return format_html("<a href=\"{}\">{}</a>", reverse('lensmodel-detail', args=[value.slug]), value)


class LensModelTable(tables.Table):
    class Meta:
        model = LensModel
        fields = ('model', 'mount', 'zoom', 'min_focal_length',
                  'max_aperture', 'autofocus', 'introduced')

    @classmethod
    def render_model(cls, value, record):
        if record.disambiguation:
            mystr = format_html("<a href=\"{}\">{} {} [{}]</a>", reverse('lensmodel-detail', args=[
                record.slug]), record.manufacturer, value, record.disambiguation)
        else:
            mystr = format_html("<a href=\"{}\">{} {}</a>", reverse(
                'lensmodel-detail', args=[record.slug]), record.manufacturer, value)
        return mystr

    @classmethod
    def render_mount(cls, value):
        return format_html("<a href=\"{}\">{}</a>", reverse('mount-detail', args=[value.slug]), value)

    @classmethod
    def render_min_focal_length(cls, record):
        if record.zoom is True:
            mystr = format_html(
                "{}-{}mm", record.min_focal_length, record.max_focal_length)
        elif record.zoom is False:
            mystr = format_html("{}mm", record.min_focal_length)
        else:
            mystr = format_html("?")
        return mystr


class ManufacturerTable(tables.Table):
    class Meta:
        model = Manufacturer
        fields = ('name', 'city', 'country', 'founded', 'dissolved')

    @classmethod
    def render_name(cls, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('manufacturer-detail', args=[record.slug]), value)


class MountTable(tables.Table):
    class Meta:
        model = Mount
        fields = ('mount', 'shutter_in_lens', 'type', 'purpose')

    @classmethod
    def render_mount(cls, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('mount-detail', args=[record.slug]), value)


class MountAdapterTable(tables.Table):
    class Meta:
        model = MountAdapter
        fields = ('id', 'camera_mount', 'lens_mount',
                  'has_optics', 'infinity_focus', 'id_owner')

    @classmethod
    def render_id(cls, value):
        return format_html("<a href=\"{}\">{}</a>", reverse('mountadapter-detail', args=[value]), value)

    @classmethod
    def render_camera_mount(cls, value):
        return format_html("<a href=\"{}\">{}</a>", reverse('mount-detail', args=[value.slug]), value)

    @classmethod
    def render_lens_mount(cls, value):
        return format_html("<a href=\"{}\">{}</a>", reverse('mount-detail', args=[value.slug]), value)


class NegativeSizeTable(tables.Table):
    class Meta:
        model = NegativeSize
        fields = ('name', 'width', 'height',
                  'crop_factor', 'area', 'aspect_ratio')

    @classmethod
    def render_name(cls, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('negativesize-detail', args=[record.id]), value)


class OrderTable(tables.Table):
    class Meta:
        model = Order
        fields = ('id', 'negative', 'width', 'height', 'added',
                  'printed', 'print', 'recipient', 'id_owner')

    @classmethod
    def render_id(cls, value):
        return format_html("<a href=\"{}\">{}</a>", reverse('order-detail', args=[value]), value)


class PaperStockTable(tables.Table):
    class Meta:
        model = PaperStock
        fields = ('name', 'resin_coated', 'colour', 'finish')

    @classmethod
    def render_name(cls, value, record):
        return format_html("<a href=\"{}\">{} {}</a>", reverse('paperstock-detail', args=[record.id]), record.manufacturer, value)


class PersonTable(tables.Table):
    class Meta:
        model = Person
        fields = ('name', 'id_owner')

    @classmethod
    def render_name(cls, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('person-detail', args=[record.id]), value)


class PrintTable(tables.Table):
    class Meta:
        model = Print
        fields = ('id', 'negative', 'date', 'paper_stock', 'height',
                  'width', 'location', 'archive', 'id_owner')

    @classmethod
    def render_id(cls, value):
        return format_html("<a href=\"{}\">{}</a>", reverse('print-detail', args=[value]), value)

    @classmethod
    def render_negative(cls, value):
        return format_html("<a href=\"{}\">{}</a>", reverse('negative-detail', args=[value.id]), value)


class ProcessTable(tables.Table):
    class Meta:
        model = Process
        fields = ('name', 'colour', 'positive')

    @classmethod
    def render_name(cls, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('process-detail', args=[record.id]), value)


class RepairTable(tables.Table):
    class Meta:
        model = Repair
        fields = ('id', 'camera', 'lens', 'date', 'summary', 'id_owner')

    @classmethod
    def render_id(cls, value):
        return format_html("<a href=\"{}\">{}</a>", reverse('repair-detail', args=[value]), value)

    @classmethod
    def render_camera(cls, value):
        return format_html("<a href=\"{}\">{}</a>", reverse('camera-detail', args=[value.id]), value)

    @classmethod
    def render_lens(cls, value):
        return format_html("<a href=\"{}\">{}</a>", reverse('lens-detail', args=[value.id]), value)


class ScanTable(tables.Table):
    class Meta:
        model = Scan
        fields = ('negative', 'print', 'filename', 'date',
                  'colour', 'width', 'height', 'id_owner')


class NegativeTable(tables.Table):
    class Meta:
        model = Negative
        fields = ('film', 'frame', 'caption', 'date', 'lens',
                  'shutter_speed', 'aperture', 'id_owner')


class FilmTable(tables.Table):
    class Meta:
        model = Film
        fields = ('id', 'title', 'filmstock', 'format', 'camera', 'id_owner')

    @classmethod
    def render_id(cls, value):
        return format_html("<a href=\"{}\">{}</a>", reverse('film-detail', args=[value]), value)

    @classmethod
    def render_filmstock(cls, value):
        return format_html("<a href=\"{}\">{}</a>", reverse('filmstock-detail', args=[value.slug]), value)

    @classmethod
    def render_format(cls, value):
        return format_html("<a href=\"{}\">{}</a>", reverse('format-detail', args=[value.id]), value)


class TeleconverterTable(tables.Table):
    class Meta:
        model = Teleconverter
        fields = ('model', 'mount', 'factor', 'id_owner')

    @classmethod
    def render_model(cls, value, record):
        return format_html("<a href=\"{}\">{} {}</a>", reverse('teleconverter-detail', args=[record.id]), record.manufacturer, value)


class TonerTable(tables.Table):
    class Meta:
        model = Toner
        fields = ('name', 'formulation', 'stock_dilution')

    @classmethod
    def render_name(cls, value, record):
        return format_html("<a href=\"{}\">{} {}</a>", reverse('toner-detail', args=[record.slug]), record.manufacturer, value)
