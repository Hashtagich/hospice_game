from rest_framework import serializers
from django.contrib.auth import get_user_model
from users.models import UserAttributes

User = get_user_model()


def validate_user_money(user, amount):
    """Функция-валидатор для проверки кол-ва монет у пользователя для покупки"""
    user_attributes = UserAttributes.objects.get(user=user)
    if user_attributes.money < amount:
        raise serializers.ValidationError("Недостаточно средств для выполнения этой операции.")


class UserAttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAttributes
        fields = ['money', 'puzzles', 'experience', 'level']


class UserSerializerForGet(serializers.ModelSerializer):
    attributes = UserAttributesSerializer()

    class Meta:
        model = User
        fields = ['username', 'attributes']


class UserSerializerForPost(serializers.ModelSerializer):
    attributes = UserAttributesSerializer()

    class Meta:
        model = User
        fields = ['username', 'attributes']

    def update(self, instance, validated_data):
        attributes_data = validated_data.pop('attributes', None)
        if attributes_data:
            user_attributes = instance.attributes

            for attr, value in attributes_data.items():
                setattr(user_attributes, attr, value)
            user_attributes.save()

        instance.username = validated_data.get('username', instance.username)
        instance.save()

        return instance


class AttributeChangeSerializer(serializers.ModelSerializer):
    point = serializers.IntegerField(default=1)

    class Meta:
        model = UserAttributes
        fields = ['point']
