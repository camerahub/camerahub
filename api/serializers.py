from rest_framework import serializers
from schema.models import Film, Negative, Scan, Print

class FilmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Film
        fields = ['url', 'id_owner', 'title']


class NegativeSerializer(serializers.HyperlinkedModelSerializer):
    film_id = serializers.StringRelatedField(many=False)
    class Meta:
        model = Negative
        fields = ['url', 'film', 'film_id', 'id_owner', 'frame', 'caption']

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
        