from rest_framework import serializers
from real_estate_api.models import Company, Estate


class EstateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estate
        fields = ('id', 'geom', 'address', 'area', 'rooms', 'garage', 'other',)


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'name', 'nif')
