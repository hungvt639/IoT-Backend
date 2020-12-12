from django.db import models
from Users.models import MyUsers
from .DeviceSensor import DeviceSensor


class DeviceData(models.Model):
    device = models.ForeignKey(DeviceSensor, related_name="device", on_delete=models.CASCADE)
    data = models.IntegerField()
    create_at = models.DateTimeField()

    def __str__(self):
        return str(self.device) + ": " + str(self.data)