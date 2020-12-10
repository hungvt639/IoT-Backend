from django.contrib import admin
from .models.mqttdata import Data
from .models.models import *

admin.site.register(Data)

admin.site.register(Pi)
admin.site.register(Device_Sensor)
admin.site.register(Device)
admin.site.register(Sensor)
admin.site.register(Account)
