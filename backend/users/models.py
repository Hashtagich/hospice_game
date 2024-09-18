from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)


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

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        # ordering = ('-id',)

    def __str__(self):
        return f'{self.username}'
