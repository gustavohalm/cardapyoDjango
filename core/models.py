from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=256)
    cnpj = models.CharField(max_length=222)
    state = models.CharField(max_length=32)
    city = models.CharField(max_length=256)
    neighborhood = models.CharField(max_length=256)
    address = models.CharField(max_length=512)
    number = models.CharField(max_length=12)
    cep = models.CharField(max_length=8)
    owner = models.ForeignKey('auth.User', related_name='restaurants', on_delete=models.CASCADE)


class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='tables')
    client = models.CharField(max_length=256)


class Category(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=128)


class Product(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=8, decimal_places=2)
