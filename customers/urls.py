from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'customers', views.CustomerViewSet, basename='customers')

urlpatterns = [
    path('', include(router.urls)),
    path('customers/<int:pk>/orders/', views.CustomerOrdersView.as_view(), name='customer-orders'),
]