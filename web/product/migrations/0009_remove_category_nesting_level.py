# Generated by Django 2.0.4 on 2018-05-06 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20180506_0957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='nesting_level',
        ),
    ]
