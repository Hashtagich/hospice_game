from rest_framework import serializers
from django.contrib.auth import get_user_model
from npc.models import Doctor, UserDoctor
from environment.models import UserRoom

User = get_user_model()


class DoctorSerializer(serializers.ModelSerializer):
    profession_name = serializers.CharField(source='profession.name', read_only=True)
    room = serializers.CharField(source='room.name', read_only=True)

    class Meta:
        model = Doctor
        fields = [
            'name',
            'surname',
            'patronymic',
            'profession_name',
            'work_experience',
            'room'
        ]


class UserDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDoctor
        fields = [
            'doctor',
            'level',
            'busyness'
        ]

    def validate(self, attrs):
        user = self.context['request'].user
        doctor = attrs.get('doctor')

        if not UserRoom.objects.filter(user=user, room=doctor.room).exists():
            raise serializers.ValidationError("У пользователя нет комнаты для данного доктора.")

        return attrs


class LevelUpDoctorSerializer(serializers.ModelSerializer):
    point = serializers.IntegerField(default=1)
    money = serializers.IntegerField(default=1)

    class Meta:
        model = UserDoctor
        fields = [
            'point',
            'money'
        ]
