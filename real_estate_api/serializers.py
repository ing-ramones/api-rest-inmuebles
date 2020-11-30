from rest_framework import serializers
from geojson_serializer.serializers import geojson_serializer
from django.core.serializers import serialize
from real_estate_api.models import Estate, Company


class EstateSerializer(serializers.ModelSerializer):

    company_id = serializers.IntegerField()

    class Meta:
        model = Estate
        fields = ('id', 'geom', 'address', 'area',
                  'rooms', 'garage', 'other', 'company_id',)


@geojson_serializer('geom')
class EstateHyperlinkedSerializer(serializers.HyperlinkedModelSerializer):

    company_id = serializers.IntegerField()

    class Meta:
        model = Estate
        fields = ('id', 'geom', 'address', 'area',
                  'rooms', 'garage', 'other', 'company_id', 'url',)


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'name', 'nif',)
