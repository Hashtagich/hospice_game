from drf_spectacular.utils import extend_schema
from rest_framework import mixins, viewsets

from api.v1.serializers.item_serializer import ResourceSerializer
from items.models import Resource


class ListAndRetrieveViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                             viewsets.GenericViewSet):
    pass


@extend_schema(tags=['Ресурсы'])
class ResourceViewSet(ListAndRetrieveViewSet):
    serializer_class = ResourceSerializer
    queryset = Resource.objects.all()
    http_method_names = ['get', 'patch']

    @extend_schema(summary="API для получения всех ресурсов")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="API для получения информации о ресурсе по его ID",
    )
    def retrieve(self, request, pk=None, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="API для частичного обновления ресурса",
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
