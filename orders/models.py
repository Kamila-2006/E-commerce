from django.db import models
from customers.models import Customer
from products.models import Product


class Order(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    total_price = models.DecimalField(max_digits=13, decimal_places=2)
    shipping_address = models.TextField()
    payment_method = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.total_price = sum(item.calculate_total for item in self.items.all())
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.customer} - {self.status}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=13, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def calculate_total(self):
        return self.price * self.quantity

    def save(self, *args, **kwargs):
        if self._state.adding and not self.price:
            self.price = self.product.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product} - {self.quantity} pcs'