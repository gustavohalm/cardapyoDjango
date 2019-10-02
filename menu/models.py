from django.db import models
from core.models import  Table, Restaurant


class Order(models.Model):

    restaurant = models.ForeignKey('core.Restaurant', related_name='restaurant_orders', on_delete=models.CASCADE)
    table = models.ForeignKey('core.Table', related_name='tables_orders', on_delete=models.CASCADE)
    products = models.ManyToManyField('core.Product', related_name='orders_product')
    total = models.DecimalField(max_digits=8, decimal_places=2)
    KITCHEN_CHOICES = (
        ('pendente', 'pendente'),
        ('cancelado', 'cancelado'),
        ('pronto', 'pronto')
    )
    kitchen_status = models.CharField( max_length=32, choices=KITCHEN_CHOICES)

    TABLE_CHOICES = (
        ('pendente', 'pendente'),
        ('cancelado', 'cancelado'),
        ('pronto', 'pronto')
    )
    table_status = models.CharField(max_length=32, choices=TABLE_CHOICES)

