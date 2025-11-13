from django.shortcuts import render
from django.db import transaction
from store.models import Order, OrderItem, Product, Customer
# request -> response
# request handler


def say_hello(request):
    return render(request, 'hello.html', {'name': 'Mosh'})
