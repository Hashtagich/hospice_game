from django.db import models
from users.models import User
from environment.models import Room, UserRoom


# Create your models here.

class Patient(models.Model):
    """Модель пациента."""
    name = models.CharField(
        verbose_name='Имя пациента',
        max_length=15,
        null=True
    )

    age = models.PositiveIntegerField(
        verbose_name='Возраст',
        default=5
    )

    diagnosis = models.ForeignKey(
        'Diagnosis',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Диагноз'
    )

    categories_procedure = models.ManyToManyField(
        'Categories',
        related_name='categories_patient',
        verbose_name='Категории процедур',
        blank=True
    )

    procedure = models.ManyToManyField(
        'Procedure',
        related_name='procedure_patient',
        verbose_name='Процедуры',
        blank=True
    )

    def __str__(self):
        return f'{self.name} {self.age} лет'

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'


class Diagnosis(models.Model):
    """Модель диагноза."""
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
    """Модель категории процедур."""
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
    """Модель процедуры."""
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

    effectiveness = models.PositiveIntegerField(
        verbose_name='Эффективность',
        default=1
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


class Profession(models.Model):
    """Модель профессии врача."""
    name = models.CharField(
        verbose_name='Название',
        max_length=30,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Профессия врача'
        verbose_name_plural = 'Профессии врачей'
        ordering = ['id']


class Doctor(models.Model):
    """Модель Врача."""
    surname = models.CharField(
        verbose_name='Фамилия',
        max_length=15,
        null=True
    )

    name = models.CharField(
        verbose_name='Имя',
        max_length=15,
        null=True
    )

    patronymic = models.CharField(
        verbose_name='Отчество',
        max_length=20,
        null=True
    )

    profession = models.ForeignKey(
        'Profession',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Профессия'
    )

    work_experience = models.CharField(
        verbose_name='Стаж',
        max_length=40,
        null=True
    )

    price = models.PositiveIntegerField(
        verbose_name='Стоимость',
        default=1
    )

    room = models.ForeignKey(
        Room,
        related_name='doctor',
        verbose_name='Комната',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic} - {self.profession}'

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'
        ordering = ['id']


class PatientProcedure(models.Model):
    """Промежуточная модель для связи пациента с процедурами."""
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
        verbose_name = 'Процедура пациента'
        verbose_name_plural = 'Процедуры пациентов'
        ordering = ['id']


class UserPatient(models.Model):
    """Промежуточная модель для связи пользователя с пациентом."""
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        verbose_name='Пациент',
        related_name='patient_users'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='user_patients'
    )

    is_done = models.BooleanField(
        verbose_name='Реабилитирован',
        default=False
    )

    rehabilitation = models.PositiveIntegerField(
        verbose_name='Реабилитация',
        default=0
    )

    def __str__(self):
        return f'{self.user.username} - {self.patient.name}'

    class Meta:
        verbose_name = 'Пациент пользователя'
        verbose_name_plural = 'Пациенты пользователей'
        ordering = ['id']


class UserDoctor(models.Model):
    """Промежуточная модель для связи пользователя с врачом."""
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        verbose_name='Врач',
        related_name='doctor_users'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='user_doctors'
    )

    level = models.PositiveIntegerField(
        verbose_name='Уровень',
        default=1
    )

    busyness = models.PositiveIntegerField(
        verbose_name='Занятость',
        default=1
    )

    accommodation_room = models.ForeignKey(
        UserRoom,
        on_delete=models.SET_NULL,
        verbose_name='Фактическая комната размещения',
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.user.username} - {self.doctor}'

    class Meta:
        verbose_name = 'Врач пользователя'
        verbose_name_plural = 'Врачи пользователей'
        ordering = ['id']

    def level_up(self, point: int = 1, money: int = 1):
        """Метод увеличения уровня и занятости врача. Увеличивается на величину point, по дефолту = 1."""
        user_attributes = self.user.attributes
        user_attributes.money_down(point=money)
        if user_attributes.check_point(point):
            raise ValueError("Число должно быть строго больше 0.")
        else:
            self.level += point
            self.busyness += point
