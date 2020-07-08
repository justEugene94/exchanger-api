from random import randint

from django.db import models
from django.db.models import Count, Q


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


class CoefficientManager(models.Manager):

    def get_by_sum_of_purchase_amount(self, amount_of_purchases: int, accessor: str):
        return self.filter(Q(commerce_value__name=accessor) & Q(amount__lt=amount_of_purchases)).order_by('-amount').first().percent


class Coefficient(models.Model):

    objects = CoefficientManager()

    amount = models.IntegerField('сумма')

    percent = models.FloatField('процент')

    pub_date = models.DateTimeField('дата публикации')

    commerce_value = models.ForeignKey(
        CommerceValue,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return 'Процент ' + str(self.percent) + ' от ' + str(self.amount) + ' заявок'

    class Meta:
        verbose_name = "Коэффициет"
        verbose_name_plural = "Коэффициеты"
        # ordering = ['-amount']