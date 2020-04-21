from random import randint

from django.db import models
from django.db.models import Count


class CommerceValueManager(models.Manager):
    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)

        return self.all()[random_index]


class CommerceValue(models.Model):

    objects = CommerceValueManager()

    name = models.CharField('имя', max_length = 6)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Коммерческая ценность"
        verbose_name_plural = "Коммерческие ценности"


class Coefficient(models.Model):

    amount = models.IntegerField('сумма')

    percent = models.FloatField('процент')

    pub_date = models.DateTimeField('дата публикации')

    commerce_value = models.ForeignKey(
        CommerceValue,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Коэффициет"
        verbose_name_plural = "Коэффициеты"