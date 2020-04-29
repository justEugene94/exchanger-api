from django.utils import timezone
from django.db import models

from currencies.models import Currency


class Customer(models.Model):

    first_name = models.CharField('имя', max_length=20)
    last_name = models.CharField('фамилия', max_length=20)
    phone_number = models.CharField('номер телефона', max_length=20, unique=True)
    created_at = models.DateTimeField('дата создания', default=timezone.now)

    def __str__(self):
        return f'{self.first_name}  {self.last_name}'


    class Meta:

        db_table = 'customers'

        verbose_name = "Покупатель"
        verbose_name_plural = "Покупатели"


class Purchase(models.Model):

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )

    currency = models.ForeignKey(
        Currency,
        related_name='currency',
        on_delete=models.CASCADE
    )

    exchange_currency = models.ForeignKey(
        Currency,
        related_name='exchange_currency',
        on_delete=models.CASCADE
    )

    value = models.PositiveIntegerField('денежная сумма')

    created_at = models.DateTimeField('дата создания', default=timezone.now)

    def __str__(self):
        return f'Денежная сумма: {str(self.value)} пользователя № {str(self.customer)}'

    class Meta:

        db_table = 'purchases'

        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'