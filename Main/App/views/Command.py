from ..serializer.Command import CommandSerializer, CreateCommandSerializer
from ..models.Command import Command
from rest_framework.response import Response
from rest_framework import status, generics
from ..utils.check_permission import check_permission
import paho.mqtt.client as paho
import time
import json


HOST = "168.63.233.199"
PORT = 1883


class CommandView(generics.ListCreateAPIView):

    def get(self, request, *args, **kwargs):
        perm = "App.view_command"
        validate, data, status_code = check_permission(request, perm)
        if validate:
            user = request.user
            values = Command.objects.filter(user=user)
            serializer = CommandSerializer(values, many=True)
            return Response(serializer.data, status=status_code)
        else:
            return Response(data, status=status_code)

    def post(self, request, *args, **kwargs):
        perm = "App.add_command"
        validate, data, status_code = check_permission(request, perm)
        if validate:
            try:
                request.data['user'] = request.user.id
                serializer = CreateCommandSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    data = serializer.data.copy()
                    data['command_id'] = data['id']
                    data.pop('user')
                    data.pop('id')
                    data = json.dumps(data)
                    try:
                        client = paho.Client()
                        client.connect(HOST, PORT)
                        (rc, mid) = client.publish(request.user.username, data, qos=1)
                        print("Publish to: {}".format(request.user.username))
                    except:
                        res = {
                            "message": "Lỗi kết nối",
                            "data": serializer.data.copy()
                        }
                        return Response(res, status=status.HTTP_400_BAD_REQUEST)
                    res = {
                        "message": "Gửi yêu cầu điều khiển thành công",
                        "data": serializer.data.copy()
                    }
                    return Response(res, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                raise e
            except:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data, status=status_code)

