from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    register_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Client: {self.name}, email: {self.email}, phone: {self.phone}'


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField()
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Product: {self.name}, price: {self.price}, count: {self.count}'


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Customer ID: {self.customer}, product ID: {self.products}'
