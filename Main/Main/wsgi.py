"""
WSGI config for Main project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from App.mqtt.subcribe import MqttConnect
from App.mqtt.SubcribeCommand import MqttConnectCommandResposr
from django.core.wsgi import get_wsgi_application
from Users.permissions import createGroup

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Main.settings')

application = get_wsgi_application()

try:
    createGroup()
except:
    pass
# mqtt.client.loop_start()
# mqtt.conect("test")

# mqtt.connect("test1")
#
# mqtt1 = MqttConnect()
# mqtt1.stop("test1")
try:
    mqtt = MqttConnect()
    mqtt.connect("subcribe")
except:
    pass

try:
    mqttc = MqttConnectCommandResposr()
    mqttc.connect("command")
except:
    pass

# mqtt = MqttConnect()
# mqtt.connect("subcribe")
