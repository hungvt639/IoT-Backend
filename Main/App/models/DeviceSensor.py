from django.db import models
from Users.models import MyUsers
from .Chip import Chip
import uuid


class DeviceSensor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    chip = models.ForeignKey(Chip, related_name="chip", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    pin_id = models.IntegerField()
    is_sensor = models.BooleanField()
    decription = models.TextField(max_length=1000, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.chip) + ": " + ": "+ self.name + ": " + str(self.pin_id) + " - " + str(self.is_sensor)