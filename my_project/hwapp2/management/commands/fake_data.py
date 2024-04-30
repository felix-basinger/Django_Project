from django.core.management.base import BaseCommand
from hwapp2.models import Client, Product, Order
import random


class Command(BaseCommand):
    help = 'Generate fake clients, products and orders'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            rand_num = random.randint(100, 999)
            client = Client(name=f'Client N{i}',
                            email=f'client{i}{i}@example.com',
                            phone=f'123-456-{rand_num}',
                            address=f'Random street, {i}')
            client.save()
            product = Product(name=f'Product N{i}',
                              description=f'Random description of Product N{i}',
                              price=39.99,
                              count=rand_num)
            product.save()

            for j in range(1, count - 5):
                order = Order.objects.create(customer=client,
                                             total_price=product.price)
                order.products.add(product)
                order.save()
