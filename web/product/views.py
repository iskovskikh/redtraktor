from django.shortcuts import render

# Create your views here.

from django.views import generic

def index(request):
    context = {}
    return render(request, 'product/index.html', context)