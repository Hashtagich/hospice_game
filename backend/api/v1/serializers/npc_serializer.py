from rest_framework import serializers
from django.contrib.auth import get_user_model
from npc.models import Doctor

User = get_user_model()


class DoctorSerializer(serializers.ModelSerializer):
    profession_name = serializers.CharField(source='profession.name', read_only=True)
    room = serializers.CharField(source='room.name', read_only=True)

    class Meta:
        model = Doctor
        fields = ['name', 'surname', 'patronymic', 'profession_name', 'work_experience', 'room']
