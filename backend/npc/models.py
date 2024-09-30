from django.db import models


# Create your models here.

class Patient(models.Model):
    """Модель пациента"""
    name = models.CharField(
        verbose_name='Имя пациента',
        max_length=15,
        null=True
    )

    age = models.PositiveIntegerField(
        verbose_name='Возраст',
        default=5
    )

    condition = models.PositiveIntegerField(
        verbose_name='Состояние',
        default=1
    )
    sentiment = models.PositiveIntegerField(
        verbose_name='Настроение',
        default=1
    )

    fatigue = models.PositiveIntegerField(
        verbose_name='Усталость',
        default=1
    )

    diagnosis = models.ForeignKey(
        'Diagnosis',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Диагноз'
    )

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'


class Diagnosis(models.Model):
    """Модель диагноза"""
    name = models.CharField(
        verbose_name='Название',
        max_length=70,
        null=True
    )

    symptoms = models.TextField(
        verbose_name='Симптомы/описание',
        null=True
    )

    class Meta:
        verbose_name = 'Диагноз'
        verbose_name_plural = 'Диагнозы'


class Categories(models.Model):
    """Модель категории процедур"""
    name = models.CharField(
        verbose_name='Название',
        max_length=30,
        null=True
    )

    class Meta:
        verbose_name = 'Категория процедур'
        verbose_name_plural = 'Категории процедур'


class Procedure(models.Model):
    """Модель процедуры"""
    name = models.CharField(
        verbose_name='Название',
        max_length=30,
        null=True
    )

    categories = models.ForeignKey(
        'Categories',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Категория'
    )

    description = models.TextField(
        verbose_name='Описание',
        null=True
    )

    effectiveness = models.TextField(
        verbose_name='Эффективность',
        null=True
    )

    execution_time = models.PositiveIntegerField(
        verbose_name='Время выполнения',
        null=True
    )

    class Meta:
        verbose_name = 'Процедур'
        verbose_name_plural = 'Процедуры'
