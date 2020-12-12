from rest_framework import serializers
from ..models.Chip import Chip
from ..models.DeviceSensor import DeviceSensor
from ..utils.function import TimestampField


class DeviceSensorSerializer(serializers.ModelSerializer):
    create_at = TimestampField("create_at")
    update_at = TimestampField("update_at")
    class Meta:
        model = DeviceSensor
        fields = ['id', 'name', 'pin_id', 'is_sensor', 'decription', 'create_at', 'update_at']



class ChipSerializer(serializers.ModelSerializer):
    chip = DeviceSensorSerializer(many=True, read_only=True)
    create_at = TimestampField("create_at")
    update_at = TimestampField("create_at")
    class Meta:
        model = Chip
        fields = ['id','name', 'user', 'key', 'decription', 'create_at', 'update_at', 'chip']
        read_only_fields = ['id', 'create_at', 'update_at', 'chip']