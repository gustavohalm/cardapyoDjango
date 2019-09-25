from rest_framework import serializers
from core import models


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Restaurant
        fields = '__all__'
        read_only_fields = ['id', 'owner']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = '__all__'
        read_only_fields = ['id', 'restaurant']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = '__all__'
        read_only_fields = ['id', 'restaurant']


class TableSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Table
        fields = '__all__'
        read_only_fields = ['id', 'restaurant']