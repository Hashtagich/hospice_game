from django.contrib import admin
from .models import User, UserAttributes


class UserAttributesInline(admin.StackedInline):  # Или используйте TabularInline для горизонтального отображения
    model = UserAttributes
    can_delete = False
    verbose_name_plural = 'Атрибуты пользователя'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'is_blocked', 'datetime_create')
    inlines = [UserAttributesInline]

    search_fields = ('username', 'email')
