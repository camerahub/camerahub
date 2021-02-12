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

    class Meta:
        model = Mount
        fields = ['mount', 'shutter_in_lens', 'type',
                  'purpose', 'notes', 'manufacturer' ]

class NegativeSizeSerializer(ModelSerializer):

    class Meta:
        model = NegativeSize
        fields = [ 'name', 'width', 'height', ]


class LensModelSerializer(ModelSerializer):
    #manufacturer = StringRelatedField(many=False)
    manufacturer = ManufacturerSerializer(many=False)
    negative_size = NegativeSizeSerializer()
    mount = MountSerializer()

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
    #manufacturer = StringRelatedField(many=False)

    class Meta:
        model = CameraModel
        fields = '__all__'


class CameraSerializer(ModelSerializer):
    cameramodel = CameraModelSerializer(read_only=True)

    class Meta:
        model = Camera
        fields = ['cameramodel', 'acquired', 'cost', 'source', 'serial', 'datecode',
                  'manufactured', 'own', 'notes', 'lost', 'lost_price', 'condition', 'condition_notes']


class FilmSerializer(ModelSerializer):
    #camera = CameraSerializer

    class Meta:
        model = Film
        fields = ['filmstock', 'exposed_at', 'format', 'status', 'date_loaded', 'date_processed', 'camera', 'title', 'frames', 'developer', 'developer_previous_uses', 'development_time',
                  'development_temperature', 'development_compensation', 'development_notes', 'bulk_film', 'bulk_film_loaded', 'film_batch', 'expiry_date', 'purchase_date', 'price', 'processed_by', 'archive']


class NegativeSerializer(ModelSerializer):
 #   film_id = StringRelatedField(many=False)
 #   filter = StringRelatedField(many=False)
 #   teleconverter = StringRelatedField(many=False)
 #   exposure_program = StringRelatedField(many=False)
 #   metering_mode = StringRelatedField(many=False)

  #  lens = LensSerializer(many=False, read_only=True)
  #  film = FilmSerializer(many=False, read_only=True)
  #  shutter_speed = StringRelatedField(many=False)

    class Meta:
        model = Negative
        fields = ['film', 'frame', 'caption', 'date', 'lens', 'shutter_speed', 'aperture', 'filter', 'teleconverter', 'notes',
                  'mount_adapter', 'focal_length', 'location', 'flash', 'metering_mode', 'exposure_program', 'photographer', 'copy_of']


class PrintSerializer(ModelSerializer):
  #  negative = NegativeSerializer(many=False, read_only=True)

    class Meta:
        model = Print
        fields = ['negative', 'date', 'paper_stock', 'height', 'width', 'aperture', 'exposure_time', 'filtration_grade', 'development_time',
                  'toner', 'own', 'location', 'sold_price', 'enlarger', 'lens', 'developer', 'fine', 'notes', 'archive', 'printer']


class ScanSerializer(ModelSerializer):
   # negative = NegativeSerializer(many=False, read_only=True)
   # print = PrintSerializer(many=False, read_only=True)

    class Meta:
        model = Scan
        fields = ['uuid', 'url', 'negative', 'print', 'filename']


class ArchiveSerializer(ModelSerializer):

    class Meta:
        model = Archive
        fields = ['name', 'type', 'max_width',
                  'max_height', 'location', 'storage', 'sealed']


class BatterySerializer(ModelSerializer):

    class Meta:
        model = Battery
        fields = ['name', 'voltage', 'chemistry', 'compatible_with']


class FilterSerializer(ModelSerializer):

    class Meta:
        model = Filter
        fields = ['type', 'shortname', 'attenuation']


class FormatSerializer(ModelSerializer):

    class Meta:
        model = Format
        fields = ['format', 'negative_size']


class FlashModelSerializer(ModelSerializer):

    class Meta:
        model = FlashModel
        fields = ['manufacturer', 'model', 'disambiguation', 'guide_number', 'gn_info', 'battery_powered', 'pc_sync', 'hot_shoe', 'light_stand', 'battery_type',
                  'battery_qty', 'manual_control', 'swivel_head', 'tilt_head', 'zoom', 'ttl', 'trigger_voltage', 'image', 'image_attribution', 'image_attribution_url']


class FlashSerializer(ModelSerializer):

    class Meta:
        model = Flash
        fields = ['flashmodel', 'serial', 'own',
                  'acquired', 'cost', 'lost', 'lost_price']


class EnlargerModelSerializer(ModelSerializer):

    class Meta:
        model = EnlargerModel
        fields = ['manufacturer', 'model', 'disambiguation', 'negative_size',
                  'type', 'light_source', 'introduced', 'discontinued', 'image', 'image_attribution', 'image_attribution_url']


class EnlargerSerializer(ModelSerializer):

    class Meta:
        model = Enlarger
        fields = ['enlargermodel', 'serial', 'own',
                  'acquired', 'cost', 'lost', 'lost_price']


class PaperStockSerializer(ModelSerializer):

    class Meta:
        model = PaperStock
        fields = ['name', 'manufacturer',
                  'resin_coated', 'colour', 'finish' ]


class PersonSerializer(ModelSerializer):

    class Meta:
        model = Person
        fields = ['name']


class ProcessSerializer(ModelSerializer):

    class Meta:
        model = Process
        fields = ['name', 'colour', 'positive']


class TeleconverterModelSerializer(ModelSerializer):

    class Meta:
        model = TeleconverterModel
        fields = ['model', 'manufacturer', 'disambiguation', 'mount',
                  'factor', 'elements', 'groups', 'multicoated', 'image', 'image_attribution', 'image_attribution_url']


class TeleconverterSerializer(ModelSerializer):

    class Meta:
        model = Teleconverter
        fields = ['teleconvertermodel', 'serial', 'own',
                  'acquired', 'cost', 'lost', 'lost_price', ]


class TonerSerializer(ModelSerializer):

    class Meta:
        model = Toner
        fields = [ 'name', 'manufacturer', 'formulation', 'stock_dilution', 'tags', ]


class FilmStockSerializer(ModelSerializer):

    class Meta:
        model = FilmStock
        fields = ['name', 'manufacturer', 'iso',
                  'colour', 'panchromatic', 'process', ]


class BulkFilmSerializer(ModelSerializer):

    class Meta:
        model = BulkFilm
        fields = ['format', 'filmstock', 'length', 'finished', 'purchase_date',
                  'cost', 'source', 'batch', 'expiry']


class MountAdapterSerializer(ModelSerializer):

    class Meta:
        model = MountAdapter
        fields = ['mount', 'shutter_in_lens', 'type',
                  'purpose', 'notes', 'manufacturer' ]


class DeveloperSerializer(ModelSerializer):

    class Meta:
        model = Developer
        fields = ['manufacturer', 'name', 'for_paper',
                  'for_film', 'chemistry' ]


class AccessorySerializer(ModelSerializer):

    class Meta:
        model = Accessory
        fields = ['manufacturer', 'model', 'type', 'acquired', 'cost', 'lost',
                  'lost_price', 'camera_model_compatibility', 'lens_model_compatibility']


class OrderSerializer(ModelSerializer):

    class Meta:
        model = Order
        fields = ['negative', 'width', 'height',
                  'added', 'printed', 'print', 'recipient']
