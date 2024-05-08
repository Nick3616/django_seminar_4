from django.core.management.base import BaseCommand
from myapp.models import User, Commodity, Order, OrderItem
from django.utils import timezone

class Command(BaseCommand):
    help = 'add new order'

    def handle(self, *args, **options):
        user = User.objects.get(pk=2)
        commodity1 = Commodity.objects.get(pk=1)
        commodity2 = Commodity.objects.get(pk=2)
        
        order = Order(name=user, data=timezone.now())
        order.save()
        OrderItem.objects.create(order=order, commodity=commodity1, quantity=2)
        OrderItem.objects.create(order=order, commodity=commodity2, quantity=3)
        order.save()

        self.stdout.write(self.style.SUCCESS('Заказ успешно создан.'))