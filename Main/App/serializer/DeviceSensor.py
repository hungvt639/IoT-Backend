from rest_framework import serializers
from ..models.DeviceSensor import DeviceSensor
from ..utils.function import TimestampField
from ..models.Sensor import SensorData, Data
from ..models.Device import DeviceData

class DeviceSerializer(serializers.ModelSerializer):
    create_at = TimestampField("create_at")
    class Meta:
        model = DeviceData
        fields = ['data', 'create_at']


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['field', 'value']


class SensorSerializer(serializers.ModelSerializer):
    data = DataSerializer(many=True)
    create_at = TimestampField("create_at")
    class Meta:
        model = SensorData
        fields = ['create_at', 'data']





class DeviceSensorSerializer(serializers.ModelSerializer):
    create_at = TimestampField("create_at")
    update_at = TimestampField("update_at")
    class Meta:
        model = DeviceSensor
        fields = ['id', 'chip', 'name', 'pin_id', 'is_sensor', 'decription', 'create_at', 'update_at']
        read_only_fields = ['id', 'create_at', 'update_at']

    def validate(self, attrs):
        device_sensor = DeviceSensor.objects.filter(chip=attrs.get('chip'))
        pin_id = attrs.get('pin_id')
        if pin_id in map(lambda x: x.pin_id, device_sensor):
            raise serializers.ValidationError({"message": ["pin_id này đã được cài đặt trong chip của bạn."]})
        return attrs

class EditDeviceSensorSerializer(serializers.ModelSerializer):
    create_at = TimestampField("create_at")
    update_at = TimestampField("update_at")
    class Meta:
        model = DeviceSensor
        fields = ['id', 'chip', 'name', 'pin_id', 'is_sensor', 'decription', 'create_at', 'update_at']
        read_only_fields = ['id', 'pin_id', 'create_at', 'update_at']
