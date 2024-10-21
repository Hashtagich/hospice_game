from rest_framework import serializers
from django.contrib.auth import get_user_model
from environment.models import Room, Furniture, Categories, UserRoom, UserFurniture

User = get_user_model()


class CategoriesFurnitureSerializer(serializers.ModelSerializer):
    """Сериализатор для категории мебели."""

    class Meta:
        model = Categories
        fields = ['name']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['name', 'description', 'price']


class FurnitureSerializer(serializers.ModelSerializer):
    # categories = CategoriesFurnitureSerializer(read_only=True)
    categories = serializers.CharField(source='categories.name', read_only=True)
    room = serializers.CharField(source='room.name', read_only=True)

    class Meta:
        model = Furniture
        fields = ['id', 'name', 'categories', 'price', 'room', 'description']


class UserRoomSerializerForGet(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    room = serializers.CharField(source='room.name', read_only=True)

    class Meta:
        model = UserRoom
        fields = [
            'user',
            'room',
            'level',
            'max_furniture_count',
            'max_medical_equipment_count',
            'max_decor_elements_count'
        ]


class UserRoomSerializerForPost(serializers.ModelSerializer):
    class Meta:
        model = UserRoom
        fields = [
            'room',
            'level',
            'max_furniture_count',
            'max_medical_equipment_count',
            'max_decor_elements_count'
        ]


class LevelUpRoomSerializer(serializers.ModelSerializer):
    point = serializers.IntegerField(default=1)
    money = serializers.IntegerField(default=1)

    class Meta:
        model = UserRoom
        fields = [
            'point',
            'money'
        ]


class UserFurnitureSerializerForGet(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    furniture = FurnitureSerializer(read_only=True)

    class Meta:
        model = UserFurniture
        fields = [
            'user',
            'furniture',
            'in_warehouse'
        ]


class UserFurnitureSerializerForPost(serializers.ModelSerializer):
    accommodation_room = serializers.PrimaryKeyRelatedField(
        queryset=UserRoom.objects.all(),
        required=False,
    )

    class Meta:
        model = UserFurniture
        fields = [
            'furniture',
            'in_warehouse',
            'accommodation_room',
        ]
        extra_kwargs = {
            'accommodation_room': {'required': False}
        }

    def validate(self, attrs):
        user = self.context['request'].user
        furniture = attrs.get('furniture')

        if furniture.categories.name == 'Специально медицинское оборудование':
            if not UserRoom.objects.filter(user=user, room=furniture.room).exists():
                raise serializers.ValidationError("У пользователя нет комнаты для данной мебели.")

        accommodation_room = attrs.get('accommodation_room')

        if accommodation_room is not None:
            accommodation_room_id = accommodation_room.id
            if not isinstance(accommodation_room_id, int):
                raise serializers.ValidationError("Неверный формат для accommodation_room. Ожидается ID.")

            try:
                user_room = UserRoom.objects.get(id=accommodation_room_id, user=user)
            except UserRoom.DoesNotExist:
                raise serializers.ValidationError("Комната не найдена или не принадлежит пользователю.")

        return attrs


class PlaceFurnitureSerializer(serializers.ModelSerializer):
    accommodation_room = serializers.PrimaryKeyRelatedField(
        queryset=UserRoom.objects.all(),
        required=False,
    )

    class Meta:
        model = UserFurniture
        fields = [
            'furniture',
            'in_warehouse',
            'accommodation_room',
        ]
        extra_kwargs = {
            'furniture': {'required': False},
            'in_warehouse': {'required': False},
            'accommodation_room': {'required': False},
        }

    def validate(self, attrs):
        user = self.context['request'].user
        furniture = attrs.get('furniture')
        accommodation_room = attrs.get('accommodation_room')

        if furniture:
            if furniture.categories.name in ('Специально медицинское оборудование', 'Вспомогательное оборудование'):
                if not UserRoom.objects.filter(user=user, room=furniture.room).exists():
                    raise serializers.ValidationError("У пользователя нет комнаты для данной мебели.")

        if accommodation_room is not None:
            accommodation_room_id = accommodation_room.id
            if not isinstance(accommodation_room_id, int):
                raise serializers.ValidationError("Неверный формат ID комнаты.")
            try:
                user_room = UserRoom.objects.get(id=accommodation_room_id, user=user)
            except UserRoom.DoesNotExist:
                raise serializers.ValidationError("Комната не найдена или не принадлежит пользователю.")

        return attrs
