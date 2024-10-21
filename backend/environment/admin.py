from django.contrib import admin
from .models import Furniture, Room, Categories, UserRoom, UserFurniture


# Register your models here.

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'price', 'is_special')
    search_fields = ('name',)


@admin.register(Furniture)
class FurnitureAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'price', 'categories', 'room')
    search_fields = ('name',)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('name',)


@admin.register(UserRoom)
class UserRoomAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'id', 'room', 'level',
        'max_medical_equipment_count',
        'max_furniture_count',
        'max_decor_elements_count'
    )
    search_fields = ('user', 'room')


@admin.register(UserFurniture)
class UserFurnitureAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'furniture', 'in_warehouse')
    search_fields = ('user', 'furniture')
