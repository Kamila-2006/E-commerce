from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from .pagination import OrderPagination


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = OrderPagination