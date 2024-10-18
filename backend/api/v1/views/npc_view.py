from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1.serializers.npc_serializer import (
    DoctorSerializer, UserDoctorSerializer, LevelUpDoctorSerializer
)
from npc.models import Doctor, UserDoctor
from environment.models import UserRoom
from users.permissions import IsAdmin, IsNotActive, IsNotBlocked, ReadOwnDataOnly


@extend_schema(tags=['Врачи'])
class DoctorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    permission_classes = [IsAuthenticated, IsNotActive, IsNotBlocked]

    @extend_schema(summary="API для получения всех врачей")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(summary="API для получения конкретного врача по ID")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


@extend_schema(tags=['Врач-Пользователь'])
class UserDoctorViewSet(viewsets.ModelViewSet):
    queryset = UserDoctor.objects.all()
    permission_classes = [IsAuthenticated, IsNotActive, IsNotBlocked]
    serializer_class = UserDoctorSerializer

    @extend_schema(summary="API для получения всей врачей")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(summary="API для получения конкретного врача по ID")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(summary="API для обновления конкретного врача по ID")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(summary="API для частичного обновления конкретного врача по ID")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(summary="API для создания нового врача")
    def create(self, request, *args, **kwargs):
        doctor_id = request.data.get('doctor')

        try:
            doctor = Doctor.objects.get(id=doctor_id)
        except Doctor.DoesNotExist:
            return Response({'error': 'Врач не найден.'}, status=status.HTTP_404_NOT_FOUND)

        doctor_price = doctor.price
        doctor_room = doctor.room.name
        user = request.user
        user_attributes = user.attributes

        if UserDoctor.objects.filter(user=user, doctor=doctor).exists():
            return Response({'error': 'Врач уже куплен.'}, status=status.HTTP_400_BAD_REQUEST)

        user_rooms = UserRoom.objects.filter(user=user, room__is_special=True)

        accommodation_room = None
        for user_room in user_rooms:
            if user_room.room.name == doctor_room:
                accommodation_room = user_room
                break

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            try:
                user_attributes.money_down(point=doctor_price)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

            serializer.save(user=request.user, accommodation_room=accommodation_room)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=['Врач-Пользователь'])
class LevelUpDoctorView(APIView):
    permission_classes = [IsAuthenticated, IsNotActive, IsNotBlocked]
    serializer_class = LevelUpDoctorSerializer

    @extend_schema(summary="API для повышения уровня врача за монеты")
    def patch(self, request, user_doctor_id):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            point = serializer.validated_data.get('point', 1)
            money = serializer.validated_data.get('money', None)

            try:
                user_doctor = UserDoctor.objects.get(id=user_doctor_id)
            except UserDoctor.DoesNotExist:
                return Response({"error": "Врач не найден или у вас нет прав на его изменение."},
                                status=status.HTTP_404_NOT_FOUND)

            try:
                user_doctor.level_up(point=point, money=money)
                user_doctor.save()

                return Response({"message": f"Уровень врача повышен на {point} за {money} монет."},
                                status=status.HTTP_200_OK)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
