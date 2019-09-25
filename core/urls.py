from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .api import viewsets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('restaurant',viewsets.RestaurantViewSet, base_name='restaurant_endpoint')

urlpatterns = [
    path('api/v0/', include(router.urls)),
    path('api-auth/', obtain_auth_token)
]