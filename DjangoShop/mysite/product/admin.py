from django.contrib import admin
from .models import ProductModel, OrderProduct, Order

# Register your models here.

admin.site.register(ProductModel)
admin.site.register(OrderProduct)
admin.site.register(Order)