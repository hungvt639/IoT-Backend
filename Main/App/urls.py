from django.urls import path
from .views.Chip import ChipView, ChipDetailView
from .views.DeviceSensor import DeviceSensorView, DeviceSensorDetailView
from .views.Command import CommandView, DetailCommandView
urlpatterns = [
    path('chip', ChipView.as_view()),
    path('chip/<int:id>', ChipDetailView.as_view()),

    path('device-sensor', DeviceSensorView.as_view()),
    path('device-sensor/<uuid:id>', DeviceSensorDetailView.as_view()),

    path('command', CommandView.as_view()),
    path('command/<int:id>', DetailCommandView.as_view()),
]
