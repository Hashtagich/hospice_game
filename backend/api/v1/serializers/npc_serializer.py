from rest_framework import serializers
from django.contrib.auth import get_user_model
from npc.models import Doctor, UserDoctor, UserPatient, Patient, Diagnosis, Categories, Procedure
from environment.models import UserRoom

User = get_user_model()


class ProcedureSerializer(serializers.ModelSerializer):
    categories = serializers.CharField(source='categories.name', read_only=True)

    class Meta:
        model = Procedure
        fields = [
            'name',
            'categories',
            'description',
            'execution_time'
        ]


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = [
            'name'
        ]


class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = [
            'name',
            'symptoms'
        ]


class PatientSerializer(serializers.ModelSerializer):
    diagnosis = DiagnosisSerializer()
    categories_procedure = CategoriesSerializer(many=True)
    procedure = ProcedureSerializer(many=True)

    class Meta:
        model = Patient
        fields = [
            'name',
            'age',
            'diagnosis',
            'categories_procedure',
            'procedure'
        ]


class DoctorSerializer(serializers.ModelSerializer):
    profession_name = serializers.CharField(source='profession.name', read_only=True)
    room = serializers.CharField(source='room.name', read_only=True)

    class Meta:
        model = Doctor
        fields = [
            'surname',
            'name',
            'patronymic',
            'profession_name',
            'work_experience',
            'price',
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


class UserPatientSerializerForGet(serializers.ModelSerializer):
    patient = PatientSerializer()

    class Meta:
        model = UserPatient
        fields = [
            'patient',
            'is_done',
            'rehabilitation',
        ]


class UserPatientSerializerForPost(serializers.ModelSerializer):
    class Meta:
        model = UserPatient
        fields = [
            'patient',
            'is_done',
            'rehabilitation',
        ]

    def validate(self, attrs):
        user = self.context['request'].user
        patient = attrs.get('patient')

        if UserPatient.objects.filter(user=user, patient=patient, is_done=False).exists():
            raise serializers.ValidationError("Данный пациент уже присутствует и уже проходит реабилитацию.")

        return attrs
