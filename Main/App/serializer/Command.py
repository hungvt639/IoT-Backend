from rest_framework import serializers
from ..models.Command import Command, CommandRespose
from ..utils.function import TimestampField


class CommandSerializer(serializers.ModelSerializer):
    create_at = TimestampField("create_at")
    class Meta:
        model = Command
        fields = ['id', 'key', 'pin_id', 'command', 'create_at']


class CreateCommandSerializer(serializers.ModelSerializer):
    create_at = serializers.DateTimeField(format="%H:%M:%S %d-%m-%Y",input_formats=["%H:%M:%S %d-%m-%Y"])
    class Meta:
        model = Command
        fields = ['id', 'user', 'key', 'pin_id', 'command', 'create_at']


class CommandResposeSerializer(serializers.ModelSerializer):
    create_at = serializers.DateTimeField(format="%H:%M:%S %d-%m-%Y",input_formats=["%H:%M:%S %d-%m-%Y"])

    class Meta:
        model = CommandRespose
        fields = ['command_id', 'data', 'create_at']

