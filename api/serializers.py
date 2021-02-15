from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, StringRelatedField, HyperlinkedIdentityField
from schema.models import Accessory, Archive,  Battery, Camera, CameraModel, Filter, NegativeSize, Film, Format
from schema.models import FlashModel, Flash, EnlargerModel, Enlarger, LensModel, Manufacturer, Mount, Negative, PaperStock
from schema.models import Person, Process, TeleconverterModel, Teleconverter, Toner, FilmStock, BulkFilm, MountAdapter, Developer
from schema.models import Lens, Print, Scan, Order

class ManufacturerSerializer(ModelSerializer):
    country = StringRelatedField(many=False)

    class Meta:
        model = Manufacturer
        fields = ['name', 'city', 'country', 'linkurl',
                  'founded', 'dissolved' ]

class MountSerializer(ModelSerializer):
    manufacturer = ManufacturerSerializer(many=False)

    class Meta:
        model = Mount
        fields = ['mount', 'shutter_in_lens', 'type',
                  'purpose', 'notes', 'manufacturer' ]

class NegativeSizeSerializer(ModelSerializer):

    class Meta:
        model = NegativeSize
        fields = [ 'name', 'width', 'height', ]

class PersonSerializer(ModelSerializer):

    class Meta:
        model = Person
        fields = ['name']


class ProcessSerializer(ModelSerializer):

    class Meta:
        model = Process
        fields = ['name', 'colour', 'positive']


class FormatSerializer(ModelSerializer):
    negative_size = NegativeSizeSerializer(many=False)

    class Meta:
        model = Format
        fields = ['format', 'negative_size']


class BatterySerializer(ModelSerializer):

    class Meta:
        model = Battery
        fields = ['name', 'voltage', 'chemistry', 'compatible_with']


class FilmStockSerializer(ModelSerializer):
    manufacturer = ManufacturerSerializer(many=False)
    process = ProcessSerializer(many=False)

    class Meta:
        model = FilmStock
        fields = ['name', 'manufacturer', 'iso',
                  'colour', 'panchromatic', 'process', ]


class ArchiveSerializer(ModelSerializer):

    class Meta:
        model = Archive
        fields = ['name', 'type', 'max_width',
                  'max_height', 'location', 'storage', 'sealed']



class FilterSerializer(ModelSerializer):

    class Meta:
        model = Filter
        fields = ['type', 'shortname', 'attenuation']


class FlashModelSerializer(ModelSerializer):
    manufacturer = ManufacturerSerializer(many=False)
    battery_type = BatterySerializer(many=False)

    class Meta:
        model = FlashModel
        fields = ['manufacturer', 'model', 'disambiguation', 'guide_number', 'gn_info', 'battery_powered', 'pc_sync', 'hot_shoe', 'light_stand', 'battery_type',
                  'battery_qty', 'manual_control', 'swivel_head', 'tilt_head', 'zoom', 'ttl', 'trigger_voltage', 'image', 'image_attribution', 'image_attribution_url']


class FlashSerializer(ModelSerializer):
    flashmodel = FlashModelSerializer(many=False)

    class Meta:
        model = Flash
        fields = ['flashmodel', 'serial', 'own',
                  'acquired', 'cost', 'lost', 'lost_price']


class EnlargerModelSerializer(ModelSerializer):
    manufacturer = ManufacturerSerializer(many=False)
    negative_size = NegativeSizeSerializer(many=False)

    class Meta:
        model = EnlargerModel
        fields = ['manufacturer', 'model', 'disambiguation', 'negative_size',
                  'type', 'light_source', 'introduced', 'discontinued', 'image', 'image_attribution', 'image_attribution_url']


class EnlargerSerializer(ModelSerializer):
    enlargermodel = EnlargerModelSerializer(many=False)

    class Meta:
        model = Enlarger
        fields = ['enlargermodel', 'serial', 'own',
                  'acquired', 'cost', 'lost', 'lost_price']


class PaperStockSerializer(ModelSerializer):
    manufacturer = ManufacturerSerializer(many=False)

    class Meta:
        model = PaperStock
        fields = ['name', 'manufacturer',
                  'resin_coated', 'colour', 'finish' ]


class TeleconverterModelSerializer(ModelSerializer):
    manufacturer = ManufacturerSerializer(many=False)
    mount = MountSerializer(many=False)

    class Meta:
        model = TeleconverterModel
        fields = ['model', 'manufacturer', 'disambiguation', 'mount',
                  'factor', 'elements', 'groups', 'multicoated', 'image', 'image_attribution', 'image_attribution_url']


class TeleconverterSerializer(ModelSerializer):
    teleconvertermodel = TeleconverterModelSerializer(many=False)

    class Meta:
        model = Teleconverter
        fields = ['teleconvertermodel', 'serial', 'own',
                  'acquired', 'cost', 'lost', 'lost_price', ]


class TonerSerializer(ModelSerializer):
    manufacturer = ManufacturerSerializer(many=False)

    class Meta:
        model = Toner
        fields = [ 'name', 'manufacturer', 'formulation', 'stock_dilution', ]


class BulkFilmSerializer(ModelSerializer):
    format = FormatSerializer(many=False)
    filmstock = FilmStockSerializer(many=False)

    class Meta:
        model = BulkFilm
        fields = ['format', 'filmstock', 'length', 'finished', 'purchase_date',
                  'cost', 'source', 'batch', 'expiry']


class MountAdapterSerializer(ModelSerializer):
    camera_mount = MountSerializer(many=False)
    lens_mount = MountSerializer(many=False)

    class Meta:
        model = MountAdapter
        fields = [ 'camera_mount', 'lens_mount', 'has_optics', 'infinity_focus', 'notes' ]


class DeveloperSerializer(ModelSerializer):
    manufacturer = ManufacturerSerializer(many=False)

    class Meta:
        model = Developer
        fields = ['manufacturer', 'name', 'for_paper',
                  'for_film', 'chemistry' ]


class AccessorySerializer(ModelSerializer):
    manufacturer = ManufacturerSerializer(many=False)
    camera_model_compatibility = StringRelatedField(many=True)
    lens_model_compatibility = StringRelatedField(many=True)

    class Meta:
        model = Accessory
        fields = ['manufacturer', 'model', 'type', 'acquired', 'cost', 'lost',
                  'lost_price', 'camera_model_compatibility', 'lens_model_compatibility']


class LensModelSerializer(ModelSerializer):
    manufacturer = ManufacturerSerializer(many=False)
    negative_size = NegativeSizeSerializer(many=False)
    mount = MountSerializer(many=False)

    class Meta:
        model = LensModel
        fields = ['manufacturer', 'model', 'disambiguation', 'mount', 'introduced', 'discontinued', 'zoom', 'min_focal_length', 'max_focal_length', 'max_aperture', 'min_aperture', 'closest_focus', 'elements', 'groups', 'nominal_min_angle_diag', 'nominal_max_angle_diag', 'lens_type', 'image_circle', 'aperture_blades',
                  'coating', 'autofocus', 'perspective_control', 'magnification', 'negative_size', 'weight', 'length', 'diameter', 'filter_thread', 'hood', 'shutter_model', 'notes', 'linkurl', 'image', 'image_attribution', 'image_attribution_url', 'diagram', 'diagram_attribution', 'diagram_attribution_url']


class LensSerializer(ModelSerializer):
    lensmodel = LensModelSerializer(many=False, read_only=True)

    class Meta:
        model = Lens
        fields = ['lensmodel', 'serial', 'date_code', 'manufactured', 'acquired', 'cost',
                  'notes', 'own', 'lost', 'lost_price', 'source', 'condition', 'condition_notes']


class CameraModelSerializer(ModelSerializer):
    manufacturer = ManufacturerSerializer(many=False)
    format = FormatSerializer(many=False)
    negative_size = NegativeSizeSerializer(many=False)
    mount = MountSerializer(many=False)
    lens_manufacturer = ManufacturerSerializer(many=False)
    metering_modes = StringRelatedField(many=True)
    exposure_programs = StringRelatedField(many=True)
    battery_type = BatterySerializer(many=False)

    class Meta:
        model = CameraModel
        fields = [ 'manufacturer', 'model', 'other_names', 'disambiguation', 'introduced', 'discontinued', 'format',
                'negative_size', 'mount', 'lens_manufacturer', 'lens_model_name', 'zoom', 'min_focal_length',
                'max_focal_length', 'max_aperture', 'min_aperture', 'closest_focus', 'elements', 'groups',
                'nominal_min_angle_diag', 'nominal_max_angle_diag', 'aperture_blades', 'coating', 'magnification',
                'filter_thread', 'hood', 'body_type', 'weight', 'focus_type', 'af_points', 'viewfinder_coverage',
                'metering', 'metering_type', 'min_iso', 'max_iso', 'meter_min_ev', 'meter_max_ev', 'metering_modes',
                'exposure_programs', 'shutter_type', 'shutter_model', 'fastest_shutter_speed', 'slowest_shutter_speed',
                'bulb', 'time', 'internal_power_drive', 'continuous_fps', 'external_power_drive', 'battery_qty', 'battery_type',
                'int_flash', 'int_flash_gn', 'ext_flash', 'pc_sync', 'shoe', 'x_sync', 'dof_preview', 'mirror_lockup', 'tripod',
                'self_timer', 'date_imprint', 'cable_release', 'interchangeable_backs', 'interchangeable_finders', 'strap_lugs',
                'multiple_exposures', 'notes', 'linkurl', 'image', 'image_attribution', 'image_attribution_url' ]


class CameraSerializer(ModelSerializer):
    cameramodel = CameraModelSerializer(read_only=True)

    class Meta:
        model = Camera
        fields = ['cameramodel', 'acquired', 'cost', 'source', 'serial', 'datecode',
                  'manufactured', 'own', 'notes', 'lost', 'lost_price', 'condition', 'condition_notes']


class FilmSerializer(ModelSerializer):
    filmstock = FilmStockSerializer(many=False)
    format = FormatSerializer(many=False)
    camera = CameraSerializer(many=False)
    developer = DeveloperSerializer(many=False)
    bulk_film = BulkFilmSerializer(many=False)
    archive = ArchiveSerializer(many=False)

    class Meta:
        model = Film
        fields = ['filmstock', 'exposed_at', 'format', 'status', 'date_loaded', 'date_processed', 'camera', 'title', 'frames', 'developer', 'developer_previous_uses', 'development_time',
                  'development_temperature', 'development_compensation', 'development_notes', 'bulk_film', 'bulk_film_loaded', 'film_batch', 'expiry_date', 'purchase_date', 'price', 'processed_by', 'archive']


class NegativeSerializer(ModelSerializer):
    film = FilmSerializer(many=False)
    lens = LensSerializer(many=False)
    filter = FilterSerializer(many=False)
 #   teleconverter = TeleconverterSerializer(many=False)
    mount_adapter = MountAdapterSerializer(many=False)
 #   exposure_program = StringRelatedField(many=False)
 #   metering_mode = StringRelatedField(many=False)
  #  shutter_speed = StringRelatedField(many=False)

    class Meta:
        model = Negative
        fields = ['film', 'frame', 'caption', 'date', 'lens', 'shutter_speed', 'aperture', 'filter', 'teleconverter', 'notes',
                  'mount_adapter', 'focal_length', 'location', 'flash', 'metering_mode', 'exposure_program', 'photographer', 'copy_of']


class PrintSerializer(ModelSerializer):
    negative = NegativeSerializer(many=False, read_only=True)
    paper_stock = PaperStockSerializer(many=False)
    enlarger = EnlargerSerializer(many=False)
    lens = LensSerializer(many=False)
    developer = DeveloperSerializer(many=False)
    archive = ArchiveSerializer(many=False)

    class Meta:
        model = Print
        fields = ['negative', 'date', 'paper_stock', 'height', 'width', 'aperture', 'exposure_time', 'filtration_grade', 'development_time',
                  'toner', 'own', 'location', 'sold_price', 'enlarger', 'lens', 'developer', 'fine', 'notes', 'archive', 'printer']


class ScanSerializer(ModelSerializer):
    negative = NegativeSerializer(many=False)
    print = PrintSerializer(many=False)

    class Meta:
        model = Scan
        fields = ['uuid', 'negative', 'print', 'filename']


class OrderSerializer(ModelSerializer):
    negative = NegativeSerializer(many=False)
    print = PrintSerializer(many=False)

    class Meta:
        model = Order
        fields = ['negative', 'width', 'height',
                  'added', 'printed', 'print', 'recipient']
