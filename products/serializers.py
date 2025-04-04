from rest_framework import serializers
from .models import ProductImage, Product


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image', 'is_primary')

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    category_by_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'discount_price', 'category', 'category_name', 'category_by_name', 'stock', 'is_active', 'created_at', 'updated_at', 'images')
        read_only_fields = ('id', 'created_at', 'updated_at')