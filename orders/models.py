from django.db import models
from catalog.models import Product


class Order(models.Model):
    STATUS_CHOICES = [
        ('nouvelle', 'Nouvelle'),
        ('contactee', 'Contactee'),
        ('confirmee', 'Confirmee'),
        ('livree', 'Livree'),
    ]

    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=30)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='nouvelle')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Commande #{self.id} - {self.name}"

    def get_total(self):
        return sum(item.get_total() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.SET_NULL, null=True)
    product_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def get_total(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.product_name} x{self.quantity}"