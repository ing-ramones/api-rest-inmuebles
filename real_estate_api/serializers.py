from rest_framework import serializers
from real_estate_api.models import Estate


class EstateSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Estate
        fields = ('id', 'geom', 'address', 'area',
                  'rooms', 'garage', 'other',)
