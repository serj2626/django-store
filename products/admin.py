from django.contrib import admin
from .models import ProductCategory, Product, Basket


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity']


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity']