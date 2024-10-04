from django.db import models
from users.models import User


# Create your models here.

class Room(models.Model):
    """Модель комнаты."""

    name = models.CharField(
        verbose_name='Название комнаты',
        max_length=30,
        null=True
    )

    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True
    )

    price = models.PositiveIntegerField(
        verbose_name='Стоимость',
        default=1
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'
        ordering = ['id']


class Categories(models.Model):
    """Модель категории мебели."""
    name = models.CharField(
        verbose_name='Название',
        max_length=30,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория мебели'
        verbose_name_plural = 'Категории мебели'
        ordering = ['id']


class Furniture(models.Model):
    """Модель мебели."""

    name = models.CharField(
        verbose_name='Название мебели',
        max_length=30,
        null=True
    )

    price = models.PositiveIntegerField(
        verbose_name='Стоимость',
        default=1
    )

    room = models.ForeignKey(
        Room,
        related_name='furniture',
        verbose_name='Комната',
        on_delete=models.CASCADE
    )

    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True
    )

    in_warehouse = models.BooleanField(
        verbose_name='На складе',
        default=False
    )

    categories = models.ForeignKey(
        Categories,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Категория'
    )

    def __str__(self):
        return f'{self.name} {self.price}'

    class Meta:
        verbose_name = 'Мебель'
        verbose_name_plural = 'Мебель'
        ordering = ['id']


class UserRoom(models.Model):
    """Промежуточная модель для связи пользователя и комнаты."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE
    )

    level = models.PositiveIntegerField(
        verbose_name='Уровень комнаты',
        default=1
    )

    max_furniture_count = models.PositiveIntegerField(
        verbose_name='Максимальное кол-во мебели в комнате',
        default=1
    )

    max_medical_equipment_count = models.PositiveIntegerField(
        verbose_name='Максимальное кол-во мед оборудования в комнате',
        default=1
    )

    class Meta:
        verbose_name = 'Комната пользователя'
        verbose_name_plural = 'Комнаты пользователя'
        ordering = ['id']
