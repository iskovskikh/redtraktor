
from . import views
from django.urls import path

app_nam = 'shop'
urlpatterns = [
    path('', views.index, name='home'),
]