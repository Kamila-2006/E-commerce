from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    parent_name = serializers.CharField(source='parent.name', read_only=True, required=False)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'parent', 'parent_name', 'image', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']