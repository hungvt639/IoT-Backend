from django.contrib import admin
from .models.Chip import Chip
from .models.DeviceSensor import DeviceSensor
from .models.Device import DeviceData
from .models.Sensor import SensorData, Data
from .models.Command import Command, CommandRespose


admin.site.register(Chip)
admin.site.register(DeviceSensor)
admin.site.register(DeviceData)
admin.site.register(SensorData)
admin.site.register(Data)
admin.site.register(Command)
admin.site.register(CommandRespose)
