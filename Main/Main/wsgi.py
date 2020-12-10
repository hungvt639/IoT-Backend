"""
WSGI config for Main project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from App.mqttview import MqttConnect
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Main.settings')

application = get_wsgi_application()
# mqtt.client.loop_start()
# mqtt.conect("test")
mqtt=MqttConnect()
mqtt.connect("test")
mqtt.connect("test1")

mqtt1=MqttConnect()
mqtt1.stop("test1")
