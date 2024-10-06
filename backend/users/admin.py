from django.contrib.admin import TabularInline, ModelAdmin, register
from .models import User, UserAttributes


class UserAttributesInline(TabularInline):  # Или используйте TabularInline для горизонтального отображения
    model = UserAttributes
    can_delete = False
    verbose_name_plural = 'Атрибуты пользователя'
    fields = ('level', 'money', 'puzzles', 'experience')  # Укажите поля, которые хотите отобразить


@register(User)
class UserAdmin(ModelAdmin):
    list_display = (
        'username',
        'id',
        'email',
        'is_active',
        'is_blocked',
        'datetime_create',
        'get_user_level',
        'get_user_experience',
        'get_user_money',
        'get_user_puzzles',
    )
    inlines = [UserAttributesInline]

    search_fields = ('username', 'email')

    def get_user_level(self, obj):
        return obj.attributes.level if obj.attributes else 'Нет'

    def get_user_money(self, obj):
        return obj.attributes.money if obj.attributes else 0

    def get_user_puzzles(self, obj):
        return obj.attributes.puzzles if obj.attributes else 0

    def get_user_experience(self, obj):
        return obj.attributes.experience if obj.attributes else 0

    get_user_level.short_description = 'Уровень'
    get_user_experience.short_description = 'Опыт'
    get_user_money.short_description = 'Монеты'
    get_user_puzzles.short_description = 'Пазлы'
