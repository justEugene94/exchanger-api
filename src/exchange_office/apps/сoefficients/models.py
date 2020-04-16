from django.db import models

class CommerceValue(models.Model):

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