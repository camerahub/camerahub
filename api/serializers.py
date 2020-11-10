from rest_framework import serializers
from schema.models import Film, Negative, Scan, Print, Lens, LensModel, Camera, CameraModel


class LensModelSerializer(serializers.HyperlinkedModelSerializer):
    manufacturer = serializers.StringRelatedField(many=False)

    class Meta:
        model = LensModel
        fields = ['manufacturer', 'model', ]


class LensSerializer(serializers.HyperlinkedModelSerializer):
    lensmodel = LensModelSerializer(many=False, read_only=True)

    class Meta:
        model = Lens
        fields = ['url', 'serial', 'lensmodel']


class CameraModelSerializer(serializers.HyperlinkedModelSerializer):
    manufacturer = serializers.StringRelatedField(many=False)

    class Meta:
        model = CameraModel
        fields = ['manufacturer', 'model', ]


class CameraSerializer(serializers.HyperlinkedModelSerializer):
    cameramodel = CameraModelSerializer(many=False, read_only=True)

    class Meta:
        model = Camera
        fields = ['url', 'serial', 'lensmodel']


class FilmSerializer(serializers.HyperlinkedModelSerializer):
    camera = CameraSerializer

    class Meta:
        model = Film
        fields = ['url', 'id_owner', 'title', 'camera']


class NegativeSerializer(serializers.HyperlinkedModelSerializer):
    film_id = serializers.StringRelatedField(many=False)
    filter = serializers.StringRelatedField(many=False)
    teleconverter = serializers.StringRelatedField(many=False)
    exposure_program = serializers.StringRelatedField(many=False)
    metering_mode = serializers.StringRelatedField(many=False)

    lens = LensSerializer(many=False, read_only=True)
    film = FilmSerializer(many=False, read_only=True)
    shutter_speed = serializers.StringRelatedField(many=False)

    class Meta:
        model = Negative
        fields = ['url', 'film', 'film_id', 'id_owner', 'frame', 'caption', 'date', 'lens', 'shutter_speed', 'aperture', 'filter', 'teleconverter',
                  'notes', 'mount_adapter', 'focal_length', 'location', 'flash', 'metering_mode', 'exposure_program', 'photographer', 'copy_of']


class PrintSerializer(serializers.HyperlinkedModelSerializer):
    negative = NegativeSerializer(many=False, read_only=True)

    class Meta:
        model = Print
        fields = ['pk', 'url', 'negative']


class ScanSerializer(serializers.HyperlinkedModelSerializer):
    negative = NegativeSerializer(many=False, read_only=True)
    print = PrintSerializer(many=False, read_only=True)

    class Meta:
        model = Scan
        fields = ['uuid', 'url', 'negative', 'print', 'filename']
