# Generated by Django 2.0.4 on 2018-06-04 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_spec'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='caption',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='spec',
            name='caption',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='spec',
            name='value',
            field=models.CharField(max_length=256),
        ),
    ]