from django.contrib import admin
from .models import *
from django.contrib.contenttypes.admin import GenericTabularInline
from django.forms import TextInput

# Register your models here.

class ImageInline(GenericTabularInline):
    model = Image
    extra = 0

class SpecInline(GenericTabularInline):
    model = Spec
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    fieldsets = []
    # formfield_overrides = {
    #     # Django enforces maximum field length of 14 onto 'title' field when user is editing in the change form
    #     models.CharField: {'widget': TextInput(attrs={'size': '300'})},
    # }
    readonly_fields = ('pub_date', 'mod_date')
    inlines = [SpecInline, ImageInline]


    # list_display = ('question_text', 'pub_date', 'was_published_recently')
    # list_filter = ['pub_date']
    # search_fields = ['question_text']

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = []
    #list_display = ('name', 'images')
    inlines = [ImageInline]
    readonly_fields = ('pub_date', 'mod_date')



admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)