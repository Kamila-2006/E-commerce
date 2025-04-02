from django.contrib import admin
from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'discount_price', 'category', 'stock', 'is_active', 'created_at', 'updated_at')
    search_fields = ('name', 'description', 'category')