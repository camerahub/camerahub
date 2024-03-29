from fractions import Fraction
from rest_framework.serializers import ModelSerializer, StringRelatedField, DecimalField, CharField, IntegerField, SerializerMethodField
from schema.models import Accessory, Archive,  Battery, Camera, CameraModel, Filter, NegativeSize, Film, Format
from schema.models import FlashModel, Flash, EnlargerModel, Enlarger, LensModel, Manufacturer, Mount, Negative, PaperStock
from schema.models import Person, Process, TeleconverterModel, Teleconverter, Toner, FilmStock, BulkFilm, MountAdapter, Developer
from schema.models import Lens, Print, Scan, MeteringMode, ExposureProgram, ShutterSpeed
from schema.funcs import deg_to_dms_rational, gps_ref


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


class ShutterSpeedSerializer(ModelSerializer):

    class Meta:
        model = ShutterSpeed
        fields = '__all__'


class NegativeSerializer(ModelSerializer):
    film = FilmSerializer(many=False)
    lens = LensSerializer(many=False)
    filter = FilterSerializer(many=False)
    teleconverter = TeleconverterSerializer(many=False)
    mount_adapter = MountAdapterSerializer(many=False)
    exposure_program = ExposureProgramSerializer(many=False)
    metering_mode = MeteringModeSerializer(many=False)
    shutter_speed = ShutterSpeedSerializer(many=False)
    photographer = PersonSerializer(many=False)
    copyright = CharField()
    latitude = DecimalField(max_digits=18, decimal_places=15)
    longitude = DecimalField(max_digits=18, decimal_places=15)
    focal_length = IntegerField()

    class Meta:
        model = Negative
        fields = '__all__'


class ExifSerializer(ModelSerializer):

    # These fields must take the correct name and data type of actual EXIF tags
    # https://exiv2.org/tags.html
    ImageUniqueID = CharField(source='uuid')
    Make = CharField(
        source="negative.film.camera.cameramodel.manufacturer.name", default=None)
    Model = SerializerMethodField(default=None)
    BodySerialNumber = CharField(
        source="negative.film.camera.serial", default=None)
    UserComment = CharField(source='negative.notes', default=None)
    # rational
    FocalLength = SerializerMethodField(default=None)
    FocalLengthIn35mmFilm = IntegerField(source='negative.focal_length_35mm', default=None)
    ExposureTime = SerializerMethodField(default=None)
    Copyright = CharField(source='negative.copyright', default=None)
    ISOSpeed = IntegerField(source='negative.film.exposed_at', default=None)
    ImageDescription = SerializerMethodField(default=None)
    LensSerialNumber = CharField(source='negative.lens.serial', default=None)
    Artist = CharField(source='negative.photographer.name', default=None)
    # rational
    FNumber = SerializerMethodField(default=None)
    DateTimeOriginal = SerializerMethodField(default=None)
    ExposureProgram = IntegerField(
        source='negative.exposure_program.id', default=None)
    MeteringMode = IntegerField(
        source='negative.metering_mode.id', default=None)
    Flash = IntegerField(source='negative.flash', default=None)
    LensModel = SerializerMethodField(default=None)
    LensMake = SerializerMethodField(default=None)
    GPSLatitude = SerializerMethodField(default=None)
    GPSLatitudeRef = SerializerMethodField(default=None)
    GPSLongitude = SerializerMethodField(default=None)
    GPSLongitudeRef = SerializerMethodField(default=None)
    ImageID = CharField(source='filename', default=None)
    DocumentName = SerializerMethodField(default=None)

    def get_DocumentName(self, obj):
        """
        Return either the Negative or Print slug
        """
        if obj.print and obj.print.id_owner:
            documentname = f"Print #{obj.print.id_owner}"
        elif obj.negative and obj.negative.slug:
            documentname = f"Negative #{obj.negative.slug}"
        else:
            documentname = None
        return documentname

    def get_DateTimeOriginal(self, obj):
        """
        Return the Negative taken date, if there is one.
        Otherwise return the Film processed date, if there is one.
        """
        try:
            negdate = obj.negative.date
        except (ValueError, AttributeError):
            negdate = None

        if negdate is None:
            try:
                filmdate = obj.negative.film.date_processed
            except (ValueError, AttributeError):
                filmdate = None

        if negdate:
            returnval = negdate.strftime('%Y:%m:%d %H:%M:%S')
        elif filmdate:
            returnval = filmdate.strftime('%Y:%m:%d %H:%M:%S')
        else:
            returnval = None

        return returnval 

    def get_ImageDescription(self, obj):
        try:
            caption = obj.negative.caption
        except (ValueError, AttributeError):
            caption = None

        try:
            if obj.print:
                slug = f"P{obj.print.id_owner}"
            else:
                slug = f"#{obj.negative.slug}"
        except (ValueError, AttributeError):
            slug = None

        if caption:
            returnval = f"{slug} {caption}"
        else:
            returnval = slug
        return returnval

    def get_FocalLength(self, obj):
        try:
            fraction = Fraction(str(obj.negative.focal_length))
        except (ValueError, AttributeError):
            returnval = None
        else:
            returnval = f'{fraction.numerator}/{fraction.denominator}'
        return returnval

    def get_ExposureTime(self, obj):
        try:
            # Shutter speed could be formatted 1/60 or 1"
            fraction = Fraction(str(obj.negative.shutter_speed.shutter_speed).replace('"', ''))
        except (ValueError, AttributeError):
            returnval = None
        else:
            returnval = f'{fraction.numerator}/{fraction.denominator}'
        return returnval

    def get_FNumber(self, obj):
        try:
            fraction = Fraction(str(obj.negative.aperture))
        except (ValueError, AttributeError):
            returnval = None
        else:
            returnval = f'{fraction.numerator}/{fraction.denominator}'
        return returnval

    def get_GPSLatitude(self, obj):
        try:
            returnval = deg_to_dms_rational(obj.negative.latitude)
        except (TypeError, ValueError, AttributeError):
            returnval = None
        return returnval

    def get_GPSLatitudeRef(self, obj):
        try:
            returnval = gps_ref('latitude', obj.negative.latitude)
        except (TypeError, ValueError, AttributeError):
            returnval = None
        return returnval

    def get_GPSLongitude(self, obj):
        try:
            returnval = deg_to_dms_rational(obj.negative.longitude)
        except (TypeError, ValueError, AttributeError):
            returnval = None
        return returnval

    def get_GPSLongitudeRef(self, obj):
        try:
            returnval = gps_ref('longitude', obj.negative.longitude)
        except (TypeError, ValueError, AttributeError):
            returnval = None
        return returnval

    def get_Model(self, obj):
        try:
            returnval = f'{obj.negative.film.camera.cameramodel.manufacturer.name} {obj.negative.film.camera.cameramodel.model}'
        except (ValueError, AttributeError):
            returnval = None
        return returnval

    def get_LensModel(self, obj):
        try:
            if obj.negative.film.camera.cameramodel.interchangeable_lens is True:
                returnval = f'{obj.negative.lens.lensmodel.manufacturer.name} {obj.negative.lens.lensmodel.model}'
            else:
                returnval = f'{obj.negative.film.camera.cameramodel.lens_manufacturer.name} {obj.negative.film.camera.cameramodel.lens_model_name}'
        except (ValueError, AttributeError):
            returnval = None
        return returnval

    def get_LensMake(self, obj):
        try:
            if obj.negative.film.camera.cameramodel.interchangeable_lens is True:
                returnval = obj.negative.lens.lensmodel.manufacturer.name
            else:
                returnval = obj.negative.film.camera.cameramodel.lens_manufacturer.name
        except (ValueError, AttributeError):
            returnval = None
        return returnval

    class Meta:
        model = Scan
        fields = [
            'ImageUniqueID',
            'Make',
            'Model',
            'BodySerialNumber',
            'UserComment',
            'FocalLength',
            'FocalLengthIn35mmFilm',
            'Copyright',
            'ISOSpeed',
            'ImageDescription',
            'LensSerialNumber',
            'LensModel',
            'LensMake',
            'Artist',
            'FNumber',
            'DateTimeOriginal',
            'ExposureProgram',
            'MeteringMode',
            'Flash',
            'GPSLatitude',
            'GPSLatitudeRef',
            'GPSLongitude',
            'GPSLongitudeRef',
            'ExposureTime',
            'ImageID',
            'DocumentName',
        ]


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
