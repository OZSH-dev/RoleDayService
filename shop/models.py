from django.db import models
from uuid import uuid4
import os


def get_image_path(_, filename):
    return os.path.join(
        "posts_images",
        str(uuid4()) + "." + filename.split(".")[-1].lower()
    )


class Item(models.Model):
    price = models.IntegerField(verbose_name="Стоимость товара")
    amount = models.IntegerField(verbose_name="Кол-во на складе")
    name = models.TextField(max_length=200, verbose_name="Название")
    description = models.TextField(max_length=2000, verbose_name="Описание")
    image = models.ImageField(upload_to=get_image_path, null=True, verbose_name="Картинка")

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return "{} ({})".format(self.name, self.amount)


