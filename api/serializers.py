from schema.models import Film
from rest_framework import serializers


class FilmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Film
        fields = ['id_owner', 'title']
