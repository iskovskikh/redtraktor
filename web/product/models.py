from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=40)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    pub_date = models.DateTimeField('date published')
    mod_date = models.DateTimeField('date modified')

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.pub_date = timezone.now()
        self.mod_date = timezone.now()
        return super(Product, self).save(*args, **kwargs)

class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=40)
    #nesting_level = models.IntegerField()
    product = models.ManyToManyField(Product, blank=True)
    parent = models.ForeignKey('self', default=None, null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    pub_date = models.DateTimeField('date published')
    mod_date = models.DateTimeField('date modified')

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return '/'.join(full_path[::-1])

    def get_absolute_url(self):
        full_url = [self.slug]
        k = self.parent
        while k is not None:
            full_url.append(k.slug)
            k = k.parent
        return '/'.join(full_url[::-1])

    def get_all_parents_path(self):
        full_parent = [self]
        k = self.parent
        while k is not None:
            full_parent.append(k)
            k = k.parent
        return full_parent[::-1]

    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.pub_date = timezone.now()
        self.mod_date = timezone.now()
        return super(Category, self).save(*args, **kwargs)