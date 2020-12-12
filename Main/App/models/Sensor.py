from django.db import models
from Users.models import MyUsers
from .DeviceSensor import DeviceSensor


class SensorData(models.Model):
    sensor = models.ForeignKey(DeviceSensor, related_name="sensor", on_delete=models.CASCADE)
    create_at = models.DateTimeField()

    def __str__(self):
        return str(self.sensor) + ": " + str(self.create_at)


class Data(models.Model):
    data = models.ForeignKey(SensorData, related_name="data", on_delete=models.CASCADE)
    field = models.CharField(max_length=100)
    value = models.IntegerField()
