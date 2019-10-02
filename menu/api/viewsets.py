from rest_framework import viewsets
from . import serializers
from menu import models


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.OrderSerializer

    def get_queryset(self):
        return models.Order.objects.filter(restaurant=self.request.user.restaurants)

    def perform_create(self, serializer):
        serializer.save(restaurant=self.request.user.restaurants)
