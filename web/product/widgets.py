from django.core.files import File
from django.core.files.images import ImageFile
from django.utils.encoding import smart_text
from django.conf import settings
from import_export import widgets
from import_export import fields
import os
from parse import *
from .models import *


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
                name=category_name,
                parent=category_parent
                # defaults = {'slug': slugify(unidecode(category_name))}
            )
            category_parent = category

        return category

    def render(self, value, obj=None):
        categories = [item.name for item in value.get_all_parents_path()]
        return self.separator.join(categories)


class MyGenericRelationsWidget(widgets.ManyToManyWidget):

    def __init__(self, model, separator=None, field=None, *args, **kwargs):
        if separator is None:
            separator = ';'
        if field is None:
            field = 'pk'
        self.model = model
        self.separator = separator
        self.field = field
        super(MyGenericRelationsWidget, self).__init__(model, separator, *args, **kwargs)

    def get_queryset(self, value, row):
        return self.model.objects.get(
            sku__iexact=row["sku"]
        )

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
        #     img = ProductImage()
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

    def clean(self, value, row=None, *args, **kwargs):
        p = self.get_queryset(value, row)
        p.images.all().delete()
        if value:
            for item in value.split(self.separator):
                if item:
                    u, c = item.split(':')
                    if u and c:
                        p.images.create(caption=c,
                                        image=ImageFile(
                                            File(
                                                open(settings.BASE_DIR + u, 'rb')
                                            ),
                                            name=os.path.basename(u)))
        return p.images.all()

    def render_obj(self, obj):
        return '%s:%s' % (obj.image.url, obj.caption)


class MyGenericSpecWidget(MyGenericRelationsWidget):

    def clean(self, value, row=None, *args, **kwargs):
        p = self.get_queryset(value, row)
        p.specs.all().delete()
        if value:
            for item in value.split(self.separator):
                if item:
                    caption, value_and_unit = item.split(':')
                    if caption and value_and_unit:
                        # val, unit = value_and_unit[:-1].split('[')
                        tmp = value_and_unit[:-1].split('[')
                        if len(tmp)==2:
                            val, unit = tmp
                        else:
                            val = tmp
                            unit = None

                        if unit:
                            u, created = SpecUnit.objects.get_or_create(name=unit)
                            c, created = SpecItem.objects.get_or_create(name=caption, unit=u)
                        else:
                            c, created = SpecItem.objects.get_or_create(name=caption)

                        if val:
                            p.specs.create(caption=c, value=val)

        return p.specs.all()

    def render_obj(self, obj):
        if obj.caption.unit:
            return '%s:%s[%s]' % (obj.caption.name, obj.value, obj.caption.unit.name)
        else:
            return '%s:%s[]' % (obj.caption.name, obj.value)
