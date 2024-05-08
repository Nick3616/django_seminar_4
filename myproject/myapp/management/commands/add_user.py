from django.core.management.base import BaseCommand
from myapp.models import User

class Command(BaseCommand):
    help = 'Add a new user to the database'
    
    def add_arguments(self, parser):
        parser.add_argument('name', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('phone', type=str)
        parser.add_argument('address', type=str)

    def handle(self, *args, **options):
        name = options['name']
        email = options['email']
        phone = options['phone']
        address = options['address']
        User.objects.create(name=name, email=email, phone=phone, address=address)
        print('User created successfully')

