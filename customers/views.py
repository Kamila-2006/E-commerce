from rest_framework import viewsets
from .models import Customer
from .serializers import CustomerSerializer
from .pagination import CustomerPagination


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    pagination_class = CustomerPagination