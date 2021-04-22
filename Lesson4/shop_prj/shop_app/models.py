from django.db import models


class GoodItem(models.Model):

    title = models.CharField(max_length=255, verbose_name='Название')
    date_entrance = models.DateField(verbose_name='Дата поступления', auto_now_add=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена', default=0)
    unit = models.CharField(max_length=2, verbose_name='Единица измерения')
    vendor = models.CharField(max_length=255, verbose_name='Поставщик')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Карточка товара'
        verbose_name_plural = 'Карточки товаров'
