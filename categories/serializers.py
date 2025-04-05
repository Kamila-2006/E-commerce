from rest_framework import serializers
from products.models import Product
from .models import Category


class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price')

class CategorySerializer(serializers.ModelSerializer):
    parent_name = serializers.CharField(source='parent.name', read_only=True, required=False)
    products = CategoryProductSerializer(many=True)
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'parent', 'parent_name', 'image', 'products_count', 'products', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at', 'products']

    def get_products_count(self, obj):
        return obj.products.count()