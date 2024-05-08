from django.core.management.base import BaseCommand
from myapp.models import User

class Command(BaseCommand):
    help = 'Get all users from the database'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        for user in users:
            self.stdout.write(f'{user.name} {user.email} {user.phone} {user.address}')

