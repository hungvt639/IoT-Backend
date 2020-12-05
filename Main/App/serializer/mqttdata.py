from ..models.mqttdata import Data
from rest_framework import serializers


class DataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Data
        fields = ['name', 'status', 'number']

