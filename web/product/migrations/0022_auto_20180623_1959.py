# Generated by Django 2.0.4 on 2018-06-23 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_auto_20180623_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=40, unique=True),
        ),
    ]
