from django.db import models
from user.models import RoleUser
from shop.models import Item

# Create your models here.

TRANSACTION_STATES = (
    (0, "Ожидает выдачи"),
    (1, "Завершена"),
    (2, "Отменена")
)


class Transaction(models.Model):
    caller = models.ForeignKey(RoleUser, on_delete=models.CASCADE, verbose_name="Участник")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="Покупка")
    state = models.IntegerField(default=0, choices=TRANSACTION_STATES, verbose_name="Состояние транзакции")
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} -> {} ({}) {}".format(self.caller, self.item, self.item.price, self.state)
