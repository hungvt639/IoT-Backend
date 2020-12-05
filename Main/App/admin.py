from django.contrib import admin
from .models.Snippets import Snippet
from .models.image import File
from .models.mqttdata import Data

admin.site.register(Snippet)
admin.site.register(File)
admin.site.register(Data)