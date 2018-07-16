from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from imagekit.processors import ResizeToFit
from imagekit.processors import SmartResize
from django.utils.text import slugify
from unidecode import unidecode
from .storage import MyImageStorage

# Create your models here.

class ShopImage(models.Model):
    caption = models.CharField(max_length=256)
    image = models.ImageField(null=True, blank=True, storage=MyImageStorage())
    image_253x253 = ImageSpecField(source='image',
                                   processors=[ResizeToFit(253, 253, mat_color=(255, 255, 255))],
                                   format='JPEG',
                                   options={'quality': 90})

    image_538x538 = ImageSpecField(source='image',
                                   processors=[ResizeToFit(538, 538, mat_color=(255, 255, 255))],
                                   format='JPEG',
                                   options={'quality': 90})

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return '{} ({})'.format(self.image, self.caption)

class Test(models.Model):
    testcontent= models.CharField(max_length=255)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


# class SpecType(models.Model):
#     caption = models.CharField(max_length=256)

class SpecUnit(models.Model):
    name = models.CharField(max_length=256, unique=True)
    def __str__(self):
        return self.name

class SpecItem(models.Model):
    name = models.CharField(max_length=256)
    unit = models.ForeignKey(SpecUnit, default=None, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Spec(models.Model):
    caption = models.ForeignKey(SpecItem, default=None, null=False, blank=False, on_delete=models.CASCADE)
    value = models.CharField(max_length=256)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=40,blank=True)
    parent = models.ForeignKey('self', default=None, null=True, blank=True, related_name='children',
                               on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    mod_date = models.DateTimeField('date modified')

    def create_slug(self):
        if self.slug == '':
            self.slug = slugify(unidecode(self.name))


    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return '/'.join(full_path[::-1])
    


    # def get_absolute_url(self):
    #     full_url = [self.slug]
    #     k = self.parent
    #     while k is not None:
    #         full_url.append(k.slug)
    #         k = k.parent
    #     return '/'.join(full_url[::-1])

    def get_all_parents(self):
        full_parent = [self]
        k = self.parent
        while k is not None:
            full_parent.append(k)
            k = k.parent
        return full_parent

    def get_all_parents_path(self):
        return self.get_all_parents()[::-1]

    def get_absolute_url(self):
        return '/'.join(map(lambda x: x.slug, self.get_all_parents_path()))

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.pub_date = timezone.now()
        self.mod_date = timezone.now()
        self.create_slug()
        return super(Category, self).save(*args, **kwargs)

    def get_products(self):
        products = Product.objects.filter(category=self)
        return products

    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, unique=True, blank=True)
    sku = models.CharField(max_length=32, unique=True)
    description = models.TextField(null=True, blank=True)
    short_description = models.CharField(max_length=80, null=True, blank=True)
    features = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    images = GenericRelation(ShopImage, related_query_name='products')
    specs = GenericRelation(Spec, related_query_name='products')
    price = models.DecimalField(max_digits=12, decimal_places=2)
    pub_date = models.DateTimeField('date published', auto_now_add = True)
    mod_date = models.DateTimeField('date modified', auto_now = True)

    def create_slug(self):
        if self.slug == '':
            self.slug = slugify(unidecode(self.name))

    def save(self, *args, **kwargs):
        if not self.id:
            self.pub_date = timezone.now()
        self.mod_date = timezone.now()
        self.create_slug()
        return super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '/product' + str(self.slug)

    def __str__(self):
        return self.name
