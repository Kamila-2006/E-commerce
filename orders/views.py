from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum, Count
from .models import Order
from .serializers import OrderSerializer
from .pagination import OrderPagination
from products.models import Product
from customers.models import Customer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = OrderPagination

class DashboardStatsView(APIView):

    def get(self, request, *args, **kwargs):
        total_products = Product.objects.count()
        total_orders = Order.objects.count()
        total_customers = Customer.objects.count()
        total_revenue = Order.objects.aggregate(Sum('total_price'))['total_price__sum'] or 0.0

        top_products = Product.objects.annotate(
            total_sold=Count('order_items')
        ).order_by('-total_sold')[:3]

        top_products_data = [
            {
                "id": product.id,
                "name": product.name,
                "total_sold": product.total_sold,
                "revenue": str(product.order_items.aggregate(
                    total_revenue=Sum('price'))['total_revenue'] or 0.0)
            }
            for product in top_products
        ]

        recent_orders = Order.objects.all().order_by('-created_at')[:5]
        recent_orders_data = []
        for order in recent_orders:
            items_data = [
                {
                    "id": item.id,
                    "product": item.product.id,
                    "product_name": item.product.name,
                    "quantity": item.quantity,
                    "price": str(item.price),
                    "created_at": item.created_at.isoformat()
                }
                for item in order.items.all()
            ]
            recent_orders_data.append({
                "id": order.id,
                "customer": order.customer.id,
                "customer_username": order.customer.username,
                "status": order.status,
                "total_price": str(order.total_price),
                "shipping_address": order.shipping_address,
                "payment_method": order.payment_method,
                "items": items_data,
                "created_at": order.created_at.isoformat(),
                "updated_at": order.updated_at.isoformat(),
            })

        data = {
            "total_products": total_products,
            "total_orders": total_orders,
            "total_customers": total_customers,
            "total_revenue": str(total_revenue),
            "top_products": top_products_data,
            "recent_orders": recent_orders_data,
        }

        return Response(data, status=status.HTTP_200_OK)