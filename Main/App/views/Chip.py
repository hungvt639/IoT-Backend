from ..serializer.Chip import ChipSerializer
from ..models.Chip import Chip
from rest_framework.response import Response
from rest_framework import status, generics
from ..utils.check_permission import check_permission


class ChipView(generics.ListCreateAPIView):

    def get(self, request, *args, **kwargs):
        perm = "App.view_chip"
        validate, data, status_code = check_permission(request, perm)
        if validate:
            user = request.user
            chips = Chip.objects.filter(user=user)
            serializer = ChipSerializer(chips, many=True)
            return Response(serializer.data, status=status_code)
        else:
            return Response(data, status=status_code)

    def post(self, request, *args, **kwargs):
        perm = "App.add_chip"
        validate, data, status_code = check_permission(request, perm)
        if validate:
            try:
                request.data['user'] = request.user.id
                serializer = ChipSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    data = serializer.data.copy()
                    return Response(data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data, status=status_code)


class ChipDetailView(generics.ListCreateAPIView):

    def get(self, request, *args, **kwargs):
        perm = "App.view_chip"
        validate, data, status_code = check_permission(request, perm)
        if validate:
            try:
                id = kwargs.get('id')
                user = request.user
                chip = Chip.objects.filter(user=user).get(id=id)
                serializer = ChipSerializer(chip)
                return Response(serializer.data, status=status_code)
            except Chip.DoesNotExist:
                return Response({"message": ["Không có CHIP này trong danh sách của bạn!"]}, status=status.HTTP_404_NOT_FOUND)
            except:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data, status=status_code)

    def put(self, request, *args, **kwargs):
        perm = "App.change_chip"
        validate, data, status_code = check_permission(request, perm)
        if validate:
            try:
                id = kwargs.get('id')
                user = request.user
                chip = Chip.objects.filter(user=user).get(id=id)
                serializer = ChipSerializer(chip, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    data = serializer.data.copy()
                    return Response(data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Chip.DoesNotExist:
                return Response({"message": ["Không có CHIP này trong danh sách của bạn!"]}, status=status.HTTP_404_NOT_FOUND)
            except:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data, status=status_code)

    def delete(self, request, *args, **kwargs):
        perm = "App.delete_chip"
        validate, data, status_code = check_permission(request, perm)
        if validate:
            try:
                id = kwargs.get('id')
                user = request.user
                chips = Chip.objects.filter(user=user)
                chips.get(id=id).delete()
                return Response({"message": ["Xóa CHIP thành công!"]}, status=status_code)
            except:
                return Response({"message": ["Không có CHIP này trong danh sách của bạn!"]}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(data, status=status_code)