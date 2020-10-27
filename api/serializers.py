from rest_framework import serializers
from schema.models import Film

class FilmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Film
        fields = ['id_owner', 'title']
