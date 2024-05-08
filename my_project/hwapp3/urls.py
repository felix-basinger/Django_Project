from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.list_clients, name='list_clients'),
    path('products/', views.all_products, name='products'),
    path('client/<int:client_id>/products/', views.client_products, name='client_products'),
]
