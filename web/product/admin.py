from django.contrib import admin

from django.contrib.contenttypes.admin import GenericTabularInline
from import_export import resources
from import_export import fields
from import_export.admin import ImportExportModelAdmin

from .widgets import *
from .models import *

# Register your models here.

class ImageInline(GenericTabularInline):
    model = ShopImage
    extra = 0


class SpecInline(GenericTabularInline):
    model = Spec
    extra = 0


# class ProductAdmin(admin.ModelAdmin):
#     fieldsets = []
#     # formfield_overrides = {
#     #     # Django enforces maximum field length of 14 onto 'title' field when user is editing in the change form
#     #     models.CharField: {'widget': TextInput(attrs={'size': '300'})},
#     # }
#     readonly_fields = ('pub_date', 'mod_date')
#     inlines = [SpecInline, ImageInline]
#
#
#     # list_display = ('question_text', 'pub_date', 'was_published_recently')
#     # list_filter = ['pub_date']
#     # search_fields = ['question_text']


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = []
    # list_display = ('name', 'images')
    inlines = [ImageInline]
    readonly_fields = ('pub_date', 'mod_date')


class ProductResource(resources.ModelResource):
    images = fields.Field(
        column_name='images',
        attribute='images',
        widget=MyGenericImageWidget(Product, field = "image"))  # use a unique field

    category = fields.Field(
        column_name='category',
        attribute='category',
        widget=MyCategoryWidjet(Product)
    )

    # images = fields.Field()
    #
    # def dehydrate_images(self, product):
    #
    #     s = ''
    #
    #     for pr in product.images.all():
    #         s.join(pr.image)
    #     return s

    class Meta:
        model = Product
        import_id_fields = ('sku',)
        export_order = (
            "sku", "name", "slug", "price", "category", "short_description", "images", "description", "features", "pub_date",
            "mod_date",)

        exclude = ("id",)
        # fields = (
        # "sku", "name", "slug", "price", "category", "short_description", "description", "features", "mod_date",)


class ProductAdmin(ImportExportModelAdmin):
    fieldsets = []
    # formfield_overrides = {
    #     # Django enforces maximum field length of 14 onto 'title' field when user is editing in the change form
    #     models.CharField: {'widget': TextInput(attrs={'size': '300'})},
    # }
    readonly_fields = ('pub_date', 'mod_date')
    inlines = [SpecInline, ImageInline]

    resource_class = ProductResource

    # list_display = ('question_text', 'pub_date', 'was_published_recently')
    # list_filter = ['pub_date']
    # search_fields = ['question_text']


class ShopImageAdmin(admin.ModelAdmin):
    fieldsets = []


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ShopImage, ShopImageAdmin)
