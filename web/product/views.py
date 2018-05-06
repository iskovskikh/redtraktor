from django.shortcuts import render

# Create your views here.

from django.views import generic
from .models import Category
from .models import Product
from django.shortcuts import *
import pprint

def product(request):
    context = {}
    return render(request, 'product/product.html', context)

def category(request, hierarchy= None):

    if hierarchy != None:
        category_slug = hierarchy.split('/')
        category_queryset = list(Category.objects.all())

        parent = get_object_or_404(Category,slug=category_slug[-1])

        path = parent.get_absolute_url().split('/')


        if set(category_slug) != set(path[::-1]):
            raise Http404

        urls = []

    else:
        parent = Category.objects.get(parent=None)
        path = []

    context = {
        'parent':parent,
        'categories': parent.children.all,
        'breadcrumbs': parent.get_all_parents_path(),
    }

    return render(request, 'product/category.html', context)