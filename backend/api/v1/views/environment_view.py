from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1.serializers.environment_serializer import (
    RoomSerializer, FurnitureSerializer, UserRoomSerializerForGet, UserRoomSerializerForPost, LevelUpRoomSerializer,
    UserFurnitureSerializerForGet, UserFurnitureSerializerForPost
)
from environment.models import Room, Furniture, UserRoom, UserFurniture
from users.permissions import IsAdmin, IsNotActive, IsNotBlocked, ReadOwnDataOnly


@extend_schema(tags=['Комнаты'])
class RoomViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    permission_classes = [IsAuthenticated, IsNotActive, IsNotBlocked]

    @extend_schema(summary="API для получения всех комнат")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(summary="API для получения конкретной комнаты по ID")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


@extend_schema(tags=['Мебель'])
class FurnitureViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer

    permission_classes = [IsAuthenticated, IsNotActive, IsNotBlocked]

    @extend_schema(summary="API для получения всей мебели")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(summary="API для получения конкретной мебели по ID")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


@extend_schema(tags=['Комната-Пользователь'])
class UserRoomViewSet(viewsets.ModelViewSet):
    queryset = UserRoom.objects.all()
    permission_classes = [IsAuthenticated, IsNotActive, IsNotBlocked]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserRoomSerializerForGet
        else:
            return UserRoomSerializerForPost

    @extend_schema(summary="API для получения всех комнат")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(summary="API для получения конкретной комнаты по ID")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(summary="API для создания новой комнаты")
    def create(self, request, *args, **kwargs):
        room_id = request.data.get('room')

        try:
            room = Room.objects.get(id=room_id)
        except Room.DoesNotExist:
            return Response({'error': 'Комната не найдена.'}, status=status.HTTP_404_NOT_FOUND)

        room_price = room.price
        user_attributes = request.user.attributes

        # Снимаем деньги
        try:
            user_attributes.money_down(point=room_price)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # Создаём комнату
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Передаем текущего пользователя
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(summary="API для обновления конкретной комнаты по ID")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(summary="API для частичного обновления конкретной комнаты по ID")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


@extend_schema(tags=['Комната-Пользователь'])
class LevelUpRoomView(APIView):
    permission_classes = [IsAuthenticated, IsNotActive, IsNotBlocked]
    serializer_class = LevelUpRoomSerializer

    @extend_schema(summary="API для повышения уровня комнаты за монеты")
    def patch(self, request, user_room_id):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            point = serializer.validated_data.get('point', 1)
            money = serializer.validated_data.get('money', None)

            try:
                user_room = UserRoom.objects.get(id=user_room_id)
            except UserRoom.DoesNotExist:
                return Response({"error": "Комната не найдена или у вас нет прав на её изменение."},
                                status=status.HTTP_404_NOT_FOUND)

            try:
                user_room.level_up(point=point, money=money)
                user_room.save()

                return Response({"message": f"Уровень комнаты повышен на {point} за {money} монет."},
                                status=status.HTTP_200_OK)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=['Мебель-Пользователь'])
class UserFurnitureViewSet(viewsets.ModelViewSet):
    queryset = UserFurniture.objects.all()
    permission_classes = [IsAuthenticated, IsNotActive, IsNotBlocked]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserFurnitureSerializerForGet
        else:
            return UserFurnitureSerializerForPost

    @extend_schema(summary="API для получения всей мебели")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(summary="API для получения конкретной мебели по ID")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(summary="API для обновления конкретной мебели по ID")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(summary="API для частичного обновления конкретной мебели по ID")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(summary="API для создания новой мебели")
    def create(self, request, *args, **kwargs):
        furniture_id = request.data.get('furniture')

        try:
            furniture = Furniture.objects.get(id=furniture_id)
        except Furniture.DoesNotExist:
            return Response({'error': 'Мебель не найдена.'}, status=status.HTTP_404_NOT_FOUND)

        furniture_price = furniture.price
        user_attributes = request.user.attributes

        # Снимаем деньги
        try:
            user_attributes.money_down(point=furniture_price)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # Создаём мебель
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Передаем текущего пользователя
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

