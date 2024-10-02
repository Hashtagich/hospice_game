from django.contrib import admin
from .models import Furniture, Room


# Register your models here.

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'level')
    search_fields = ('name', )


@admin.register(Furniture)
class FurnitureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    search_fields = ('name', )
