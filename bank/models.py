from django.db import models
from user.models import RoleUser
from shop.models import Item

# Create your models here.


class Transaction(models.Model):
    caller = models.ForeignKey(RoleUser, on_delete=models.CASCADE, verbose_name="Участник")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="Покупка")
    reverted = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    given = models.BooleanField(default=False)