from django.core.management.base import BaseCommand
from hwapp2.models import Client


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        client = Client(name='Simon Peters', email='simon@gmail.com', phone='+37-349-031-31-46',
                        address='Citizen street, 30, California, USA')

        client.save()
        self.stdout.write(f'{client}')
