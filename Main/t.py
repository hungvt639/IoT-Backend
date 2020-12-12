import paho.mqtt.client as paho
import time
import json


HOST = "168.63.233.199"
PORT = 1883



data = {
    "command_id":"id",
    "key": "IDDDDĐ",
    "pin_id": "idd",
    "command": 1,
    "create_at": "123113113123"
}
data = json.dumps(data)

client = paho.Client()
a = client.connect(HOST, PORT)
print(a)
# client.loop_start()
(rc, mid) = client.publish("vthung", data, qos=1)
print(rc)
print(mid)
client.disconnect()



