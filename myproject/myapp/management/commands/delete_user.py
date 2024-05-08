from django.core.management.base import BaseCommand
from myapp.models import User

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int)

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        user = User.objects.filter(pk=pk).first()
        if user is not None:
            user.delete()
            self.stdout.write(f'{user}')