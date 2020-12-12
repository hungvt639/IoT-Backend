from ..serializer.DeviceSensor import DeviceSensorSerializer, DeviceSerializer, SensorSerializer, EditDeviceSensorSerializer
from ..models.DeviceSensor import DeviceSensor
from ..models.Device import DeviceData
from ..models.Sensor import SensorData
from ..models.Chip import Chip
from rest_framework.response import Response
from rest_framework import status, generics
from ..utils.check_permission import check_permission


class DeviceSensorView(generics.ListCreateAPIView):

    def get(self, request, *args, **kwargs):
        perm = "App.view_devicesensor"
        validate, data, status_code = check_permission(request, perm)
        if validate:
            user = request.user
            values = DeviceSensor.objects.filter(chip__user=user)
            serializer = DeviceSensorSerializer(values, many=True)
            return Response(serializer.data, status=status_code)
        else:
            return Response(data, status=status_code)

    def post(self, request, *args, **kwargs):
        perm = "App.add_devicesensor"
        validate, data, status_code = check_permission(request, perm)
        if validate:
            try:
                user = request.user
                chip = int(request.data.get('chip', 0))
                if chip:
                    chips = Chip.objects.filter(id=chip, user=user)
                    if chips:
                        serializer = DeviceSensorSerializer(data=request.data)
                        if serializer.is_valid():
                            serializer.save()
                            data = serializer.data.copy()
                            return Response(data, status=status.HTTP_200_OK)
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return Response({'message': ['Không có CHIP nào có id bằng {} trong danh sách chip của bạn'.format(chip)],})
                else:
                    return Response({'message': ['Vui lòng nhập ID của chip'.format(chip)],})
            except:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data, status=status_code)


class DeviceSensorDetailView(generics.ListCreateAPIView):

    def get(self, request, *args, **kwargs):
        perm = "App.view_devicesensor"
        validate, data, status_code = check_permission(request, perm)
        if validate:
            try:
                id = kwargs.get('id')
                user = request.user
                value = DeviceSensor.objects.filter(chip__user=user).get(id=id)
                if value.is_sensor:
                    sensor_data = SensorData.objects.filter(sensor=value)
                    serializer_data = SensorSerializer(sensor_data, many=True)
                    print(1)
                else:
                    device_data = DeviceData.objects.filter(device=value).last()
                    serializer_data = DeviceSerializer(device_data)
                serializer = DeviceSensorSerializer(value)
                data = serializer.data
                data['data'] = serializer_data.data
                return Response(data, status=status_code)
            except Exception as e:
                raise e
            except DeviceSensor.DoesNotExist:
                return Response({"message": ["Không có thiết bị này trong danh sách của bạn!"]},status=status.HTTP_404_NOT_FOUND)
            except:
                return Response({"message": ["Đã có lỗi sảy ra, bạn vui lòng thử lại sau!"]}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data, status=status_code)

    def put(self, request, *args, **kwargs):
        perm = "App.change_devicesensor"
        validate, data, status_code = check_permission(request, perm)
        if validate:
            try:
                id = kwargs.get('id')
                user = request.user
                value = DeviceSensor.objects.filter(chip__user=user).get(id=id)
                request.data['chip'] = value.chip.id
                pin = request.data.get('pin_id', 0)
                if pin and value.pin_id == pin:
                    serializer = EditDeviceSensorSerializer(value, data=request.data)
                else:
                    serializer = DeviceSensorSerializer(value, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    data = serializer.data.copy()
                    return Response(data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except DeviceSensor.DoesNotExist:
                return Response({"message": ["Không có sản thiết bị này trong danh sách CHIP của bạn!"]}, status=status.HTTP_404_NOT_FOUND)
            except:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data, status=status_code)

    def delete(self, request, *args, **kwargs):
        perm = "App.delete_devicesensor"
        validate, data, status_code = check_permission(request, perm)
        if validate:
            try:
                id = kwargs.get('id')
                user = request.user
                value = DeviceSensor.objects.filter(chip__user=user)
                value.get(id=id).delete()
                return Response({"message": ["Xóa thiết bị thành công!"]}, status=status_code)
            except:
                return Response({"message": ["Không có thiết bị này trong danh sách của bạn!"]}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(data, status=status_code)