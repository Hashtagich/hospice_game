from rest_framework import serializers

from items.models import Resource


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = (
            'title',
            'quantity',
        )
