from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.utils import timezone
from .validators import _validate_username


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

        UserAttributes.objects.create(user=user)

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
        max_length=15,
        blank=True,
        unique=True,
        validators=[_validate_username]
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
        default=10000
    )

    puzzles = models.PositiveIntegerField(
        verbose_name='Пазлы',
        default=10000
    )

    experience = models.PositiveIntegerField(
        verbose_name='Опыт',
        default=0
    )

    number_patients = models.PositiveIntegerField(
        verbose_name='Кол-во мест для пациентов',
        default=0
    )

    def __str__(self):
        return f'{self.user.username} - уровень {self.level}'

    class Meta:
        verbose_name = 'Атрибуты пользователя'
        verbose_name_plural = 'Атрибуты пользователей'

    @staticmethod
    def check_point(point: int) -> bool:
        """Проверяет корректности вводимых данных."""
        return point <= 0

    @staticmethod
    def check_funds(currency: int, point: int) -> bool:
        """Проверяет, можно ли вычесть указанную сумму без отрицательного результата."""
        if UserAttributes.check_point(point):
            raise ValueError("Число должно быть строго больше 0.")
        else:
            return currency - point >= 0

    def level_up(self, point: int = 1):
        """Метод увеличения уровня пользователя. Увеличивается на величину point, по дефолту = 1."""
        if self.check_point(point):
            raise ValueError("Число должно быть строго больше 0.")
        else:
            self.level += point
            self.save()

    def money_up(self, point: int = 1):
        """Метод увеличения валюты пользователя. Увеличивается на величину point, по дефолту = 1."""
        if self.check_point(point):
            raise ValueError("Число должно быть строго больше 0.")
        else:
            self.money += point
            self.save()

    def money_down(self, point: int = 1):
        """Метод уменьшения валюты пользователя. Уменьшается на величину point, по дефолту = 1."""
        if self.check_funds(currency=self.money, point=point):
            self.money -= point
            self.save()
        else:
            raise ValueError("Недостаточно средств для вычитания этой суммы.")

    def puzzles_up(self, point: int = 1):
        """Метод увеличения пазлов пользователя. Увеличивается на величину point, по дефолту = 1."""
        if self.check_point(point):
            raise ValueError("Число должно быть строго больше 0.")
        else:
            self.puzzles += point
            self.save()

    def puzzles_down(self, point: int = 1):
        """Метод уменьшения валюты пользователя. Уменьшается на величину point, по дефолту = 1."""
        if self.check_funds(currency=self.puzzles, point=point):
            self.puzzles -= point
            self.save()
        else:
            raise ValueError("Недостаточно средств для вычитания этой суммы.")

    def number_patients_up(self, point: int = 1):
        """Метод увеличения кол-ва мест для пациентов пользователя. Увеличивается на величину point, по дефолту = 1."""
        if self.check_point(point):
            raise ValueError("Число должно быть строго больше 0.")
        else:
            self.number_patients += point
            self.save()

    def number_patients_down(self, point: int = 1):
        """Метод уменьшения кол-ва мест для пациентов пользователя. Уменьшается на величину point, по дефолту = 1."""
        if self.check_funds(currency=self.number_patients, point=point):
            self.number_patients -= point
            self.save()
        else:
            raise ValueError("Недостаточно средств для вычитания этой суммы.")

    def experience_up(self, point: int = 1):
        """
        Метод увеличения опыта пользователя. Увеличивается на величину point, по дефолту = 1.
        Как только становиться больше или равен 1000 то уменьшается на 100 и автоматически повышает уровень пользователя
        на 1 и даёт 100 валюты и 1 пазл.
        """
        if self.check_point(point):
            raise ValueError("Число должно быть строго больше 0.")
        else:
            self.experience += point
            if self.experience >= 1000:
                k = self.experience // 1000
                self.experience = self.experience % 1000

                self.money_up(point=100*k)
                self.puzzles_up(point=1*k)
                self.level_up(point=1*k)
            self.save()


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
