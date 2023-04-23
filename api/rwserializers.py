from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, SlugRelatedField
from schema.models import Accessory, Archive, BulkFilm, Camera, CameraModel, Developer, Enlarger, EnlargerModel
from schema.models import ExposureProgram, Film, FilmStock, Filter, Flash, FlashModel, Format, Lens
from schema.models import LensModel, Manufacturer, MeteringMode, Mount, MountAdapter, Negative
from schema.models import PaperStock, Person, Print, Scan, ShutterSpeed, Teleconverter, TeleconverterModel


class PersonRWSerializer(ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'


class ArchiveRWSerializer(ModelSerializer):

    class Meta:
        model = Archive
        fields = '__all__'


class FlashRWSerializer(ModelSerializer):
    flashmodel = PrimaryKeyRelatedField(queryset=FlashModel.objects.all())

    class Meta:
        model = Flash
        fields = '__all__'


class EnlargerRWSerializer(ModelSerializer):
    enlargermodel = PrimaryKeyRelatedField(
        queryset=EnlargerModel.objects.all())

    class Meta:
        model = Enlarger
        fields = '__all__'


class TeleconverterRWSerializer(ModelSerializer):
    teleconvertermodel = PrimaryKeyRelatedField(
        queryset=TeleconverterModel.objects.all())

    class Meta:
        model = Teleconverter
        fields = '__all__'


class BulkFilmRWSerializer(ModelSerializer):
    format = PrimaryKeyRelatedField(queryset=Format.objects.all())
    filmstock = PrimaryKeyRelatedField(queryset=FilmStock.objects.all())

    class Meta:
        model = BulkFilm
        fields = '__all__'


class MountAdapterRWSerializer(ModelSerializer):
    camera_mount = PrimaryKeyRelatedField(queryset=Mount.objects.all())
    lens_mount = PrimaryKeyRelatedField(queryset=Mount.objects.all())

    class Meta:
        model = MountAdapter
        fields = '__all__'


class AccessoryRWSerializer(ModelSerializer):
    manufacturer = PrimaryKeyRelatedField(
        queryset=Manufacturer.objects.all(), required=False)
    camera_model_compatibility = PrimaryKeyRelatedField(
        many=True, queryset=CameraModel.objects.all(), required=False)
    lens_model_compatibility = PrimaryKeyRelatedField(
        many=True, queryset=LensModel.objects.all(), required=False)

    class Meta:
        model = Accessory
        fields = '__all__'


class LensRWSerializer(ModelSerializer):
    lensmodel = PrimaryKeyRelatedField(
        many=True, queryset=LensModel.objects.all())

    class Meta:
        model = Lens
        fields = '__all__'


class CameraRWSerializer(ModelSerializer):
    cameramodel = PrimaryKeyRelatedField(
        many=True, queryset=CameraModel.objects.all())

    class Meta:
        model = Camera
        fields = '__all__'


class FilmRWSerializer(ModelSerializer):
    filmstock = PrimaryKeyRelatedField(
        queryset=FilmStock.objects.all(), required=False)
    format = PrimaryKeyRelatedField(
        queryset=Format.objects.all(), required=False)
    camera = SlugRelatedField(slug_field='id_owner',
                              queryset=Camera.objects.all(), required=False)
    developer = PrimaryKeyRelatedField(
        queryset=Developer.objects.all(), required=False)
    bulk_film = PrimaryKeyRelatedField(
        queryset=BulkFilm.objects.all(), required=False)
    archive = PrimaryKeyRelatedField(
        queryset=Archive.objects.all(), required=False)

    class Meta:
        model = Film
        fields = '__all__'


class NegativeRWSerializer(ModelSerializer):
    film = SlugRelatedField(slug_field='id_owner', queryset=Film.objects.all())
    lens = SlugRelatedField(slug_field='id_owner',
                            queryset=Lens.objects.all(), required=False)
    filter = PrimaryKeyRelatedField(
        queryset=Filter.objects.all(), required=False)
    teleconverter = SlugRelatedField(
        slug_field='id_owner', queryset=Teleconverter.objects.all(), required=False)
    mount_adapter = PrimaryKeyRelatedField(
        queryset=MountAdapter.objects.all(), required=False)
    exposure_program = PrimaryKeyRelatedField(
        queryset=ExposureProgram.objects.all(), required=False)
    metering_mode = PrimaryKeyRelatedField(
        queryset=MeteringMode.objects.all(), required=False)
    shutter_speed = PrimaryKeyRelatedField(
        queryset=ShutterSpeed.objects.all(), required=False)

    class Meta:
        model = Negative
        fields = '__all__'


class PrintRWSerializer(ModelSerializer):
    negative = SlugRelatedField(
        slug_field='slug', queryset=Negative.objects.all())
    paper_stock = PrimaryKeyRelatedField(
        queryset=PaperStock.objects.all(), required=False)
    enlarger = SlugRelatedField(
        slug_field='id_owner', queryset=Enlarger.objects.all(), required=False)
    lens = SlugRelatedField(slug_field='id_owner',
                            queryset=Lens.objects.all(), required=False)
    developer = PrimaryKeyRelatedField(
        queryset=Developer.objects.all(), required=False)
    archive = SlugRelatedField(
        slug_field='id_owner', queryset=Archive.objects.all(), required=False)

    class Meta:
        model = Print
        fields = '__all__'


class ScanRWSerializer(ModelSerializer):
    negative = SlugRelatedField(
        slug_field='slug', queryset=Negative.objects.all(), required=False)
    print = SlugRelatedField(slug_field='id_owner',
                             queryset=Print.objects.all(), required=False)

    class Meta:
        model = Scan
        fields = '__all__'
