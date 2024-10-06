from rest_framework import serializers
from django.contrib.auth import get_user_model
from environment.models import Room, Furniture, Categories

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
