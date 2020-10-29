from rest_framework import serializers
from schema.models import Film, Negative, Scan, Print

class FilmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Film
        fields = ['id_owner', 'title']


class NegativeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Negative
        fields = ['id_owner', 'frame', 'caption']


class ScanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Scan
        fields = ['uuid', 'url', 'filename']
