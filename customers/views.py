from rest_framework import viewsets

from orders.serializers import OrderSerializer
from .models import Customer
from .serializers import CustomerSerializer
from .pagination import CustomerPagination
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    pagination_class = CustomerPagination

class CustomerOrdersView(APIView):
    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        orders = customer.orders.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=200)