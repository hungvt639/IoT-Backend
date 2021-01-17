import paho.mqtt.client as mqtt
from ..serializer.Command import CommandResposeSerializer
import ast
from Main.settings import MQTT_HOST, MQTT_PORT

print(MQTT_HOST, MQTT_PORT)

def on_connect(client, userdata, flags, rc):
    print("Connect to: {}:{}".format(MQTT_HOST, MQTT_PORT))
    client.subscribe(userdata, qos=1)


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribe topic: {} - ".format(userdata) + str(mid) + " " + str(granted_qos))


def on_disconnect(client, userdata, rc):
    print("Disconnect to {}".format(userdata))


def on_message(client, userdata, msg):
    data = ast.literal_eval(msg.payload.decode("UTF-8"))
    try:
        serializer = CommandResposeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print("Create",serializer.data.copy())
        else: print(serializer.errors)
    except Exception as e:
        print("Lỗi - {}: ".format(userdata), e)
    print("______________________________________________________")


class MqttConnectCommandResponse:
    def connect(self, topic):
        client = mqtt.Client(topic, userdata=topic)
        client.on_connect = on_connect
        client.on_subscribe = on_subscribe
        client.reconnect_delay_set(1, 60)
        client.on_message = on_message
        client.on_disconnect = on_disconnect
        client.connect(MQTT_HOST, MQTT_PORT, keepalive=60)
        client.loop_start()