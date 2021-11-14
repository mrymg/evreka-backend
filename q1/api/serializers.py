from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from q1.models import NavigationRecord, Vehicle


class NavigationRecordSerializer(ModelSerializer):
    class Meta:
        model = NavigationRecord
        fields = '__all__'


class VehicleSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'
