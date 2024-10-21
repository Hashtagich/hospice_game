from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1.serializers.environment_serializer import (
    RoomSerializer, FurnitureSerializer, UserRoomSerializerForGet, UserRoomSerializerForPost, LevelUpRoomSerializer,
    UserFurnitureSerializerForGet, UserFurnitureSerializerForPost, PlaceFurnitureSerializer
)
from environment.models import Room, Furniture, UserRoom, UserFurniture
from users.permissions import IsNotActive, IsNotBlocked, ReadOwnDataOnlyForConnection
from users.models import UserAttributes


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

    @extend_schema(summary="API для получения всех комнат текущего пользователя")
    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(user=request.user)
        return super().list(request, *args, **kwargs)

    @extend_schema(summary="API для получения конкретной комнаты по ID")
    def retrieve(self, request, *args, **kwargs):
        self.permission_classes = [IsAuthenticated, IsNotActive, IsNotBlocked, ReadOwnDataOnlyForConnection]
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(summary="API для создания новой комнаты")
    def create(self, request, *args, **kwargs):
        room_id = request.data.get('room')

        try:
            room = Room.objects.get(id=room_id)
        except Room.DoesNotExist:
            return Response({'error': 'Комната не найдена.'}, status=status.HTTP_404_NOT_FOUND)

        room_price = room.price
        user = request.user
        user_attributes = user.attributes

        try:
            user_room = UserRoom.objects.filter(user=user, room=room).first()

            if user_room:
                room_is_special = user_room.room.is_special
                if room_is_special:
                    return Response({'error': f'Вы можете купить только один кабинет - {room.name}.'},
                                    status=status.HTTP_400_BAD_REQUEST)

            else:
                user_attributes.number_patients_up(point=1)
            user_attributes.money_down(point=room_price)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({
                'message': f'{room.name} успешно куплен за {room_price} монет.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
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
        elif self.request.method in ['PUT', 'PATCH']:
            return PlaceFurnitureSerializer
        else:
            return UserFurnitureSerializerForPost

    @extend_schema(summary="API для получения всей мебели текущего пользователя")
    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(user=request.user)
        return super().list(request, *args, **kwargs)

    @extend_schema(summary="API для получения конкретной мебели по ID")
    def retrieve(self, request, *args, **kwargs):
        self.permission_classes = [IsAuthenticated, IsNotActive, IsNotBlocked, ReadOwnDataOnlyForConnection]
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(exclude=True)
    def update(self, request, *args, **kwargs):
        return Response({'error': 'Метод обновления недоступен.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @extend_schema(summary="API для частичного редактирования/размещения в комнате или отправки на склад мебели по ID")
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()

        if not instance.in_warehouse:
            instance.in_warehouse = True
            instance.accommodation_room = None
            instance.save()
            return Response({'message': 'Статус in_warehouse был обновлён на True, accommodation_room очищен.'},
                            status=status.HTTP_200_OK)

        accommodation_room = request.data.get('accommodation_room')

        if accommodation_room:
            user = request.user
            try:
                user_room = UserRoom.objects.get(id=accommodation_room, user=user)
            except UserRoom.DoesNotExist:
                return Response({'error': 'Комната не найдена или не принадлежит пользователю.'},
                                status=status.HTTP_404_NOT_FOUND)

            furniture = instance.furniture
            category_name = furniture.categories.name

            if category_name == "Мебель и принадлежности":
                if user_room.max_furniture_count <= 0:
                    return Response({'error': 'Достигнуто максимальное количество мебели в комнате.'},
                                    status=status.HTTP_400_BAD_REQUEST)
                user_room.max_furniture_count -= 1
            elif category_name == "Специально медицинское оборудование":
                if user_room.max_medical_equipment_count <= 0:
                    return Response({
                        'error': 'Достигнуто максимальное количество специального медицинского оборудования в комнате.'},
                        status=status.HTTP_400_BAD_REQUEST)
                user_room.max_medical_equipment_count -= 1
            elif category_name == "Элементы декора":
                if user_room.max_decor_elements_count <= 0:
                    return Response({'error': 'Достигнуто максимальное количество элементов декора в комнате.'},
                                    status=status.HTTP_400_BAD_REQUEST)
                user_room.max_decor_elements_count -= 1

            user_room.save()

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['in_warehouse'] = False
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

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

    @extend_schema(summary="API для удаления/продажи мебели")
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user
        furniture = instance.furniture

        try:
            user_furniture = UserFurniture.objects.get(user=user, furniture=furniture)
        except UserFurniture.DoesNotExist:
            return Response({'error': 'У вас нет прав на удаление этой мебели.'}, status=status.HTTP_403_FORBIDDEN)

        try:
            user_attributes = UserAttributes.objects.get(user=user)
        except UserAttributes.DoesNotExist:
            return Response({'error': 'Атрибуты пользователя не найдены.'}, status=status.HTTP_404_NOT_FOUND)

        furniture_price = furniture.price
        user_attributes.money_up(furniture_price // 2)

        instance.delete()

        return Response({'message': 'Мебель успешно продана и деньги добавлены.'}, status=status.HTTP_204_NO_CONTENT)
