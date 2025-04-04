from django.contrib import admin
from products.models import Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'discount_price', 'category', 'stock', 'is_active', 'created_at', 'updated_at')
    search_fields = ('name', 'description', 'category')

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'is_primary')