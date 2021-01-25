from rest_framework import serializers
from ..models.Command import Command, CommandRespose
from ..models.Chip import Chip
from ..utils.function import TimestampField


class CommandSerializer(serializers.ModelSerializer):
    # create_at = TimestampField("create_at")
    create_at = serializers.DateTimeField(format="%H:%M:%S %d-%m-%Y", input_formats=["%H:%M:%S %d-%m-%Y"])
    class Meta:
        model = Command
        fields = ['id', 'key', 'pin_id', 'command', 'create_at']


class CreateCommandSerializer(serializers.ModelSerializer):
    create_at = serializers.DateTimeField(format="%H:%M:%S %d-%m-%Y",input_formats=["%H:%M:%S %d-%m-%Y"])
    class Meta:
        model = Command
        fields = ['id', 'user', 'key', 'pin_id', 'command', 'create_at']

    def validate(self, attrs):
        chip = Chip.objects.filter(user=attrs.get('user'), key=attrs.get('key'))
        if not chip:
            raise serializers.ValidationError({'message': ["Bạn không có quyền điều khiển thiết bị này!"]})
        return attrs


class CommandResposeSerializer(serializers.ModelSerializer):
    create_at = serializers.DateTimeField(format="%H:%M:%S %d-%m-%Y",input_formats=["%H:%M:%S %d-%m-%Y"])

    class Meta:
        model = CommandRespose
        fields = ['command_id', 'data', 'create_at']

