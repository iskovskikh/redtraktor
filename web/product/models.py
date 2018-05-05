from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    pub_date = models.DateTimeField('date published')
    mod_date = models.DateTimeField('date modified')

class Category(models.Model):
    name = models.CharField(max_length=256)
    product = models.ManyToManyField(Product, blank=True)
    parent_category = models.ManyToManyField('self', blank=True)
    image = models.ImageField(null=True, blank=True)
    pub_date = models.DateTimeField('date published')
    mod_date = models.DateTimeField('date modified')