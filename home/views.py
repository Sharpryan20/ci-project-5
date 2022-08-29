from django.shortcuts import render

from products.models import Product

def index(request):
    """ A view to return the index page """
    featured_list = Product.objects.filter(featured=True)
    context = {
        'featured_list': featured_list,
    }
    return render(request, 'home/index.html', context)
