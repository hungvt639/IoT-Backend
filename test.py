import paho.mqtt.client as paho
import datetime
import json
import time
import random


HOST = "168.63.233.199"
PORT = 1883


val = 10
data1=1
while True:

    temperature = random.randrange(10, 50)
    sound = random.randrange(50, 100)
    light = random.randrange(0, 100)
    if val == 10:
        data1 = random.randrange(0,2)
        val = 0
    data2 = random.randrange(0, 255)
    values = [
        {
            "sensor": "c45cc9ed-e9e5-430d-b8fa-31565cbbcca7",
            "data":[
                {"field": "temperature", "value": temperature},
                {"field": "sound", "value": sound}
            ],
            "create_at": datetime.datetime.now().strftime("%H:%M:%S %d-%m-%Y")
        },
        {
            "device": "3326d28c-5b38-4c9c-a6fe-76599d39a3d8",
            "data": data1,
            "create_at": datetime.datetime.now().strftime("%H:%M:%S %d-%m-%Y")
        },
        {
            "device": "6599e39f-77d5-4880-ba2f-f2ec66dc29fd",
            "data": data2,
            "create_at": datetime.datetime.now().strftime("%H:%M:%S %d-%m-%Y")
        },
        {
            "sensor": "a9f0fa39-0499-469d-b385-75c01c5ded2e",
            "data":[
                {"field": "light", "value": light}
            ],
            "create_at": datetime.datetime.now().strftime("%H:%M:%S %d-%m-%Y")
        }
    ]
    val = val + 1
    try:
        data = json.dumps(values)
        client = paho.Client()
        a = client.connect(HOST, PORT)
        (rc, mid) = client.publish("testtest", data, qos=1)
        print(values)
        client.disconnect()
    except:
        pass
    time.sleep(10)


