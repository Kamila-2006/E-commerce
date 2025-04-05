from rest_framework import serializers
from .models import OrderItem, Order


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('product', 'quantity', 'price')

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'customer', 'status', 'total_price', 'shipping_address', 'payment_method', 'items', 'created_at', 'updated_at')
        read_only_fields = ('id', 'total_price', 'created_at', 'updated_at')