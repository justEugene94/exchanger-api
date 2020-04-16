from django.db import models

class Currency(models.Model):

    name = models.CharField('имя', max_length = 5)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'