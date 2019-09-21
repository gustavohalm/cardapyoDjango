from django.contrib import admin
from core.models import Table, Restaurant, Category, Product
from menu.models import  Order

# Register your models here.

admin.site.register(Table)
admin.site.register(Restaurant)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)