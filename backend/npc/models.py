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

    def __str__(self):
        return f'{self.name} {self.age} лет'

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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Диагноз'
        verbose_name_plural = 'Диагнозы'
        ordering = ['id']


class Categories(models.Model):
    """Модель категории процедур"""
    name = models.CharField(
        verbose_name='Название',
        max_length=30,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория процедур'
        verbose_name_plural = 'Категории процедур'
        ordering = ['id']


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
        null=True,
        blank=True,
    )

    execution_time = models.PositiveIntegerField(
        verbose_name='Время выполнения',
        null=True
    )

    def __str__(self):
        return f'{self.name} {self.execution_time} мин.'

    class Meta:
        verbose_name = 'Процедур'
        verbose_name_plural = 'Процедуры'
        ordering = ['id']


class PatientProcedure(models.Model):
    """Промежуточная модель для связи пациента с процедурами"""
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        verbose_name='Пациент',
        related_name='patient_procedures'
    )

    procedure = models.ForeignKey(
        Procedure,
        on_delete=models.CASCADE,
        verbose_name='Процедура',
        related_name='procedure_patients'
    )

    counter = models.PositiveIntegerField(
        verbose_name='Счётчик',
        default=0
    )

    is_done = models.BooleanField(
        verbose_name='Выполнена',
        default=False
    )

    def __str__(self):
        return f'{self.patient.name} - {self.procedure.name}'

    class Meta:
        # unique_together = ('patient', 'procedure')  # Уникальность комбинации пациент-процедура
        verbose_name = 'Процедура пациента'
        verbose_name_plural = 'Процедуры пациентов'
