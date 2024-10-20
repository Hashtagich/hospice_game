from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied


class IsNotBlocked(BasePermission):
    """Проверка заблокирован пользователь или нет."""

    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated or user.is_blocked:
            raise PermissionDenied("Ваша учётная запись заблокирована.")
        return True


class IsAdmin(BasePermission):
    """Проверка является ли пользователь админом или нет."""

    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated or not user.is_staff:
            raise PermissionDenied("Данный функционал доступен только пользователям с ролью Администратор.")
        return True


class IsNotActive(BasePermission):
    """Проверка активирована учетная запись пользователя или нет."""

    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated or not user.is_active:
            raise PermissionDenied("Вам нужно активировать учетную запись с помощью письма, отправленного на почту.")
        return True


class ReadOwnDataOnly(BasePermission):
    """Проверка доступа пользователя только к своим данным."""

    def has_object_permission(self, request, view, obj):
        if request.method in ['HEAD', 'OPTIONS']:
            return True

        if obj.id != request.user.id:
            raise PermissionDenied("У вас нет доступа к данным других пользователей.")
        else:
            return True


class ReadOwnDataOnlyForConnection(BasePermission):
    """Проверка доступа пользователя только к своим данным. Для связей"""

    def has_object_permission(self, request, view, obj):
        if request.method in ['HEAD', 'OPTIONS']:
            return True

        if obj.user.id != request.user.id:
            raise PermissionDenied("У вас нет доступа к данным других пользователей.")
        else:
            return True
