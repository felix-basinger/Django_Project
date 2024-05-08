from datetime import timezone, datetime
from django.core.management.base import BaseCommand
from hwapp3.models import Client, Product, Order
import random


class Command(BaseCommand):
    help = 'Generate fake clients, products, and orders'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of each entity to create')

    def random_date_within_days(self, days):
        return timezone.now() - datetime.timedelta(days=random.randint(0, days))

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')

        # Создаем клиентов
        for i in range(1, count + 1):
            client = Client.objects.create(
                name=f'Client N{i}',
                email=f'client{i}@example.com',
                phone=f'123-456-{random.randint(100, 999)}',
                address=f'Random street, {random.randint(1, 100)}'
            )
            client.save()

        # Создаем продукты
        for i in range(1, count + 1):
            product = Product.objects.create(
                name=f'Product N{i}',
                description=f'Description for Product N{i}',
                price=round(random.uniform(10.0, 100.0), 2),
                count=random.randint(1, 100)
            )
            product.save()

        # Создаем заказы
        clients = list(Client.objects.all())
        products = list(Product.objects.all())

        for client in clients:
            for _ in range(random.randint(1, 5)):  # Каждому клиенту от 1 до 5 заказов
                order = Order(
                    customer=client,
                    total_price=round(random.uniform(100.0, 1000.0), 2)
                )
                order.save()
                selected_products = random.sample(products, random.randint(1, min(5, len(products))))
                order.products.set(selected_products)

        self.stdout.write(self.style.SUCCESS(f'Successfully created {count} clients, products, and orders.'))
