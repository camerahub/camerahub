from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, StringRelatedField
from schema.models import Accessory, Archive,  Battery, Camera, CameraModel, Condition, ExposureProgram, Filter, NegativeSize, Film, Format
from schema.models import FlashModel, Flash, EnlargerModel, Enlarger, LensModel, Manufacturer, MeteringMode, Mount, Negative, PaperStock
from schema.models import Person, Process, TeleconverterModel, Teleconverter, Toner, FilmStock, BulkFilm, MountAdapter, ShutterSpeed, Developer
from schema.models import LensModel, CameraModel, Lens, Film, Negative, Print, Toning, Scan, Order

class LensModelSerializer(HyperlinkedModelSerializer):
    manufacturer = StringRelatedField(many=False)

    class Meta:
        model = LensModel
        fields = ['manufacturer', 'model', ]


class LensSerializer(HyperlinkedModelSerializer):
    lensmodel = LensModelSerializer(many=False, read_only=True)

    class Meta:
        model = Lens
        fields = ['url', 'serial', 'lensmodel']


class CameraModelSerializer(HyperlinkedModelSerializer):
    manufacturer = StringRelatedField(many=False)

    class Meta:
        model = CameraModel
        fields = ['manufacturer', 'model', ]


class CameraSerializer(HyperlinkedModelSerializer):
    cameramodel = CameraModelSerializer(many=False, read_only=True)

    class Meta:
        model = Camera
        fields = ['url', 'serial', 'lensmodel']


class FilmSerializer(HyperlinkedModelSerializer):
    camera = CameraSerializer

    class Meta:
        model = Film
        fields = ['url', 'id_owner', 'title', 'camera']


class NegativeSerializer(HyperlinkedModelSerializer):
    film_id = StringRelatedField(many=False)
    filter = StringRelatedField(many=False)
    teleconverter = StringRelatedField(many=False)
    exposure_program = StringRelatedField(many=False)
    metering_mode = StringRelatedField(many=False)

    lens = LensSerializer(many=False, read_only=True)
    film = FilmSerializer(many=False, read_only=True)
    shutter_speed = StringRelatedField(many=False)

    class Meta:
        model = Negative
        fields = ['url', 'slug', 'film', 'film_id', 'id_owner', 'frame', 'caption', 'date', 'lens', 'shutter_speed', 'aperture', 'filter', 'teleconverter',
                  'notes', 'mount_adapter', 'focal_length', 'location', 'flash', 'metering_mode', 'exposure_program', 'photographer', 'copy_of']


class PrintSerializer(HyperlinkedModelSerializer):
    negative = NegativeSerializer(many=False, read_only=True)

    class Meta:
        model = Print
        fields = ['pk', 'url', 'negative']


class ScanSerializer(HyperlinkedModelSerializer):
    negative = NegativeSerializer(many=False, read_only=True)
    print = PrintSerializer(many=False, read_only=True)

    class Meta:
        model = Scan
        fields = ['uuid', 'url', 'negative', 'print', 'filename']


class ManufacturerSerializer(ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = '__all__'


class ArchiveSerializer(ModelSerializer):

    class Meta:
        model = Archive
        fields = '__all__'


class BatterySerializer(ModelSerializer):

    class Meta:
        model = Battery
        fields = '__all__'


class ConditionSerializer(ModelSerializer):

    class Meta:
        model = Condition
        fields = '__all__'


class ExposureProgramSerializer(ModelSerializer):

    class Meta:
        model = ExposureProgram
        fields = '__all__'


class FilterSerializer(ModelSerializer):

    class Meta:
        model = Filter
        fields = '__all__'


class NegativeSizeSerializer(ModelSerializer):

    class Meta:
        model = NegativeSize
        fields = '__all__'


class FormatSerializer(ModelSerializer):

    class Meta:
        model = Format
        fields = '__all__'


class FlashModelSerializer(ModelSerializer):

    class Meta:
        model = FlashModel
        fields = '__all__'


class FlashSerializer(ModelSerializer):

    class Meta:
        model = Flash
        fields = '__all__'


class EnlargerModelSerializer(ModelSerializer):

    class Meta:
        model = EnlargerModel
        fields = '__all__'


class EnlargerSerializer(ModelSerializer):

    class Meta:
        model = Enlarger
        fields = '__all__'


class MeteringModeSerializer(ModelSerializer):

    class Meta:
        model = MeteringMode
        fields = '__all__'


class MountSerializer(ModelSerializer):

    class Meta:
        model = Mount
        fields = '__all__'


class PaperStockSerializer(ModelSerializer):

    class Meta:
        model = PaperStock
        fields = '__all__'


class PersonSerializer(ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'


class ProcessSerializer(ModelSerializer):

    class Meta:
        model = Process
        fields = '__all__'


class TeleconverterModelSerializer(ModelSerializer):

    class Meta:
        model = TeleconverterModel
        fields = '__all__'


class TeleconverterSerializer(ModelSerializer):

    class Meta:
        model = Teleconverter
        fields = '__all__'


class TonerSerializer(ModelSerializer):

    class Meta:
        model = Toner
        fields = '__all__'


class FilmStockSerializer(ModelSerializer):

    class Meta:
        model = FilmStock
        fields = '__all__'


class BulkFilmSerializer(ModelSerializer):

    class Meta:
        model = BulkFilm
        fields = '__all__'


class MountAdapterSerializer(ModelSerializer):

    class Meta:
        model = MountAdapter
        fields = '__all__'


class ShutterSpeedSerializer(ModelSerializer):

    class Meta:
        model = ShutterSpeed
        fields = '__all__'


class DeveloperSerializer(ModelSerializer):

    class Meta:
        model = Developer
        fields = '__all__'


class AccessorySerializer(ModelSerializer):

    class Meta:
        model = Accessory
        fields = '__all__'


class ToningSerializer(ModelSerializer):

    class Meta:
        model = Toning
        fields = '__all__'


class OrderSerializer(ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
