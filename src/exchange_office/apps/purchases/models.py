from random import randint

from django.utils import timezone
from django.db import models
from django.db.models import Count, Sum

from currencies.models import Currency


class CustomerManager(models.Manager):

    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)

        return self.all()[random_index]


class Customer(models.Model):

    objects = CustomerManager()

    first_name = models.CharField(verbose_name='имя', max_length=20)
    last_name = models.CharField(verbose_name='фамилия', max_length=20)
    phone_number = models.CharField(verbose_name='номер телефона', max_length=20, unique=True)
    created_at = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='дата обновления', auto_now=True)

    def __str__(self):
        return f'{self.first_name}  {self.last_name}'


    class Meta:
        db_table = 'customers'
        verbose_name = "Покупатель"
        verbose_name_plural = "Покупатели"
        ordering = ['-created_at']


class PurchaseManager(models.Manager):
    def get_sum(self, currency: Currency, accessor: str = 'buy'):

        if accessor == 'sale':
            return self.filter(currency_id=currency.id).aggregate(Sum('value'))['value__sum']
        else:
            return self.filter(exchange_currency_id=currency.id).aggregate(Sum('value'))['value__sum']


class Purchase(models.Model):
    objects = PurchaseManager()

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='purchase'
    )

    currency = models.ForeignKey(
        Currency,
        related_name='purchase',
        on_delete=models.CASCADE,
    )

    exchange_currency = models.ForeignKey(
        Currency,
        related_name='exchange_purchase',
        on_delete=models.CASCADE
    )

    value = models.PositiveIntegerField(verbose_name='денежная сумма')
    created_at = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='дата обновления', auto_now=True)

    def __str__(self):
        return f'Денежная сумма: {str(self.value)} пользователя № {str(self.customer)}'

    class Meta:
        db_table = 'purchases'
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'
        ordering = ['-created_at']
