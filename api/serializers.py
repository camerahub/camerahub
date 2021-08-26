from rest_framework.serializers import ModelSerializer, StringRelatedField, DecimalField, CharField, IntegerField
from schema.models import Accessory, Archive,  Battery, Camera, CameraModel, Filter, NegativeSize, Film, Format
from schema.models import FlashModel, Flash, EnlargerModel, Enlarger, LensModel, Manufacturer, Mount, Negative, PaperStock
from schema.models import Person, Process, TeleconverterModel, Teleconverter, Toner, FilmStock, BulkFilm, MountAdapter, Developer
from schema.models import Lens, Print, Scan, Order, MeteringMode, ExposureProgram, ShutterSpeed

class ExposureProgramSerializer(ModelSerializer):

    class Meta:
        model = ExposureProgram
        fields = '__all__'


class MeteringModeSerializer(ModelSerializer):

    class Meta:
        model = MeteringMode
        fields = '__all__'


class ManufacturerSerializer(ModelSerializer):
    country = StringRelatedField(many=False)

    class Meta:
        model = Manufacturer
        fields = '__all__'


class MountSerializer(ModelSerializer):
    manufacturer = ManufacturerSerializer(many=False)

    class Meta:
        model = Mount
        fields = '__all__'


class NegativeSizeSerializer(ModelSerializer):

    class Meta:
        model = NegativeSize
        fields = '__all__'


class PersonSerializer(ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'


class ProcessSerializer(ModelSerializer):

    class Meta:
        model = Process
        fields = '__all__'


class FormatSerializer(ModelSerializer):
    negative_size = NegativeSizeSerializer(many=False)

    class Meta:
        model = Format
        fields = '__all__'


class BatterySerializer(ModelSerializer):

    class Meta:
        model = Battery
        fields = '__all__'


class FilmStockSerializer(ModelSerializer):
    manufacturer = ManufacturerSerializer(many=False)
    process = ProcessSerializer(many=False)

    class Meta:
        model = FilmStock
        fields = '__all__'


class ArchiveSerializer(ModelSerializer):

    class Meta:
        model = Archive
        fields = '__all__'


class FilterSerializer(ModelSerializer):

    class Meta:
        model = Filter
        fields = '__all__'


class FlashModelSerializer(ModelSerializer):
    manufacturer = ManufacturerSerializer(many=False)
    battery_type = BatterySerializer(many=False)

    class Meta:
        model = FlashModel
        fields = '__all__'


class FlashSerializer(ModelSerializer):
    flashmodel = FlashModelSerializer(many=False)

    class Meta:
        model = Flash
        fields = '__all__'


class EnlargerModelSerializer(ModelSerializer):
    manufacturer = ManufacturerSerializer(many=False)
    negative_size = NegativeSizeSerializer(many=False)

    class Meta:
        model = EnlargerModel
        fields = '__all__'


class EnlargerSerializer(ModelSerializer):
    enlargermodel = EnlargerModelSerializer(many=False)

    class Meta:
        model = Enlarger
        fields = '__all__'


class PaperStockSerializer(ModelSerializer):
    manufacturer = ManufacturerSerializer(many=False)

    class Meta:
        model = PaperStock
        fields = '__all__'


class TeleconverterModelSerializer(ModelSerializer):
    manufacturer = ManufacturerSerializer(many=False)
    mount = MountSerializer(many=False)

    class Meta:
        model = TeleconverterModel
        fields = '__all__'


class TeleconverterSerializer(ModelSerializer):
    teleconvertermodel = TeleconverterModelSerializer(many=False)

    class Meta:
        model = Teleconverter
        fields = '__all__'


class TonerSerializer(ModelSerializer):
    manufacturer = ManufacturerSerializer(many=False)

    class Meta:
        model = Toner
        fields = '__all__'


class BulkFilmSerializer(ModelSerializer):
    format = FormatSerializer(many=False)
    filmstock = FilmStockSerializer(many=False)

    class Meta:
        model = BulkFilm
        fields = '__all__'


class MountAdapterSerializer(ModelSerializer):
    camera_mount = MountSerializer(many=False)
    lens_mount = MountSerializer(many=False)

    class Meta:
        model = MountAdapter
        fields = '__all__'


class DeveloperSerializer(ModelSerializer):
    manufacturer = ManufacturerSerializer(many=False)

    class Meta:
        model = Developer
        fields = '__all__'


class AccessorySerializer(ModelSerializer):
    manufacturer = ManufacturerSerializer(many=False)
    camera_model_compatibility = StringRelatedField(many=True)
    lens_model_compatibility = StringRelatedField(many=True)

    class Meta:
        model = Accessory
        fields = '__all__'


class LensModelSerializer(ModelSerializer):
    manufacturer = ManufacturerSerializer(many=False)
    negative_size = NegativeSizeSerializer(many=False)
    mount = MountSerializer(many=False)

    class Meta:
        model = LensModel
        fields = '__all__'


class LensSerializer(ModelSerializer):
    lensmodel = LensModelSerializer(many=False, read_only=True)

    class Meta:
        model = Lens
        fields = '__all__'


class CameraModelSerializer(ModelSerializer):
    manufacturer = ManufacturerSerializer(many=False)
    format = FormatSerializer(many=False)
    negative_size = NegativeSizeSerializer(many=False)
    mount = MountSerializer(many=False)
    lens_manufacturer = ManufacturerSerializer(many=False)
    metering_modes = MeteringModeSerializer(many=True)
    exposure_programs = ExposureProgramSerializer(many=True)
    battery_type = BatterySerializer(many=False)

    class Meta:
        model = CameraModel
        fields = '__all__'


class CameraSerializer(ModelSerializer):
    cameramodel = CameraModelSerializer(read_only=True)

    class Meta:
        model = Camera
        fields = '__all__'


class FilmSerializer(ModelSerializer):
    filmstock = FilmStockSerializer(many=False)
    format = FormatSerializer(many=False)
    camera = CameraSerializer(many=False)
    developer = DeveloperSerializer(many=False)
    bulk_film = BulkFilmSerializer(many=False)
    archive = ArchiveSerializer(many=False)

    class Meta:
        model = Film
        fields = '__all__'


class NegativeSerializer(ModelSerializer):
    film = FilmSerializer(many=False)
    lens = LensSerializer(many=False)
    filter = FilterSerializer(many=False)
    teleconverter = TeleconverterSerializer(many=False)
    mount_adapter = MountAdapterSerializer(many=False)
    exposure_program = ExposureProgramSerializer(many=False)
    metering_mode = MeteringModeSerializer(many=False)
    shutter_speed = StringRelatedField(many=False)
    photographer = PersonSerializer(many=False)
    copyright = CharField()
    latitude = DecimalField(max_digits=18, decimal_places=15)
    longitude = DecimalField(max_digits=18, decimal_places=15)
    focal_length = IntegerField()

    class Meta:
        model = Negative
        fields = '__all__'


class PrintSerializer(ModelSerializer):
    negative = NegativeSerializer(many=False, read_only=True)
    paper_stock = PaperStockSerializer(many=False)
    enlarger = EnlargerSerializer(many=False)
    lens = LensSerializer(many=False)
    developer = DeveloperSerializer(many=False)
    archive = ArchiveSerializer(many=False)

    class Meta:
        model = Print
        fields = '__all__'


class ScanSerializer(ModelSerializer):
    negative = NegativeSerializer(many=False)
    print = PrintSerializer(many=False)

    class Meta:
        model = Scan
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    negative = NegativeSerializer(many=False)
    print = PrintSerializer(many=False)

    class Meta:
        model = Order
        fields = '__all__'

class ShutterSpeedSerializer(ModelSerializer):

    class Meta:
        model = ShutterSpeed
        fields = '__all__'
