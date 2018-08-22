from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class RoleUser(AbstractUser):
    first_name = models.TextField(verbose_name="Имя")
    last_name = models.TextField(verbose_name="Фамилия")
    squad = models.PositiveSmallIntegerField(verbose_name="Отряд")
    money = models.IntegerField(verbose_name="Кол-во валюты")

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return "{} {} {} ({})".format(
            self.last_name, self.first_name, self.squad, self.money)