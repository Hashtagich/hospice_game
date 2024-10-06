from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1.serializers.environment_serializer import (
    RoomSerializer, FurnitureSerializer
)
from environment.models import Room, Furniture
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
