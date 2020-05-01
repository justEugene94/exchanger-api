from random import randint

from django.db import models
from django.db.models import Count


class CurrencyManager(models.Manager):

    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)

        return self.all()[random_index]


class Currency(models.Model):

    objects = CurrencyManager()

    name = models.CharField('имя', max_length = 5)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'