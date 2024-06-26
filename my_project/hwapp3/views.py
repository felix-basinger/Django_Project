import logging

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta

from .forms import ProductForm
from .models import Order, Client, Product

logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'hwapp3/index.html')


def list_clients(request):
    clients = Client.objects.all()
    return render(request, 'hwapp3/clients.html', {'clients': clients})


def client_products(request, client_id):
    client = Client.objects.get(id=client_id)
    today = timezone.now()

    periods = {
        'week': today - timedelta(days=7),
        'month': today - timedelta(days=30),
        'year': today - timedelta(days=365),
    }

    products_with_dates = {period: {} for period in periods}

    for period, start_date in periods.items():
        orders = Order.objects.filter(customer=client, date_ordered__gte=start_date)
        for order in orders:
            for product in order.products.all():
                if product not in products_with_dates[period]:
                    products_with_dates[period][product] = []
                products_with_dates[period][product].append(order.date_ordered)

    context = {
        'client': client,
        'products_with_dates': products_with_dates
    }

    return render(request, 'hwapp3/client_products.html', context)


def all_products(request):
    products = Product.objects.all()
    return render(request, 'hwapp3/products.html', {'products': products})


def product_form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        message = 'Заполните форму ещё раз'
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.save()
            message = 'Товар успешно добавлен'
    else:
        form = ProductForm()
        message = 'Добавьте товар'
    return render(request, 'hwapp3/product_form.html',
                  {'form': form, 'message': message})
