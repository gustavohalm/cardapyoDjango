from rest_framework import serializers
from menu import models


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = '__all__'
        read_only_fields = ['id', 'restaurant']
