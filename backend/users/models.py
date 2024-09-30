from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.utils import timezone


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **kwargs):
        is_staff = kwargs.pop('is_staff', False)
        is_superuser = kwargs.pop('is_superuser', False)
        email = self.normalize_email(email)

        user = self.model(
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=True,
            **kwargs,
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password, **kwargs):
        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        return self._create_user(
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True,
            **kwargs,
        )


class User(AbstractBaseUser, PermissionsMixin):
    """Модель пользователя"""
    username = models.CharField(
        'Username',
        max_length=128,
        blank=True,
        unique=True,
    )

    email = models.EmailField(
        verbose_name='Email',
        null=False,
        unique=True,
    )
    is_staff = models.BooleanField(
        verbose_name='Суперпользователь',
        default=False
    )
    is_active = models.BooleanField(
        verbose_name='Активен',
        default=True
    )

    is_blocked = models.BooleanField(
        verbose_name='Заблокирован',
        default=False
    )

    datetime_create = models.DateTimeField(
        verbose_name='Дата регистрации',
        auto_now_add=True
    )

    datetime_first_pay = models.DateTimeField(
        verbose_name='Дата первой покупки',
        blank=True,
        null=True
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        # ordering = ('-id',)

    def __str__(self):
        return f'{self.username}'

    def set_datetime_first_pay(self):
        """Установка даты первой покупки"""
        self.datetime_first_pay = timezone.now()


class UserAttributes(models.Model):
    """Модель атрибутов пользователя"""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='attributes'
    )

    level = models.PositiveIntegerField(
        verbose_name='Уровень игрока',
        default=1
    )

    money = models.PositiveIntegerField(
        verbose_name='Монеты',
        default=1
    )

    puzzles = models.PositiveIntegerField(
        verbose_name='Пазлы',
        default=1
    )

    experience = models.PositiveIntegerField(
        verbose_name='Пазлы',
        default=1
    )

    class Meta:
        verbose_name = 'Атрибуты пользователя'
        verbose_name_plural = 'Атрибуты пользователей'


class Task(models.Model):
    """Модель задачи."""
    name = models.CharField(
        verbose_name='Название задачи',
        max_length=60,
        null=True
    )
    is_done = models.BooleanField(
        verbose_name='Выполнена',
        default=False
    )
    datetime_create = models.DateTimeField(
        verbose_name='Дата создания задачи',
        auto_now_add=True
    )

    user = models.ForeignKey(
        User,
        related_name='tasks',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ('is_done', 'name')


class GameSettings(models.Model):
    """Модель настроек игры."""
    CHOICE_LANGUAGE = (
        ('ru', 'Русский'),
        ('en', 'Английский'),
    )

    user_attributes = models.OneToOneField(
        UserAttributes,
        on_delete=models.CASCADE,
        related_name='settings'
    )

    volume = models.PositiveIntegerField(
        verbose_name='Громкость игры',
        default=0
    )
    notifications = models.BooleanField(
        verbose_name='Уведомления',
        default=False
    )

    language = models.CharField(
        verbose_name='Язык',
        max_length=20,
        choices=CHOICE_LANGUAGE,
        default='ru'
    )

    def __str__(self):
        return f'{self.volume}'

    class Meta:
        verbose_name = 'Настройки игры'
        verbose_name_plural = 'Настройки игры'
