from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1.serializers.user_serializer import (
    UserSerializerForGet, UserSerializerForPost, AttributeChangeSerializer
)
from users.models import User
from users.permissions import IsAdmin, IsNotActive, IsNotBlocked, ReadOwnDataOnly


@extend_schema(tags=['Пользователи'])
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    permission_classes = [IsAuthenticated, IsNotActive, IsNotBlocked, ReadOwnDataOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserSerializerForGet
        else:
            return UserSerializerForPost

    @extend_schema(exclude=True)
    def create(self, request, *args, **kwargs):
        return Response({'error': 'Метод создания недоступен.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @extend_schema(exclude=True)
    def destroy(self, request, *args, **kwargs):
        return Response({'error': 'Метод удаления недоступен.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @extend_schema(exclude=True)
    def list(self, request, *args, **kwargs):
        return Response({'error': 'Метод передачи списка недоступен.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @extend_schema(summary="API для получения конкретного пользователя по ID")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(summary="API для частичного редактирования конкретного пользователя по ID")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(summary="API для полного редактирования конкретного пользователя по ID")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class BaseAttributeView(APIView):
    permission_classes = [IsAuthenticated, IsNotActive, IsNotBlocked]
    serializer_class = AttributeChangeSerializer

    def get_object(self):
        return self.request.user.attributes

    def handle_patch(self, request, point, action_method, success_message):
        user_attributes = self.get_object()

        if user_attributes:
            try:
                action_method(point)
                user_attributes.save()
                return Response({"message": f"{success_message} {point}"}, status=status.HTTP_200_OK)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Атрибуты пользователя не найдены"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, action_method, success_message):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            point = serializer.validated_data.get('point', 1)
            return self.handle_patch(request, point, action_method, success_message)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=['Пользователи'])
class LevelUpView(BaseAttributeView):
    @extend_schema(summary="API для повышения уровня пользователя на указанную величину")
    def patch(self, request, *args, **kwargs):
        return super().patch(request, action_method=self.get_object().level_up,
                             success_message="Уровень успешно увеличен на")


@extend_schema(tags=['Пользователи'])
class MoneyUpView(BaseAttributeView):
    @extend_schema(summary="API для повышения монет пользователя на указанную величину")
    def patch(self, request, *args, **kwargs):
        return super().patch(request, action_method=self.get_object().money_up,
                             success_message="Количество монет успешно увеличено на")


@extend_schema(tags=['Пользователи'])
class MoneyDownView(BaseAttributeView):
    @extend_schema(summary="API для понижения монет пользователя на указанную величину")
    def patch(self, request, *args, **kwargs):
        return super().patch(request, action_method=self.get_object().money_down,
                             success_message="Количество монет успешно уменьшено на")


@extend_schema(tags=['Пользователи'])
class PuzzlesUpView(BaseAttributeView):
    @extend_schema(summary="API для повышения спец валюты пользователя на указанную величину")
    def patch(self, request, *args, **kwargs):
        return super().patch(request, action_method=self.get_object().puzzles_up,
                             success_message="Количество спец валюты успешно увеличено на")


@extend_schema(tags=['Пользователи'])
class PuzzlesDownView(BaseAttributeView):
    @extend_schema(summary="API для уменьшения спец валюты пользователя на указанную величину")
    def patch(self, request, *args, **kwargs):
        return super().patch(request, action_method=self.get_object().puzzles_down,
                             success_message="Количество спец валюты успешно уменьшено на")


@extend_schema(tags=['Пользователи'])
class ExperienceUpView(BaseAttributeView):

    @extend_schema(summary="API для повышения опыта пользователя на указанную величину")
    def patch(self, request, *args, **kwargs):
        return super().patch(request, action_method=self.get_object().experience_up,
                             success_message="Количество опыта успешно увеличено на")
