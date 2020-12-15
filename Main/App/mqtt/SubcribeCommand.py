import paho.mqtt.client as mqtt
from ..serializer.Command import CommandResposeSerializer
import ast
import time
import datetime

HOST = "168.63.233.199"
PORT = 1883


def stamp_to_time(time_stamp):
    local_time = time.localtime(int(time_stamp))
    mytime = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    return datetime.datetime.strptime(mytime, "%Y-%m-%d %H:%M:%S")

def on_connect(client, userdata, flags, rc):
    print(client._client_id.decode("utf-8"))
    client.subscribe(client._client_id.decode("utf-8"), qos=1)

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_disconnect(client, userdata, rc):
    print("Disconect")
    client.reconnect()
def on_message(client, userdata, msg):
    data = ast.literal_eval(msg.payload.decode("UTF-8"))
    print(data)
    try:
        serializer = CommandResposeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print("Create",serializer.data.copy())
        else: print(serializer.errors)
    except:
        pass


class MqttConnectCommandResposr():
    def connect(self, topic):
        client = mqtt.Client(topic)
        client.on_connect = on_connect
        client.on_subscribe = on_subscribe
        # client.reconnect_delay_set(1, 120)
        client.on_message = on_message
        client.connect(HOST, PORT)
        client.loop_start()