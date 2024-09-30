from django.db import models


# Create your models here.

class Room(models.Model):
    """Модель комнаты."""

    name = models.CharField(
        verbose_name='Название комнаты',
        max_length=30,
        null=True
    )

    level = models.PositiveIntegerField(
        verbose_name='Уровень комнаты',
        default=1
    )

    def __str__(self):
        return f'{self.name} {self.level}'

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'


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

    def __str__(self):
        return f'{self.name} {self.price}'

    class Meta:
        verbose_name = 'Мебель'
        verbose_name_plural = 'Мебель'
