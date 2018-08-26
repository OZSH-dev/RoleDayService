from django.db import models
from django.contrib.auth.models import AbstractUser


class RoleUser(AbstractUser):
    money = models.IntegerField(verbose_name="Кол-во валюты", default=0)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return "{} {} ({})".format(
            self.last_name, self.first_name, self.money)
