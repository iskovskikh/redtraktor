from django.contrib import admin

from .models import *
from django.contrib.contenttypes.admin import GenericTabularInline
from django.forms import TextInput

from import_export import resources
from import_export import fields
from import_export import widgets
from import_export.admin import ImportExportModelAdmin
from django.utils.encoding import force_text
from unidecode import unidecode


# Register your models here.

class ImageInline(GenericTabularInline):
    model = Image
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


from django.utils.encoding import smart_text


class MyCategoryWidjet(widgets.Widget):

    def __init__(self, model, separator=None, *args, **kwargs):
        if separator is None:
            separator = '/'
        self.model = model
        self.separator = separator
        # super(widgets.Widget, self).__init__(*args, **kwargs)

    def clean(self, value, row=None, *args, **kwargs):

        category_parent = None
        category = Category()
        for category_name in value.split(self.separator):
            category, created = Category.objects.get_or_create(
                name = category_name,
                parent = category_parent
                # defaults = {'slug': slugify(unidecode(category_name))}
            )
            category_parent = category

        return category

    def render(self, value, obj=None):
        categories = [item.name for item in value.get_all_parents_path()]
        return self.separator.join(categories)


class MyGenericRelationsWidget(widgets.Widget):
    def __init__(self, model, separator=None, field=None, ):
        if separator is None:
            separator = '\n'
        if field is None:
            field = 'pk'
        self.model = model
        self.field = field
        self.separator = separator
        super(MyGenericRelationsWidget, self).__init__()

    def get_queryset(self, value, row, *args, **kwargs):
        return self.model.objects.all()

    def clean(self, value, row=None, *args, **kwargs):
        if not value:
            return self.model.objects.none()
        # else:
        #
        #     product = value.objects.get('sku')
        #     for item in value.split(self.separator):
        #         temp = item.split(',')
        #         f = open(temp[1], 'rb')
        #         img = value.images.get_or_create()
        #
        #
        #     img = Image()
        # return self.model.objects.filter(**{
        #     '%s__in' % self.field: ids
        # })
        return self.field.ids

    def render_obj(self, obj):
        return smart_text(obj)
        # return str(obj.url, 'utf-8')

    # def render(self, value, obj=None):
    #     ids = [self.render_obj(getattr(obj, self.field)) for obj in value.all()]
    #     return self.separator.join(ids)
    def render(self, value, obj=None):
        ids = [self.render_obj(obj) for obj in value.all()]
        return self.separator.join(ids)


class MyGenericImageWidget(MyGenericRelationsWidget):

    def render_obj(self, obj):
        # return smart_text(obj)
        return '{%s, %s}' % (obj.image.url, obj.caption)


class ProductResource(resources.ModelResource):
    # images = fields.Field(
    #     column_name='images',
    #     attribute='images',
    #     widget=MyGenericImageWidget(Product, field = "image"))  # use a unique field

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
            "sku", "name", "slug", "price", "category", "short_description", "description", "features", "pub_date",
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


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
