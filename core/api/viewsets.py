from . import serializers
from rest_framework import viewsets
from core import models


class RestaurantViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RestaurantSerializer

    def get_queryset(self):
        return models.Restaurant.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TableViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TableSerializer

    def get_queryset(self):
        return models.Restaurant.objects.filter(restaurant=self.request.user.restaurants)

    def perform_create(self, serializer):
        serializer.save(restaurant = self.request.user.restaurants)


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        return models.Category.objects.filter(restaurant=self.request.user.restaurants)

    def perform_create(self, serializer):
        serializer.save(restaurant=self.request.user.restaurants)


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        return models.Product.objects.filter(restaurant=self.request.restaurants)

    def perform_create(self, serializer):
        serializer.save(restaurant=self.request.user.restaurants)
