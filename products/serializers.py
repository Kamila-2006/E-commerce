from rest_framework import serializers
from .models import ProductImage, Product
from django.db import transaction


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'product', 'image', 'is_primary', 'created_at')
        read_only_fields = ('id', 'created_at')

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)  # ✅ Read uchun
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(), write_only=True  # ✅ Write uchun
    )

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'discount_price', 'category', 'stock', 'is_active', 'created_at', 'updated_at', 'images', 'uploaded_images')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def create(self, validated_data):
        images_data = validated_data.pop('uploaded_images', [])  # ✅ To‘g‘ri maydon
        with transaction.atomic():
            product = Product.objects.create(**validated_data)
            for image in images_data:
                ProductImage.objects.create(product=product, image=image)
        return product
