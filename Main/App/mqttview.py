# import paho.mqtt.client as mqtt
# from App.models.mqttdata import Data
# from App.serializer.mqttdata import DataSerializer
# import json
# import ast
#
# HOST = "168.63.233.199"
# PORT = 1883
#
#
# def on_connect(client, userdata, flags, rc):
#     print("CONNACK received with code %d." % (rc))
#
#
# def on_publish(client, userdata, mid):
#     print("publiced message with ID: " + str(mid))
#
#
# def on_subscribe(client, userdata, mid, granted_qos):
#     print("Subscribed: " + str(mid) + " " + str(granted_qos))
#
#
# def on_message(client, userdata, msg):
#     data = ast.literal_eval(msg.payload.decode("UTF-8"))
#     print(data)
#     serializer = DataSerializer(data=data)
#     if serializer.is_valid():
#         serializer.save()
#     else:
#         pass
#
#
# class MqttConnect():
#
#     def connect(self, topic):
#         client = mqtt.Client(topic)
#         client.on_connect = on_connect
#         client.on_publish = on_publish
#         client.on_subscribe = on_subscribe
#         client.on_message = on_message
#         client.connect(HOST, PORT)
#         client.subscribe(topic, qos=0)
#         client.loop_start()
#
#     def stop(self, topic):
#         client = mqtt.Client(topic)
#         client.on_connect = on_connect
#         # client.on_publish = on_publish
#         # client.on_subscribe = on_subscribe
#         # client.on_message = on_message
#         client.connect(HOST, PORT)
#         # client.subscribe(topic, qos=1)
#         # client.loop_start()
#         client.loop_stop()
#
#
# # def conect(topic):
# #     client = mqtt.Client()
# #     client.on_connect = on_connect
# #     client.on_publish = on_publish
# #     client.on_subscribe = on_subscribe
# #     client.on_message = on_message
# #     client.connect(HOST, PORT)
# #     client.subscribe(topic, qos=1)
# #     client.loop_start()
