from ..models.models import *
from rest_framework import serializers
from Users.models import MyUsers


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['user', 'username', 'password', 'time_create', 'time_update']


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['sensor', 'values', 'time_create', 'time_update']


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['device', 'values', 'time_create', 'time_update']


class DeviceSensorSerializer(serializers.ModelSerializer):
    sensor = SensorSerializer(many=True, read_only=True)
    device = DeviceSerializer(many=True, read_only=True)

    class Meta:
        model = Account
        fields = ['pi', 'dsid', 'decription', 'time_create', 'time_update', 'sensor', 'device']


class PiSerializer(serializers.ModelSerializer):
    pi = DeviceSensorSerializer(many=True, read_only=True)
    
    class Meta:
        model = Account
        fields = ['user', 'key', 'decription', 'time_create', 'time_update', 'pi']