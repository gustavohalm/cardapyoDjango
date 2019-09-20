from django.db import models

# Create your models he

class Restaurant( models.Model):
    name = models.CharField(max_length=256)
    state = models.CharField(max_length=32)
    city = models.CharField(max_length=256)
    neighborhood = models.CharField(max_length=256)
    address = models.CharField(max_length=512)
    number = models.CharField(max_length=12)
    cep = models.CharField(max_length=8)
    owner = models.ForeignKey('auth.User', related_name='restaurants', on_delete=models.CASCADE)