from django.contrib import admin
from .models import Client, Product, Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'count', 'rating', 'add_time']
    search_fields = ['name', 'description']
    date_hierarchy = 'add_time'


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'register_date']
    search_fields = ['name', 'email', 'phone', 'address']
    date_hierarchy = 'register_date'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'total_price', 'date_ordered']
    ordering = ['customer']
    date_hierarchy = 'date_ordered'


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
