from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1.serializers.npc_serializer import (
    DoctorSerializer
)
from npc.models import Doctor
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
