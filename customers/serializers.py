from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer

    class Meta:
        model = Customer
        fields = ('user', 'phone', 'address', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')