from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status', 'total_price', 'shipping_address', 'payment_method', 'created_at', 'updated_at')
    search_fields = ('status', 'shipping_address', 'payment_method')
    inlines = [OrderItemInline]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'price', 'created_at')
    search_fields = ('order__id', 'product__name')