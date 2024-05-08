from django.core.management.base import BaseCommand
from myapp.models import Commodity

class Command(BaseCommand):
    help = 'add commodity'
    
    def add_arguments(self, parser):
        parser.add_argument('name', type=str)
        parser.add_argument('description', type=str)
        parser.add_argument('price', type=int)
        parser.add_argument('quantity', type=int)
        
    def handle(self, *args, **options):
        name = options['name']
        description = options['description']
        price = options['price']
        quantity = options['quantity']
        Commodity.objects.create(name=name, description=description, price=price, quantity=quantity)


