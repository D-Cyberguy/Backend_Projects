from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product
# request -> response
# request handler


def say_hello(request):
    queryset = Product.objects.filter(title__iendswith='set')

    return render(request, 'hello.html', {'name': 'Ayomide', 'products': list(queryset)})
