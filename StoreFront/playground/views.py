from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Customer, Product
from tags.models import TaggedItem
# request -> response
# request handler

# products ordered & sort by title

# get last 5 orders with their customers and items (incl product)


def say_hello(request):
    queryset = TaggedItem.objects.get_tags_for(Product, 1)
    return render(request, 'hello.html', {'name': 'Ayomide', 'result': list(queryset)})
