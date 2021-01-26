from rest_framework import serializers
from ..models.Sensor import SensorData, Data
from ..utils.function import TimestampField


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['field', 'value']


class SensorSerializer(serializers.ModelSerializer):
    data = DataSerializer(many=True, )
    # create_at = TimestampField("create_at")
    create_at = serializers.DateTimeField( format="%H:%M:%S %d-%m-%Y",input_formats=["%Y-%m-%d %H:%M:%S",])
    class Meta:
        model = SensorData
        fields = ['id', 'sensor', 'create_at', 'data']

    def create(self, validated_data):
        sensor_data = SensorData.objects.create(
            sensor = validated_data.get('sensor'),
            create_at = validated_data.get('create_at')
        )
        datas = validated_data.get('data')
        for data in datas:
            d = Data.objects.create(
                data = sensor_data,
                field = data.get('field'),
                value = data.get('value')
            )
            d.save()
        sensor_data.save()
        return sensor_data