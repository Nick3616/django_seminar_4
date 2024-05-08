from collections.abc import Iterable
from django.db import models
from django.utils import timezone
from django.db.models import Sum, F

class User(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField(max_length=25)
    phone = models.IntegerField()
    address = models.TextField()
    
    def __str__(self):
        return f'Name: {self.name} Email: {self.email} Phone: {self.phone} Address: {self.address}'
    
class Commodity (models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/commodities', null=True, blank=True)
    
class Order(models.Model):
    name = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    products = models.ManyToManyField(Commodity, through='OrderItem')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    data = models.DateTimeField(default=timezone.now)
    
    def save(self, *args, **kwargs):
        if not self.pk:
            super(Order, self).save(*args, **kwargs)
        current_total = self.orderitem_set.aggregate(
            total=Sum(F('commodity__price') * F('quantity'), output_field=models.DecimalField())
        )['total'] or 0
        if current_total != self.total_amount:
            self.total_amount = current_total
            super(Order, self).save(update_fields=['total_amount'])

    def __str__(self):
        return f"Order {self.id} by {self.name.name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.commodity.name} for {self.order.id}"
