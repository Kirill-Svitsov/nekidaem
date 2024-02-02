from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = (
        'username',
        'first_name',
        'last_name'
    )
    email = models.EmailField(
        unique=True,
        max_length=150,
        verbose_name='Адрес электронной почты'
    )
    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Имя пользователя'
    )
    first_name = models.CharField(
        max_length=150,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name='Фамилия'
    )
    registration_date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата регистрации'
    )

    class Meta:
        ordering = ('-registration_date',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
