import django_tables2 as tables
from django.utils.html import format_html
from django.urls import reverse

# Import all models that need admin pages
from schema.models import Accessory, Archive, Battery, BulkFilm, Camera, CameraModel, Developer, Enlarger, FilmStock, Filter
from schema.models import Flash, FlashProtocol, Format, Lens, LensModel, Manufacturer
from schema.models import Mount, MountAdapter, NegativeSize, Order, PaperStock, Person, Print, Toning
from schema.models import Process, Repair, Scan, Negative, Film, Series, ShutterSpeed, Teleconverter, Toner


class AccessoryTable(tables.Table):
    class Meta:
        model = Accessory
        fields = ('model', 'type')

    def render_model(self, value, record):
        return format_html("<a href=\"{}\">{} {}</a>", reverse('accessory-detail', args=[record.id]), record.manufacturer, value)


class ArchiveTable(tables.Table):
    class Meta:
        model = Archive
        fields = ('name', 'type', 'location', 'storage', 'sealed')
        sequence = ('name',)

    def render_name(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('archive-detail', args=[record.id]), value)


class BatteryTable(tables.Table):
    class Meta:
        model = Battery
        fields = ('name', 'voltage', 'chemistry')

    def render_name(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('battery-detail', args=[record.slug]), value)


class BulkFilmTable(tables.Table):
    class Meta:
        model = BulkFilm
        fields = ('id', 'format', 'filmstock', 'id_owner')

    def render_id(self, value, record):
        return format_html("<a href=\"{}\">#{}</a>", reverse('bulkfilm-detail', args=[value]), value)


class CameraTable(tables.Table):
    class Meta:
        model = Camera
        fields = ('id', 'cameramodel', 'serial',
                  'manufactured', 'lens', 'id_owner')

    def render_id(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('camera-detail', args=[value]), value)

    def render_cameramodel(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('cameramodel-detail', args=[record.slug]), value)


class CameraModelTable(tables.Table):
    class Meta:
        model = CameraModel
        fields = ('model', 'disambiguation', 'mount', 'format',
                  'introduced', 'body_type', 'negative_size', 'shutter_type')

    def render_model(self, value, record):
        return format_html("<a href=\"{}\">{} {}</a>", reverse('cameramodel-detail', args=[record.slug]), record.manufacturer, value)

    def render_mount(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('mount-detail', args=[value.slug]), value)

    def render_format(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('format-detail', args=[value.id]), value)


class DeveloperTable(tables.Table):
    class Meta:
        model = Developer
        fields = ('name', 'for_paper', 'for_film')

    def render_name(self, value, record):
        return format_html("<a href=\"{}\">{} {}</a>", reverse('developer-detail', args=[record.slug]), record.manufacturer, value)


class EnlargerTable(tables.Table):
    class Meta:
        model = Enlarger
        fields = ('model', 'negative_size', 'type', 'id_owner')

    def render_model(self, value, record):
        return format_html("<a href=\"{}\">{} {}</a>", reverse('enlarger-detail', args=[record.id]), record.manufacturer, value)


class FilmStockTable(tables.Table):
    class Meta:
        model = FilmStock
        fields = ('name', 'iso', 'colour', 'panchromatic', 'process')

    def render_name(self, value, record):
        return format_html("<a href=\"{}\">{} {}</a>", reverse('filmstock-detail', args=[record.slug]), record.manufacturer, value)


class FilterTable(tables.Table):
    class Meta:
        model = Filter
        fields = ('type',)

    def render_type(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('filter-detail', args=[record.id]), value)


class FlashTable(tables.Table):
    class Meta:
        model = Flash
        fields = ('model', 'guide_number', 'ttl', 'flash_protocol', 'id_owner')

    def render_model(self, value, record):
        return format_html("<a href=\"{}\">{} {}</a>", reverse('flash-detail', args=[record.id]), record.manufacturer, value)


class FlashProtocolTable(tables.Table):
    class Meta:
        model = FlashProtocol
        fields = ('name',)

    def render_name(self, value, record):
        if record.manufacturer is not None:
            return format_html("<a href=\"{}\">{} {}</a>", reverse('flashprotocol-detail', args=[record.id]), record.manufacturer, value)
        else:
            return format_html("<a href=\"{}\">{}</a>", reverse('flashprotocol-detail', args=[record.id]), value)


class FormatTable(tables.Table):
    class Meta:
        model = Format
        fields = ('format',)

    def render_format(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('format-detail', args=[record.id]), value)


class LensTable(tables.Table):
    class Meta:
        model = Lens
        fields = ('id', 'lensmodel', 'serial',
                  'manufactured', 'acquired', 'id_owner')

    def render_id(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('lens-detail', args=[value]), value)

    def render_lensmodel(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('lensmodel-detail', args=[value.slug]), value)


class LensModelTable(tables.Table):
    class Meta:
        model = LensModel
        fields = ('model', 'disambiguation', 'mount', 'zoom', 'min_focal_length',
                  'max_aperture', 'autofocus', 'introduced', 'fixed_mount')

    def render_model(self, value, record):
        return format_html("<a href=\"{}\">{} {}</a>", reverse('lensmodel-detail', args=[record.slug]), record.manufacturer, value)

    def render_mount(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('mount-detail', args=[value.slug]), value)

    def render_min_focal_length(self, value, record):
        if record.zoom is True:
            return format_html("{}-{}mm", record.min_focal_length, record.max_focal_length)
        elif record.zoom is False:
            return format_html("{}mm", record.min_focal_length)
        else:
            return format_html("?")


class ManufacturerTable(tables.Table):
    class Meta:
        model = Manufacturer
        fields = ('name', 'city', 'country', 'founded', 'dissolved')

    def render_name(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('manufacturer-detail', args=[record.slug]), value)


class MountTable(tables.Table):
    class Meta:
        model = Mount
        fields = ('mount', 'shutter_in_lens', 'type', 'purpose')

    def render_mount(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('mount-detail', args=[record.slug]), value)


class MountAdapterTable(tables.Table):
    class Meta:
        model = MountAdapter
        fields = ('id', 'camera_mount', 'lens_mount',
                  'has_optics', 'infinity_focus', 'id_owner')

    def render_id(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('mountadapter-detail', args=[value]), value)

    def render_camera_mount(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('mount-detail', args=[value.slug]), value)

    def render_lens_mount(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('mount-detail', args=[value.slug]), value)


class NegativeSizeTable(tables.Table):
    class Meta:
        model = NegativeSize
        fields = ('name', 'width', 'height',
                  'crop_factor', 'area', 'aspect_ratio')

    def render_name(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('negativesize-detail', args=[record.id]), value)


class OrderTable(tables.Table):
    class Meta:
        model = Order
        fields = ('id', 'negative', 'width', 'height', 'added',
                  'printed', 'print', 'recipient', 'id_owner')

    def render_id(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('order-detail', args=[value]), value)


class PaperStockTable(tables.Table):
    class Meta:
        model = PaperStock
        fields = ('name', 'resin_coated', 'colour', 'finish')

    def render_name(self, value, record):
        return format_html("<a href=\"{}\">{} {}</a>", reverse('paperstock-detail', args=[record.id]), record.manufacturer, value)


class PersonTable(tables.Table):
    class Meta:
        model = Person
        fields = ('name', 'id_owner')

    def render_name(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('person-detail', args=[record.id]), value)


class PrintTable(tables.Table):
    class Meta:
        model = Print
        fields = ('id', 'negative', 'date', 'paper_stock', 'height',
                  'width', 'location', 'archive', 'id_owner')

    def render_id(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('print-detail', args=[value]), value)

    def render_negative(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('negative-detail', args=[value.id]), value)


class ProcessTable(tables.Table):
    class Meta:
        model = Process
        fields = ('name', 'colour', 'positive')

    def render_name(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('process-detail', args=[record.id]), value)


class RepairTable(tables.Table):
    class Meta:
        model = Repair
        fields = ('id', 'camera', 'lens', 'date', 'summary', 'id_owner')

    def render_id(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('repair-detail', args=[value]), value)

    def render_camera(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('camera-detail', args=[value.id]), value)

    def render_lens(self, value, record):
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

    def render_id(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('film-detail', args=[value]), value)

    def render_filmstock(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('filmstock-detail', args=[value.slug]), value)

    def render_format(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('format-detail', args=[value.id]), value)


class SeriesTable(tables.Table):
    class Meta:
        model = Series
        fields = ('name',)

    def render_name(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('series-detail', args=[record.id]), value)


class TeleconverterTable(tables.Table):
    class Meta:
        model = Teleconverter
        fields = ('model', 'mount', 'factor', 'id_owner')

    def render_model(self, value, record):
        return format_html("<a href=\"{}\">{} {}</a>", reverse('teleconverter-detail', args=[record.id]), record.manufacturer, value)


class TonerTable(tables.Table):
    class Meta:
        model = Toner
        fields = ('name', 'formulation', 'stock_dilution')

    def render_name(self, value, record):
        return format_html("<a href=\"{}\">{} {}</a>", reverse('toner-detail', args=[record.slug]), record.manufacturer, value)
