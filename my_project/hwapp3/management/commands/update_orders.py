from django.core.management.base import BaseCommand
from hwapp3.models import Order


class Command(BaseCommand):
    help = "Update order date by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')
        parser.add_argument('date_ordered', type=str, help='Order date')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')

        date_ordered = kwargs.get('date_ordered')
        order = Order.objects.filter(pk=pk).first()
        order.date_ordered = date_ordered
        order.save()
        self.stdout.write(f'{order}')
