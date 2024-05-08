from django.core.management.base import BaseCommand, CommandParser
from myapp.models import User

class Command(BaseCommand):
    help = 'Update user'
    
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int)
        parser.add_argument('name', type=str)

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        name = kwargs['name']

        user = User.objects.filter(pk=pk).first()
        user.name = name
        user.save()
        self.stdout.write(f'{user}')


