from rest_framework import serializers
from vps.models import Vps


class VpsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vps
        fields = '__all__'


class VpsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vps
        fields = (
            'uid',
            'cpu',
            'ram',
            'hdd',
            'status'
        )
