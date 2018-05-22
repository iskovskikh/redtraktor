from django.shortcuts import render

# Create your views here.

from django.views import generic
from .models import Category
from .models import Product
from django.shortcuts import *
import pprint

def product(request, slug = None):


    product = Product.objects.get(slug = slug)

    breadcrumbs = []
    for breadcrumb in product.category.get_all_parents_path():
        breadcrumbs.append({'name':breadcrumb.name, 'url':breadcrumb.get_absolute_url()})
    breadcrumbs.append({'name':product.name, 'url':product.get_absolute_url()})

    context = {
        'product': product,
        'breadcrumbs': breadcrumbs,
    }
    return render(request, 'product/product.html', context)

def category(request, hierarchy= None):

    if hierarchy != None:
        category_slug = hierarchy.split('/')
        # category_queryset = list(Category.objects.all())
        parent = get_object_or_404(Category,slug=category_slug[-1])
        path = parent.get_absolute_url().split('/')
        if set(category_slug) != set(path[::-1]):
            raise Http404
    else:
        parent = Category.objects.get(parent=None)

    breadcrumbs = []
    for breadcrumb in parent.get_all_parents_path():
        breadcrumbs.append({'name': breadcrumb.name, 'url': breadcrumb.get_absolute_url()})

    context = {
        'parent':parent,
        'categories': parent.children.all,
        'products': parent.get_products,
        'breadcrumbs': breadcrumbs,
    }

    return render(request, 'product/category.html', context)