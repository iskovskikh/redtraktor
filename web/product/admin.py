from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    fieldsets = []

    readonly_fields = ('pub_date', 'mod_date')
    # inlines = [ChoiceInline]
    # list_display = ('question_text', 'pub_date', 'was_published_recently')
    # list_filter = ['pub_date']
    # search_fields = ['question_text']

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = []
    list_display = ('name', 'image')
    readonly_fields = ('pub_date', 'mod_date')



admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)