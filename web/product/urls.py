
from . import views
from django.urls import path, re_path

app_nam = 'product'
urlpatterns = [
    path('product/', views.product, name='product'),
    path('', views.category, name='category_root'),
    re_path(r'^(?P<hierarchy>.+)/$', views.category, name='category'),
]