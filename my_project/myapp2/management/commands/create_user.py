from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        user = User(name='John', email='john@mail.com', password='12345', age=24)

        user.save()
        self.stdout.write(f'{user}')
