from rest_framework import serializers
from schema.models import Film, Negative

class FilmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Film
        fields = ['id_owner', 'title']


class NegativeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Negative
        fields = ['id_owner', 'frame', 'caption']
