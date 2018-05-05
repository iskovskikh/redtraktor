
from . import views
from django.urls import path

app_nam = 'product'
urlpatterns = [
    path('', views.index, name='index'),
]