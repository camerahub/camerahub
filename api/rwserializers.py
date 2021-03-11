from rest_framework.serializers import ModelSerializer
from schema.models import Accessory, Archive,  Camera, Film
from schema.models import Flash, Enlarger, Negative
from schema.models import Person, Teleconverter, BulkFilm, MountAdapter
from schema.models import Lens, Print, Scan, Order


class PersonRWSerializer(ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'


class ArchiveRWSerializer(ModelSerializer):

    class Meta:
        model = Archive
        fields = '__all__'


class FlashRWSerializer(ModelSerializer):

    class Meta:
        model = Flash
        fields = '__all__'


class EnlargerRWSerializer(ModelSerializer):

    class Meta:
        model = Enlarger
        fields = '__all__'


class TeleconverterRWSerializer(ModelSerializer):

    class Meta:
        model = Teleconverter
        fields = '__all__'


class BulkFilmRWSerializer(ModelSerializer):

    class Meta:
        model = BulkFilm
        fields = '__all__'


class MountAdapterRWSerializer(ModelSerializer):

    class Meta:
        model = MountAdapter
        fields = '__all__'


class AccessoryRWSerializer(ModelSerializer):

    class Meta:
        model = Accessory
        fields = '__all__'


class LensRWSerializer(ModelSerializer):

    class Meta:
        model = Lens
        fields = '__all__'


class CameraRWSerializer(ModelSerializer):

    class Meta:
        model = Camera
        fields = '__all__'


class FilmRWSerializer(ModelSerializer):

    class Meta:
        model = Film
        fields = '__all__'


class NegativeRWSerializer(ModelSerializer):

    class Meta:
        model = Negative
        fields = '__all__'


class PrintRWSerializer(ModelSerializer):

    class Meta:
        model = Print
        fields = '__all__'


class ScanRWSerializer(ModelSerializer):

    class Meta:
        model = Scan
        fields = '__all__'


class OrderRWSerializer(ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
