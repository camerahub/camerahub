import django_tables2 as tables
from django.utils.html import format_html
from django.urls import reverse

# Import all models that need admin pages
from schema.models import Accessory, Archive, Battery, BulkFilm, Camera, CameraModel, Developer, Enlarger, FilmStock, Filter
from schema.models import Flash, FlashProtocol, Format, Lens, LensModel, Manufacturer
from schema.models import Mount, MountAdapter, NegativeSize, Order, PaperStock, Person, Print, Toning
from schema.models import Process, Repair, Scan, Negative, Film, Series, ShutterSpeed, Teleconverter, Toner

#sequence – reorder columns
#fields – specify model fields to include
#exclude – specify model fields to exclude

class AccessoryTable(tables.Table):
    class Meta:
        model = Accessory
        exclude = ('id', 'manufacturer', 'cost_currency', 'lost', 'lost_price', 'lost_price_currency', 'owner', 'acquired', 'cost')
        sequence = ('model', 'type')
    def render_model(self, value, record):
        return format_html("<a href=\"{}\">{} {}</a>", reverse('accessory-detail', args=[record.id]), record.manufacturer, value)

class ArchiveTable(tables.Table):
    class Meta:
        model = Archive
        exclude = ('id', 'owner', 'max_width', 'max_height')
        sequence = ('name',)
    def render_name(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('archive-detail', args=[record.id]), value)

class BatteryTable(tables.Table):
    class Meta:
        model = Battery
    def render_name(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('battery-detail', args=[record.id]), value)

class BulkFilmTable(tables.Table):
    class Meta:
        model = BulkFilm
        exclude = ('cost_currency', 'owner', 'purchase_date', 'source', 'batch', 'expiry', 'cost')
    def render_id(self, value, record):
        return format_html("<a href=\"{}\">#{}</a>", reverse('bulkfilm-detail', args=[value]), value)

class CameraTable(tables.Table):
    class Meta:
        model = Camera
        exclude = ('condition', 'cost_currency', 'lost', 'lost_price_currency', 'lost_price', 'owner', 'notes', 'own', 'datecode', 'source', 'condition_notes', 'display_lens')
    def render_id(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('camera-detail', args=[value]), value)
    def render_cameramodel(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('cameramodel-detail', args=[value.id]), value)  

class CameraModelTable(tables.Table):
    class Meta:
        model = CameraModel
        exclude = ('id', 'manufacturer', 'focus_type', 'metering', 'coupled_metering', 'metering_type', 'weight', 'discontinued', 'shutter_model', 'cable_release', 'viewfinder_coverage', 'power_drive', 'continuous_fps', 'fixed_mount', 'battery_qty', 'battery_type', 'notes', 'bulb', 'time', 'min_iso', 'max_iso', 'af_points', 'int_flash', 'int_flash_gn', 'ext_flash', 'flash_metering', 'pc_sync', 'hotshoe', 'coldshoe', 'meter_min_ev', 'meter_max_ev', 'dof_preview', 'tripod')
    def render_model(self, value, record):
        return format_html("<a href=\"{}\">{} {}</a>", reverse('cameramodel-detail', args=[record.id]), record.manufacturer, value)
    def render_mount(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('mount-detail', args=[value.id]), value)  
    def render_format(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('format-detail', args=[value.id]), value)

class DeveloperTable(tables.Table):
    class Meta:
        model = Developer
        exclude = ('id', 'chemistry',)

class EnlargerTable(tables.Table):
    class Meta:
        model = Enlarger
        exclude = ('id', 'manufacturer', 'lost', 'cost_currency', 'lost_price_currency', 'lost_price', 'owner', 'acquired', 'introduced', 'discontinued', 'cost')
    def render_model(self, value, record):
        return format_html("<a href=\"{}\">{} {}</a>", reverse('enlarger-detail', args=[record.id]), record.manufacturer, value)

class FilmStockTable(tables.Table):
    class Meta:
        model = FilmStock
        exclude = ('id', 'manufacturer')
    def render_name(self, value, record):
        return format_html("<a href=\"{}\">{} {}</a>", reverse('filmstock-detail', args=[record.id]), record.manufacturer, value)

class FilterTable(tables.Table):
    class Meta:
        model = Filter
        exclude = ('id', 'owner', 'attenuation', 'qty')

class FlashTable(tables.Table):
    class Meta:
        model = Flash
        exclude = ('id', 'manufacturer', 'own', 'cost_currency', 'owner', 'gn_info', 'battery_powered', 'pc_sync', 'hot_shoe', 'light_stand', 'battery_type', 'battery_qty', 'manual_control', 'swivel_head', 'tilt_head', 'zoom', 'acquired', 'cost', 'trigger_voltage')
    def render_model(self, value, record):
        return format_html("<a href=\"{}\">{} {}</a>", reverse('flash-detail', args=[record.id]), record.manufacturer, value)

class FlashProtocolTable(tables.Table):
    class Meta:
        model = FlashProtocol
        exclude = ('id', 'manufacturer',)
    def render_name(self, value, record):
        if record.manufacturer is not None:
            return format_html("<a href=\"{}\">{} {}</a>", reverse('flashprotocol-detail', args=[record.id]), record.manufacturer, value)
        else:
            return format_html("<a href=\"{}\">{}</a>", reverse('flashprotocol-detail', args=[record.id]), value)

class FormatTable(tables.Table):
    class Meta:
        model = Format
        exclude = ('id',)
    def render_format(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('format-detail', args=[record.id]), value)

class LensTable(tables.Table):
    class Meta:
        model = Lens
        exclude = ('cost_currency', 'own', 'lost', 'lost_price_currency', 'lost_price', 'owner', 'date_code', 'notes', 'source', 'condition', 'condition_notes')
    def render_id(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('lens-detail', args=[value]), value)
    def render_lensmodel(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('lensmodel-detail', args=[value.id]), value)

class LensModelTable(tables.Table):
    class Meta:
        model = LensModel
        exclude = ('id', 'manufacturer', 'zoom', 'closest_focus', 'min_aperture', 'elements', 'groups', 'weight', 'nominal_min_angle_diag', 'nominal_max_angle_diag', 'filter_thread', 'magnification', 'url', 'discontinued', 'negative_size', 'notes', 'coating', 'hood', 'exif_lenstype', 'rectilinear', 'length', 'diameter', 'image_circle', 'formula', 'shutter_model')
    def render_model(self, value, record):
        return format_html("<a href=\"{}\">{} {}</a>", reverse('lensmodel-detail', args=[record.id]), record.manufacturer, value)
    def render_mount(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('mount-detail', args=[value.id]), value)  

class ManufacturerTable(tables.Table):
    class Meta:
        model = Manufacturer
        exclude = ('id', 'url',)
    def render_name(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('manufacturer-detail', args=[record.id]), value)

class MountTable(tables.Table):
    class Meta:
        model = Mount
        exclude = ('id', 'manufacturer', 'notes')
    def render_mount(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('mount-detail', args=[record.id]), value)

class MountAdapterTable(tables.Table):
    class Meta:
        model = MountAdapter
        exclude = ('owner',)
    def render_id(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('mountadapter-detail', args=[value]), value)
    def render_camera_mount(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('mount-detail', args=[value.id]), value)
    def render_lens_mount(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('mount-detail', args=[value.id]), value)

class NegativeSizeTable(tables.Table):
    class Meta:
        model = NegativeSize
        exclude = ('id',)
    def render_name(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('negativesize-detail', args=[record.id]), value)

class OrderTable(tables.Table):
    class Meta:
        model = Order
        exclude = ('owner',)
    def render_id(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('order-detail', args=[value]), value)

class PaperStockTable(tables.Table):
    class Meta:
        model = PaperStock
        exclude = ('id', 'manufacturer',)
    def render_name(self, value, record):
        return format_html("<a href=\"{}\">{} {}</a>", reverse('paperstock-detail', args=[record.id]), record.manufacturer, value)

class PersonTable(tables.Table):
    class Meta:
        model = Person
        exclude = ('id', 'owner')
    def render_name(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('person-detail', args=[record.id]), value)

class PrintTable(tables.Table):
    class Meta:
        model = Print
        exclude = ('owner', 'own', 'sold_price_currency', 'notes', 'aperture', 'exposure_time', 'filtration_grade', 'development_time', 'enlarger', 'lens', 'developer', 'fine', 'printer')
    def render_id(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('print-detail', args=[value]), value)
    def render_negative(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('negative-detail', args=[value.id]), value)

class ToningTable(tables.Table):
    class Meta:
        model = Toning

class ProcessTable(tables.Table):
    class Meta:
        model = Process
        exclude = ('id',)
    def render_name(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('process-detail', args=[record.id]), value)

class RepairTable(tables.Table):
    class Meta:
        model = Repair
        exclude = ('detail', 'owner')
    def render_id(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('repair-detail', args=[value]), value)
    def render_camera(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('camera-detail', args=[value.id]), value)
    def render_lens(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('lens-detail', args=[value.id]), value)

class ScanTable(tables.Table):
    class Meta:
        model = Scan
        exclude = ('id', 'owner')

class NegativeTable(tables.Table):
    class Meta:
        model = Negative
        exclude = ('id', 'owner', 'filter', 'teleconverter', 'notes', 'mount_adapter', 'focal_length', 'latitude', 'longitude', 'flash', 'metering_mode', 'exposure_program', 'photographer', 'copy_of')

class FilmTable(tables.Table):
    class Meta:
        model = Film
        exclude = ('exposed_at', 'directory', 'dev_uses', 'dev_time', 'dev_temp', 'dev_n', 'developer', 'development_notes', 'price_currency', 'owner', 'date_loaded', 'date_processed', 'frames', 'bulk_film', 'bulk_film_loaded', 'film_batch', 'expiry_date', 'purchase_date', 'price', 'processed_by', 'archive')
        sequence = ('id', 'title', 'filmstock', 'format', 'camera')
    def render_id(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('film-detail', args=[value]), value)
    def render_filmstock(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('filmstock-detail', args=[value.id]), value)
    def render_format(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('format-detail', args=[value.id]), value)

class SeriesTable(tables.Table):
    class Meta:
        model = Series
        exclude = ('id', 'owner', 'id_owner')
    def render_name(self, value, record):
        return format_html("<a href=\"{}\">{}</a>", reverse('series-detail', args=[record.id]), value)

class ShutterSpeedTable(tables.Table):
    class Meta:
        model = ShutterSpeed

class TeleconverterTable(tables.Table):
    class Meta:
        model = Teleconverter
        exclude = ('id', 'manufacturer', 'owner', 'elements', 'groups', 'multicoated')
    def render_model(self, value, record):
        return format_html("<a href=\"{}\">{} {}</a>", reverse('teleconverter-detail', args=[record.id]), record.manufacturer, value)

class TonerTable(tables.Table):
    class Meta:
        model = Toner
        exclude = ('id', 'manufacturer')
    def render_name(self, value, record):
        return format_html("<a href=\"{}\">{} {}</a>", reverse('toner-detail', args=[record.id]), record.manufacturer, value)