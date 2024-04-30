from django.core.management.base import BaseCommand
from hwapp2.models import Product


class Command(BaseCommand):
    help = "Create product."

    def handle(self, *args, **kwargs):
        product = Product(name='Lamp', description='The best lamp in the world', price=19.99,
                          count=5)

        product.save()
        self.stdout.write(f'{product}')
