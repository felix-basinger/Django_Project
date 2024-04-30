from django.core.management.base import BaseCommand
from hwapp2.models import Order


class Command(BaseCommand):
    help = "Create order."

    def handle(self, *args, **kwargs):
        order = Order(customer="John", products=3, total_price=19.99)

        order.save()
        self.stdout.write(f'{order}')